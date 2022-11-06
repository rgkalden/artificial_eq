import streamlit as st
import numpy as np
import tensorflow as tf
import pandas as pd

import inference
import config

st.title('Artificial EQ 😎')

with st.form('collect_string'):
    string = st.text_input('Please enter a comment, then click Predict to use machine learning to see what the emotion is!')

    submit_button = st.form_submit_button(label='Predict')

if submit_button:
    col1, col2, col3 = st.columns(3)
    col1.metric('Emotion', 'emotion')
    col2.metric('Emoji', 'emoji')
    col3.metric('Probablility', 'prob')

