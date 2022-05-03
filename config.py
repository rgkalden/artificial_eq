# Emotion labels, 27 + neutral for total of 28.
# Note that ordered alphabetically except for neutral, this is accounted
# for in the model training so predictions still match this list
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

# Constant variables for sequence processing, match what is used in
# the model development notebook
MAX_LENGTH = 30
TRUNC_TYPE = 'post'
VOCAB_SIZE = 10000
EMBEDDING_DIM = 100
OOV_TOKEN = '<oov>'

# File paths for model file and tokenizer
MODEL_PATH = 'model.h5'
TOKENIZER_PATH = 'tokenizer.joblib'