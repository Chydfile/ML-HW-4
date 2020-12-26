import pickle
import catboost
import streamlit as st
import sys
import numpy as np
import pandas as pd
from catboost import CatBoostRegressor
st.title('Предсказание арендной стоимости жилья в Лондоне и близлежащих окрестностях на основании заданных критериев')

col1,= st.beta_columns(1)
with col1:
    st.image("https://s.wsj.net/public/resources/images/BN-IS945_london_G_20150603154805.jpg")
res = []
with open('logisticRegr.pkl', 'rb') as f:
    model = pickle.load(f)

commodities = st.slider('Количество человек', 0, 20, 1)
res.append(commodities)

deposit = st.slider('Депозит, фунты', 0, 4000, 100)
res.append(deposit)

cleaning = st.slider('Стоимость финальной уборки, фунты', 0, 500, 10)
res.append(cleaning)

min_nights = st.slider('Минимальное количество ночей', 0, 500, 10)
res.append(min_nights)

extra_night = st.slider('Удаленность от центра Лондона в км', 0, 10, 1)
res.append(extra_night)

number = st.number_input('Стоимость дополнительного человека, фунты')
st.write('The current number is ', number)
res.append(number)

london = st.number_input('Удаленность от центра Лондона, км')
st.write('Вы ввели', london)
res.append(london)

x_arr = np.array(res)
y = np.expm1(model.predict(x_arr))
st.write(y)
