import pickle
import catboost
import streamlit as st
import sys
import numpy as np
from catboost import CatBoostRegressor
st.title('My first app')
res = []
with open('logisticRegr.pkl', 'rb') as f:
    model = pickle.load(f)
for i in range(6):
#    res.append(st.text_area('name'))
    res.appen(i)
x_arr = np.array(res)
y = np.expm1(model.predict(x_arr))
st.write(y)