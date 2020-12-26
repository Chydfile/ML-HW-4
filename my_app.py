import pickle
import catboost
import streamlit as st
import sys
import numpy as np
import pandas as pd
from catboost import CatBoostRegressor
st.title('Предсказание арендной стоимости жилья для арендодателя на основании заданных критериев')
st.image("https://s.wsj.net/public/resources/images/BN-IS945_london_G_20150603154805.jpg", use_column_width=True)
res = []
with open('logisticRegr.pkl', 'rb') as f:
    model = pickle.load(f)

add_selectbox = st.sidebar.selectbox(
    "*Название города",
    ("Лондон",)
)
st.sidebar.write('*В демонстрационной версии доступен только 1 город - Лондон')
col5, col6 = st.beta_columns(2)
with col5:
    commodities = st.slider('Количество человек', 1, 10, 1)
    res.append(commodities)
with col6:
    district_type = st.selectbox(
    "Тип помещения",
    ('Apartment', 'House', 'Condominium', 'Boat', 'Hostel')
    )
deposit = st.slider('Депозит, фунты', 0, 1000, int(100))
res.append(deposit)

cleaning = st.slider('Стоимость финальной уборки, фунты', 0, 500, int(50))
res.append(cleaning)

col1, col2, col3 = st.beta_columns(3)
with col1:
    number = st.number_input('Минимальное количество ночей', value = int(1), min_value = int(1), max_value = int(10))
    res.append(number)
with col2:
    london = st.number_input('Удаленность от центра, км', value = int(1), min_value = int(0), max_value = int(20))
    res.append(london)
with col3:
    district = st.selectbox(
    "Район",
    ('Camden', 'Hackney', 'Islington', 'Tower Hamlets', 'Lewisham', 'Wandsworth',
    'Hammersmith and Fulham', 'Haringey', 'Southwark', 'Lambeth', 'Sutton',
    'Brent', 'Enfield', 'Harrow', 'Barnet', 'Ealing', 'Newham', 'Hounslow',
    'Redbridge', 'Kensington and Chelsea', 'Croydon', 'Greenwich', 'Westminster',
    'Richmond upon Thames', 'Barking and Dagenham', 'Kingston upon Thames',
    'City of London', 'Merton', 'Waltham Forest', 'Hillingdon', 'Havering',
    'Bexley', 'Bromley')
    )
res.append(district)
res.append(district_type)
x_arr = np.array(res)
y = np.expm1(model.predict(x_arr))
st.write('Примерная стоимость аренды за ночь', int(y))
