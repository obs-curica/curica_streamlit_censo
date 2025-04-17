import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

from scripts.load_data import carregar_dados
from scripts.graficos import grafico_alunos_por_municipio
from scripts.graficos import grafico_escolas_por_municipio
from scripts.graficos import grafico_escolas_por_dependencia
from scripts.graficos import grafico_alunos_por_dependencia

# Configuração visual
plt.style.use('dark_background')
COR_TEXTO = '#FFA07A'
CORES_BARRAS = ['#B0E0E6', '#FFC107']
st.set_page_config(page_title="Panorama Rede de Ensino", layout="wide", page_icon="🦜")

# Carregar os dados
url_panorama = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_geral/df_panorama_geral.csv"
df_panorama_geral = carregar_dados(url_panorama)


# Título da página
st.title("🏫 Panorama da Rede Pública de Ensino do Estado do Acre")
st.write("Esta página apresenta uma análise da rede de ensino do estado do Acre, com base nos dados do Censo Escolar.")
st.write(df_panorama_geral.head(5))

#============================
# Seção 01 - Caracterização da Rede de Ensino
#============================
st.header("Caracterização da Rede de Ensino")
st.write("Texto explicativo.")

# Subseção 01.1 - Total de Alunos e Escolas por Município
st.subheader("Total de Alunos e Escolas por Município")
st.write("Abaixo será apresentada a caracterização da rede de ensino, discriminando o número total de escolas e alunos por ano e por Município.")

# Selectbox do ano do Censo Escolar
ano_censo = st.selectbox("Selecione o ano do Censo Escolar:", sorted(df_panorama_geral['NU_ANO_CENSO'].unique()))
col1, col2 = st.columns(2)

with col1:
    grafico_alunos_por_municipio(df_panorama_geral, ano_censo)

with col2:
    grafico_escolas_por_municipio(df_panorama_geral, ano_censo)

# Texto de análise dos gráficos
st.write("Texto analítico.")

# Subseção 01.2 - Total de Alunos e Escolas por Dependência Administrativa
st.subheader("Total de Alunos e Escolas por Dependência Administrativa")
st.write("Abaixo será realizada a caracterização da rede de ensino, discriminando a dependência administrativa a qual a escola está vinculada, se Municial, Estadual ou Federal. Total e por Município.")

# Divide a tela em duas colunas
col1, col2 = st.columns(2)
# Gráfico do total de alunos por dependência
with col1:
    grafico_alunos_por_dependencia(df_panorama_geral, ano_censo)
# Gráfico do total de escolas por dependência
with col2:
    grafico_escolas_por_dependencia(df_panorama_geral, ano_censo)


#===============================
# Seção 02 - Urbano vs. Rural
#===============================
st.header("Urbano vs. Rural")
st.write("Texto explicativo")

st.write("Número de alunos por localização (Urbana/Rural).")

# Gráficos = Coluna 1 total no Estado, Coluna 2 total do Município

st.write("Número de escolas por localização (Urbana/Rural).")

# Grafico do total de alunos por localização, por Município

st.subheader("Escolas em localização diferenciada")
st.write("Texto explicativo")

# Grafico do total de alunos por localização diferenciada

st.subheader("Escolas em Terra Indígena")

st.subheader("Escolas em Projeto de Assentamento do INCRA")

st.subheader("Escolas em área onde habitam populações tradicionais")
st.write("Problematizar o endereço da escola que contém a palavra rio e se está marcada com localização diferenciada. Falar das Unidades de Conservação, Reservas Extrativistas e ribeirinhos.")

st.subheader("Geração de relatórios")
st.write("Seegue abaixo ferramente para geração de relatórios para download. Basta selecionar os filtros desejados e clicar no botão de download.")