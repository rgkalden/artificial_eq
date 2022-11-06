# import inference.py script functions and variables
import inference
# import config file for global variables and file paths
import config


def predict(comment):

    # Load model and tokenizer
    model = inference.load_model(config.MODEL_PATH)
    tokenizer = inference.load_tokenizer(config.TOKENIZER_PATH)

    # Get comment that is entered, prepare data
    prepared_comment = inference.prepare_comment(
        comment, tokenizer, max_length=config.MAX_LENGTH, trunc_type=config.TRUNC_TYPE)

    # Make prediction
    emotion, prob = inference.predict_emotion(model, prepared_comment)

    # Match emoji to predicted emotion
    emoji = config.EMOJI_MAP[emotion]

    return emotion, emoji, prob
