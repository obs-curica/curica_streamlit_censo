import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

from scripts.utils import carregar_dados
from scripts.graficos import grafico_matriculas_por_localizacao_diferenciada
from scripts.graficos import grafico_escolas_por_localizacao_diferenciada
from scripts.graficos import grafico_matriculas_por_localizacao_diferenciada_municipio
from scripts.graficos import grafico_escolas_por_localizacao_diferenciada_municipio

# Configuração da página
st.set_page_config(page_title="Panorama Povos e Populações Tradicionais", layout="wide", page_icon="🦜")
# Carregar os dados
url_panorama = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_geral/df_panorama_geral.csv"
df_panorama_geral = carregar_dados(url_panorama)

# Título da página
st.title("Panorama da Educação: Povos e Populações Tradicionais")
st.write("Esta página apresenta uma análise da educação dos povos e populações tradicionais do estado do Acre, com base nos dados do Censo Escolar.")

st.header("Escolas em localização diferenciada")
st.write("Texto explicativo.")
st.write("Explicar que o campo Comunidades Tradicionais, somente a partir de 2024.")

# Definicao do ano do Censo Escolar
anos_disponiveis = sorted(df_panorama_geral['NU_ANO_CENSO'].unique())
ano_mais_recente = max(anos_disponiveis)

ano_censo = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente)
)

# Criação do dataframe para localização diferenciada
df_localizacao_diferenciada = df_panorama_geral[
    (df_panorama_geral['TP_LOCALIZACAO_DIFERENCIADA'] != 0) & 
    (df_panorama_geral['NU_ANO_CENSO'] == ano_censo) &
    (df_panorama_geral['TP_LOCALIZACAO_DIFERENCIADA'].notnull())
]

st.write("Número total de escolas declaradas em localização diferenciada: ", df_localizacao_diferenciada['TP_LOCALIZACAO_DIFERENCIADA'].count())

# Gráficos
col1, col2 = st.columns(2)
# Gráfico do total de alunos por localização diferenciada
with col1:
    grafico_matriculas_por_localizacao_diferenciada(df_panorama_geral, ano_censo)
# Gráfico do total de escolas por localização diferenciada
with col2:
    grafico_escolas_por_localizacao_diferenciada(df_panorama_geral, ano_censo)
# Texto de análise dos gráficos
st.write("Texto analítico.")

# Tabela de localização por Município
with st.form("form_localizacao_diferenciada"):
    ano_censo_localizacao = st.selectbox("Selecione o ano do Censo Escolar:", sorted(df_panorama_geral['NU_ANO_CENSO'].unique()), key ="ano_censo_localizacao_diferenciada")

    municipio_localizacao = st.selectbox("Selecione o município:", sorted(df_panorama_geral['NO_MUNICIPIO'].unique()), key="municipio_localizacao_diferenciada")
    
    # localizacao = st.selectbox("Selecione a localização:", sorted(df_panorama_geral['TP_LOCALIZACAO'].unique()), key="localizacao")
    submitted = st.form_submit_button("Gerar Dados")
    if submitted:
        col1, col2 = st.columns(2)
        with col1:
            st.write(grafico_matriculas_por_localizacao_diferenciada_municipio(df_panorama_geral, ano_censo_localizacao, municipio_localizacao))
        # Gráfico do total de escolas por localização    
        with col2:
            grafico_escolas_por_localizacao_diferenciada_municipio(df_panorama_geral, ano_censo_localizacao, municipio_localizacao)
    
        # Texto de análise dos gráficos
        st.write("Existem Unidades de Conservação no território de seu Município? E os ribeirinhos? Há populações tradicionais habitando esses espaços? Existem escolas na localidade?")

# Subseção 02.3 - Total de Alunos e Escolas em Projeto de Assentamento do INCRA
st.header("Escolas em Projeto de Assentamento do INCRA")

# Subseção 02.2 - Total de Alunos e Escolas em Terra Indígena
st.header("Escolas em Terra Indígena")

# Subseção 02.4 - Total de Alunos e Escolas em área de população tradicionais
st.header("Escolas em área onde habitam populações tradicionais")
st.write("Problematizar o endereço da escola que contém a palavra rio e se está marcada com localização diferenciada. Falar das Unidades de Conservação, Reservas Extrativistas e ribeirinhos.")

#===============================
# Seção 03 - Geração de Relatórios
#===============================
st.header("Geração de relatórios")
st.write("Seegue abaixo ferramente para geração de relatórios para download. Basta selecionar os filtros desejados e clicar no botão de download.")