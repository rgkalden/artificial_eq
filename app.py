import numpy as np
import tensorflow as tf
import pandas as pd
from flask import Flask, request, render_template

# import inference.py script functions and variables
import inference
# import config file for global variables and file paths
import config

app = Flask(__name__)

# Initialize pandas DataFrame to store comments entered and the model output results
df = pd.DataFrame(columns=['Comment', 'Emotion', 'Emoji', 'Probability'])

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict(df=df):

    # Load model and tokenizer
    model = inference.load_model(config.MODEL_PATH)
    tokenizer = inference.load_tokenizer(config.TOKENIZER_PATH)

    # Get comment that is entered, prepare data
    comment = request.form.values()
    prepared_comment = inference.prepare_comment(
        comment, tokenizer, max_length=config.MAX_LENGTH, trunc_type=config.TRUNC_TYPE)

    # Make prediction
    emotion, prob = inference.predict_emotion(model, prepared_comment)

    # Match emoji to predicted emotion
    emoji = config.EMOJI_MAP[emotion]

    

    # NEW: Store results in new row of DataFrame
    new_row = {'Comment': request.form['comment'], 'Emotion': emotion, 'Emoji': emoji, 'Probability': '{}%'.format(int(round(prob * 100)))}
    df = df.append(new_row, ignore_index=True)

    # NEW: Render template with DataFrame as table
    return render_template('index.html', tables=[df.to_html(classes='results')], titles=df.columns.values)

    """ return render_template('index.html',
                           emoji_output = emoji,
                           comment_text=request.form['comment'],
                           prediction_text=emotion,
                           probability='{}%'.format(int(round(prob * 100))))
 """

if __name__ == "__main__":
    app.run(debug=True)
