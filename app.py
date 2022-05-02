import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template

# import inference.py script functions and variables
import inference

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    model_path = 'baseline-glove-2022-04-28-19-08-04-test-acc-0.505.h5'
    model = inference.load_model(model_path)

    tokenizer_path = 'tokenizer.joblib'
    tokenizer = inference.load_tokenizer(tokenizer_path)

    comment = request.form.values()

    prepared_comment = inference.prepare_comment(
        comment, tokenizer, max_length=inference.MAX_LENGTH, trunc_type=inference.TRUNC_TYPE)

    emotion, prob = inference.predict_emotion(model, prepared_comment)

    return render_template('index.html', comment_text='The comment is: {}'.format(request.form['comment']),
                            prediction_text='The emotion is: {}'.format(emotion),
                            probability='Probability: {}%'.format(int(round(prob * 100))))


if __name__ == "__main__":
    app.run(debug=True)
