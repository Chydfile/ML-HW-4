import pickle
import catboost
import streamlit as st
import sys
import numpy as np
st.text('This is some text.')

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')