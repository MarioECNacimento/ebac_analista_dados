import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import time

st.set_page_config(layout = 'wide')

df = pd.read_csv('previsao_de_renda.csv')
df = df.drop('Unnamed: 0', axis = 1)
df['log_renda'] = np.log(df['renda'])

st.markdown("<h1 style='text-align: center; color: black;'>Modulo 15 - Exercicio 02 - StreamLit </h1>", unsafe_allow_html=True)

st.markdown('------')
st.markdown('#### *Dataframe com as informações sobre a previsão de crédido*')
st.markdown(' - As variáveis explicativas são: Tipo de renda, posse de veiculo, posse de imovel, estado civil, escolaridade')
st.markdown(' - As variáveis respostas são: renda, log de renda')
st.markdown('------')

st.dataframe(df)
st.markdown('------')

st.sidebar.markdown('#### OPÇÕES')
opt = st.sidebar.selectbox(
    'Qual Gráfico de BoxPlot Gostaria de Observar?',
    ('Tipo de Renda x Renda', 'Posse de Veiculo x Renda', 
    'Posse de Imovel x Renda', 'Escolaridade x Renda', 
    'Estado Civil x Renda'))

if opt == 'Posse de Veiculo x Renda':
    st.markdown('#### Gráfico BoxPlot')
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='posse_de_veiculo', y='log_renda', data=df)
    plt.ylabel('Log de Renda')
    plt.xlabel('Posse de Veiculo')
    st.pyplot(fig)
    st.markdown('------')

elif opt == 'Posse de Imovel x Renda':
    st.markdown('#### Gráfico BoxPlot')
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='posse_de_imovel', y='log_renda', data=df)
    plt.ylabel('Log de Renda')
    plt.xlabel('Posse de Imovel')
    st.pyplot(fig)
    st.markdown('------')

elif opt == 'Escolaridade x Renda':
    st.markdown('#### Gráfico BoxPlot')
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='educacao', y='log_renda', data=df)
    plt.ylabel('Log de Renda')
    plt.xlabel('Escolaridade')
    st.pyplot(fig)
    st.markdown('------')

elif opt == 'Estado Civil x Renda':
    st.markdown('#### Gráfico BoxPlot')
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='estado_civil', y='log_renda', data=df)
    plt.ylabel('Log de Renda')
    plt.xlabel('Estado Civil')
    st.pyplot(fig)
    st.markdown('------')

else:
    st.markdown('#### Gráfico BoxPlot')
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='tipo_renda', y='log_renda', data=df)
    plt.ylabel('Log de Renda')
    plt.xlabel('Tipo de Renda')
    st.pyplot(fig)
    st.markdown('------')

if st.sidebar.button('Estatistica Descritiva'):
    st.markdown('#### Estatistica Descritiva das variáveis do DataFrame')
    st.table(df.describe())
    st.markdown('------')

if st.sidebar.button('Grafico 1'):
    st.markdown('#### Gráfico BoxPlot')
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='tipo_renda', y='log_renda', hue='educacao', data=df)
    plt.ylabel('Log de Renda')
    plt.xlabel('Tipo de Renda')
    st.pyplot(fig)
    st.markdown('------')

if st.sidebar.button('Grafico 2'):
    st.markdown('#### Gráfico BoxPlot')
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='tipo_renda', y='log_renda', hue='posse_de_veiculo', data=df)
    plt.ylabel('Log de Renda')
    plt.xlabel('Tipo de Renda')
    st.pyplot(fig)
    st.markdown('------')

if st.sidebar.button('Grafico 3'):
    st.markdown('#### Gráfico BoxPlot')
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='tipo_renda', y='log_renda', hue='posse_de_imovel', data=df)
    plt.ylabel('Log de Renda')
    plt.xlabel('Tipo de Renda')
    st.pyplot(fig)
    st.markdown('------')

if st.sidebar.button('Grafico 4'):
    st.markdown('#### Gráfico BoxPlot')
    fig = plt.figure(figsize=(10, 4))
    sns.boxplot(x='tipo_renda', y='log_renda', hue='sexo', data=df)
    plt.ylabel('Log de Renda')
    plt.xlabel('Tipo de Renda')
    st.pyplot(fig)
    st.markdown('------')

