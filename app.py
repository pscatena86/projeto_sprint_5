import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')
st.header('Dashboard de Vendas de Carros')

if st.link_button: # se o botão for clicado
            # escrever uma mensagem
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
            fig = px.histogram(car_data, x="odometer")
        
            # exibir um gráfico Plotly interativo
            st.plotly_chart(fig, use_container_width=True)

# SEGUNDO BOTÃO (gráfico de dispersão) - novo!
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para mostrar a relação entre quilometragem e preço')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
  st.write('Criando um histograma para a coluna odometer')
fig = px.histogram(car_data, x="odometer")