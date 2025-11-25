
import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.title ("Analisis de datos anuncios de venta de autos")
show_disp = st.checkbox('Mostrar gráfico de dispersión')#Botón para mostrar el gráfico de dispersión
if show_disp:
    st.write('Creacion de grafico de dispersion para el conjunto de datos anunciados de venta de autos')
fig = px.scatter(car_data, x="odometer", y="price") #Crear un gráfico de dispersión
st.plotly_chart(fig) #Gráfico de dispersión

show_hist = st.checkbox('Construir un histograma')# Botón para mostrar el histograma
if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
fig = px.histogram(car_data, x="odometer") #Crear historiograma
st.plotly_chart(fig, use_container_width=True) #Historiograma

