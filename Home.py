import streamlit as st
import predict

st.set_page_config(page_title="Artificial EQ", page_icon="😎")

st.title('Artificial EQ 😎')

with st.form('collect_string'):
    text_input = st.text_input(label='Please enter a comment, then click Predict to use machine learning to see what the emotion is!',
                               value='What a cool guy')

    comment = [text_input]

    submit_button = st.form_submit_button(label='Predict')

if submit_button:

    emotion, emoji, prob = predict.predict(comment)

    col1, col2, col3 = st.columns(3)
    col1.metric('Emotion', emotion)
    col2.metric('Emoji', emoji)
    col3.metric('Probability (%)', int(prob * 100))
