import numpy as np
import tensorflow as tf
from joblib import load
from tensorflow.keras.preprocessing.sequence import pad_sequences

MAX_LENGTH = 30
TRUNC_TYPE = 'post'

LABELS = [
    'admiration',
    'amusement',
    'anger',
    'annoyance',
    'approval',
    'caring',
    'confusion',
    'curiosity',
    'desire',
    'disappointment',
    'disapproval',
    'disgust',
    'embarrassment',
    'excitement',
    'fear',
    'gratitude',
    'grief',
    'joy',
    'love',
    'nervousness',
    'optimism',
    'pride',
    'realization',
    'relief',
    'remorse',
    'sadness',
    'surprise',
    'neutral',
]


def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    print('Model loaded from', model_path)
    return model


def load_tokenizer(path):
    tokenizer = load(path)
    print('Tokenizer loaded from', path)
    return tokenizer


def input_comment():
    default = 'This is a super happy comment'
    comment_text = input('Please enter a comment: ') or default

    comment = []
    comment.append(comment_text)

    if comment_text == default:
        print('Using default comment:', comment_text)

    return comment


def prepare_comment(comment, tokenizer, max_length=MAX_LENGTH, trunc_type=TRUNC_TYPE, print_sequence=False):
    sequence = tokenizer.texts_to_sequences(comment)
    padded_sequence = pad_sequences(
        sequence, maxlen=max_length, truncating=trunc_type)
    if print_sequence == True:
        print(padded_sequence)
    return padded_sequence


def predict_emotion(prepared_comment, print_prediction=False, print_index=False, print_emotion=True):
    print('Predicting...')
    prediction = model.predict(prepared_comment)
    if print_prediction == True:
        print(prediction)

    label_index = np.argmax(prediction)
    if print_index == True:
        print('LABEL index', label_index)

    emotion = LABELS[label_index]
    if print_emotion == True:
        print('The emotion is:', emotion)

    return emotion


if __name__ == '__main__':
    model_path = 'baseline-glove-2022-04-28-19-08-04-test-acc-0.505.h5'
    model = load_model(model_path)

    tokenizer_path = 'tokenizer.joblib'
    tokenizer = load_tokenizer(tokenizer_path)

    comment = input_comment()

    prepared_comment = prepare_comment(
        comment, tokenizer, max_length=30, trunc_type='post')

    emotion = predict_emotion(prepared_comment)
