import pickle
import catboost
import streamlit as st
import sys
import numpy as np
from catboost import CatBoostRegressor

res = []
with open('logisticRegr.pkl', 'rb') as f:
    model = pickle.load(f)
for i in range(6):
    res.append(st.write())

x_arr = np.array(res)
y = np.expm1(model.predict(x_arr))
st.text_area(y)