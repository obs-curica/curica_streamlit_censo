import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re


from scripts.graficos import plot_agua_potavel_por_municipio
from scripts.utils import carregar_dados

# Configuração visual
plt.style.use('dark_background')
COR_TEXTO = '#FFA07A'
CORES_BARRAS = ['#B0E0E6', '#FFC107']

st.set_page_config(page_title="Panorama Água Potável", layout="wide", page_icon="🦜")

# Título da página
st.title('💧 Panorama da Oferta de Água Potável')

# Texto introdutório
st.write("Esta página apresenta uma análise do fornecimento de água potável nas escolas públicas do estado do Acre, com base nos dados do Censo Escolar.") 

# Subtítulo 
st.subheader("Análise do Fornecimento de Água Potável nas Escolas Públicas do Acre")

# Texto subtítulo
st.write("Análise da oferta de água potável segundo a marcação do campo no Censo Escolar.")
st.write("Você pode filtrar os dados por ano, localização (urbana ou rural), condição de fornecimento de água e Município.")

# Carregar os dados
url_agua = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua.csv"
df_censo_agua = carregar_dados(url_agua)

# Filtros de Seleção
# Seleção do ano do Censo Escolar
ano_censo = st.selectbox("Selecione o ano do Censo Escolar:", options=df_censo_agua['NU_ANO_CENSO'].unique())

# Seleção de Localização (Urbana/Rural)
localizacao = st.selectbox("Selecione a Localização (Urbana ou Rural):", options=["Urbana", "Rural"]) 

# Filtro de Fornecimento de Água
agua_potavel = st.selectbox("Selecione a condição de fornecimento de Água Potável:", options=["Sim", "Não"])

# Filtro de Município
municipio_selecionado = st.selectbox("Selecione o Município:", options=df_censo_agua['NO_MUNICIPIO'].unique())

# Mapeando valores para filtros
localizacao_map = {"Urbana": 1, "Rural": 2}
agua_map = {"Sim": 1, "Não": 0}

# Filtrando os dados com base nas seleções
df_filtered = df_censo_agua[
    (df_censo_agua['NU_ANO_CENSO'] == ano_censo) &
    (df_censo_agua['TP_LOCALIZACAO'] == localizacao_map[localizacao]) &
    (df_censo_agua['IN_AGUA_POTAVEL'] == agua_map[agua_potavel]) &
    (df_censo_agua['NO_MUNICIPIO'] == municipio_selecionado)
]


# Exibe o DataFrame filtrado
st.write(f"Exibindo dados filtrados para {municipio_selecionado} - {localizacao} - {agua_potavel}:")
st.write(df_filtered[['NU_ANO_CENSO', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'CO_ENTIDADE', 'TP_LOCALIZACAO', 'QT_MAT_BAS', 'IN_AGUA_POTAVEL']])

# Subtítulo gráfico
st.subheader("Gráfico com o total de escolas do Município, por tipo de fornecimento de água.")

# Filtrar o DataFrame apenas pelo ano e município (não inserir água potável aqui!)
plot_agua_potavel_por_municipio(df_censo_agua, ano_censo, municipio_selecionado, CORES_BARRAS, COR_TEXTO)