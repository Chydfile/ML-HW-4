import pickle
import catboost
import streamlit as st
import sys
import numpy as np
st.text('This is some text.')

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

genre = st.radio(
"What's your favorite movie genre",
('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

title = st.text_input('Movie title', 'Life of Brian')

number = st.number_input('Insert a number')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

col1,= st.beta_columns(1)
with col1:
    st.header("Предсказание арендной стоимости жилья в Лондоне и близлежащих окрестностях на основании заданных критериев")
    st.image("https://s.wsj.net/public/resources/images/BN-IS945_london_G_20150603154805.jpg")