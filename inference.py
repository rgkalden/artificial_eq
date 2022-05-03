import numpy as np
import tensorflow as tf
from joblib import load
from tensorflow.keras.preprocessing.sequence import pad_sequences

# import config file for global variables and file paths
import config


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


def prepare_comment(comment, tokenizer, max_length=config.MAX_LENGTH, trunc_type=config.TRUNC_TYPE, print_sequence=False, print_comment=False):
    sequence = tokenizer.texts_to_sequences(comment)
    padded_sequence = pad_sequences(
        sequence, maxlen=max_length, truncating=trunc_type)
    
    if print_comment == True:
        print(comment)
    if print_sequence == True:
        print(padded_sequence)
    
    return padded_sequence


def predict_emotion(model, prepared_comment, print_prediction=False, print_index=False, print_emotion=True):
    print('Predicting...')
    prediction = model.predict(prepared_comment)
    if print_prediction == True:
        print(prediction)

    label_index = np.argmax(prediction)
    prob = np.max(prediction)

    if print_index == True:
        print('LABEL index', label_index)

    emotion = config.LABELS[label_index]
    if print_emotion == True:
        print('The emotion is:', emotion)
        print('Probability: {}%'.format(int(round(prob * 100))))

    return emotion, prob


if __name__ == '__main__':
    
    model = load_model(config.MODEL_PATH)

    tokenizer = load_tokenizer(config.TOKENIZER_PATH)

    comment = input_comment()

    prepared_comment = prepare_comment(
        comment, tokenizer, max_length=config.MAX_LENGTH, trunc_type=config.TRUNC_TYPE)

    emotion, prob = predict_emotion(model, prepared_comment)
