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
st.write('The current movie title is', title)

number = st.number_input('Insert a number')
st.write('The current number is ', number)

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


st.header("Предсказание арендной стоимости жилья в Лондоне и близлежащих окрестностях на основании заданных критериев")
st.image("https://cdn.londonandpartners.com/-/media/images/london/business/tower-bridge-1920x580/towerbridgeheronew.jpg?mw=1920&hash=98F25194979A1578C5364EF0897462B0C5EF60B5")