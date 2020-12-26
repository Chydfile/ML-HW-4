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

commodities = st.slider('Количество человек', 1, 20, 1)
res.append(commodities)

deposit = st.slider('Депозит, фунты', 0, 1000, 100)
res.append(deposit)

cleaning = st.slider('Стоимость финальной уборки, фунты', 0, 500, 50)
res.append(cleaning)

number = st.number_input('Минимальное количество ночей', value = int(1), min_value = int(1), max_value = int(10))
res.append(number)

london = st.number_input('Удаленность от центра Лондона, км', value = int(1), min_value = int(0), max_value = int(20))
res.append(london)

district = st.sidebar.selectbox(
    "Район Лондона",
    ('Camden', 'Hackney', 'Islington', 'Tower Hamlets', 'Lewisham', 'Wandsworth',
 'Hammersmith and Fulham', 'Haringey', 'Southwark', 'Lambeth', 'Sutton',
 'Brent', 'Enfield', 'Harrow', 'Barnet', 'Ealing', 'Newham', 'Hounslow',
 'Redbridge', 'Kensington and Chelsea', 'Croydon', 'Greenwich', 'Westminster',
 'Richmond upon Thames', 'Barking and Dagenham', 'Kingston upon Thames',
 'City of London', 'Merton', 'Waltham Forest', 'Hillingdon', 'Havering',
 'Bexley', 'Bromley')
)
res.append(distric)
x_arr = np.array(res).reshape(1, -1)
y = np.expm1(model.predict(x_arr))
st.write('Стоимость жилья за ночь', y)
