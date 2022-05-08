import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template

# import inference.py script functions and variables
import inference
# import config file for global variables and file paths
import config

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    model = inference.load_model(config.MODEL_PATH)

    tokenizer = inference.load_tokenizer(config.TOKENIZER_PATH)

    comment = request.form.values()

    prepared_comment = inference.prepare_comment(
        comment, tokenizer, max_length=config.MAX_LENGTH, trunc_type=config.TRUNC_TYPE)

    emotion, prob = inference.predict_emotion(model, prepared_comment)

    # Match emoji to predicted emotion
    emoji = config.EMOJI_MAP[emotion]

    return render_template('index.html',
                           emoji_output = emoji,
                           comment_text=request.form['comment'],
                           prediction_text=emotion,
                           probability='{}%'.format(int(round(prob * 100))))


if __name__ == "__main__":
    app.run(debug=True)
