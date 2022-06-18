from operator import index
import numpy as np
import tensorflow as tf
import pandas as pd
from flask import Flask, request, render_template

# import inference.py script functions and variables
import inference
# import config file for global variables and file paths
import config

app = Flask(__name__)

# Initialize list to store comments entered and the model output results
data = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict(data=data):

    # Load model and tokenizer
    model = inference.load_model(config.MODEL_PATH)
    tokenizer = inference.load_tokenizer(config.TOKENIZER_PATH)

    # Get comment that is entered, prepare data
    comment = request.form.values()
    prepared_comment = inference.prepare_comment(
        comment, tokenizer, max_length=config.MAX_LENGTH, trunc_type=config.TRUNC_TYPE)

    # Make prediction
    emotion, prob = inference.predict_emotion(model, prepared_comment)
    prob_string = '{}%'.format(int(round(prob * 100)))

    # Match emoji to predicted emotion
    emoji = config.EMOJI_MAP[emotion]

    # NEW: Store results in new row of list
    new_row = [request.form['comment'], emotion, emoji, prob_string]
    data.append(new_row)
    df = pd.DataFrame(
        data, columns=['Comment', 'Emotion', 'Emoji', 'Probability'])
    df.sort_index(axis=0, ascending=False, inplace=True)
    
    # Only Show last 5 comments
    df = df.iloc[:5]

    # NEW: Render template with DataFrame as table
    return render_template('index.html', tables=[df.to_html(classes='results', index=False)], titles=df.columns.values)


if __name__ == "__main__":
    app.run(debug=True)
