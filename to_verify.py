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

title = st.text_input(max_value(int),'Movie title', 'Life of Brian')
st.write('The current movie title is', title)