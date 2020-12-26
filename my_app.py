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
res.append(st.text_area('name1'))
res.append(st.text_area('name2'))
res.append(st.text_area('name3'))
res.append(st.text_area('name4'))
res.append(st.text_area('name5'))
res.append(st.text_area('name6'))
x_arr = np.array(res)
y = np.expm1(model.predict(x_arr))
st.write(y)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)