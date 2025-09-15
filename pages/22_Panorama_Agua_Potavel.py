import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re



from scripts.utils import(carregar_dados,
                          COLUNAS_RENOMEADAS_CENSO
)

from scripts.textos import(texto_pan_agua_intro,
                           texto_pan_agua_metodologia,
                           texto_pan_agua_dados_brutos_intro
)

from scripts.graficos import grafico_agua_dados_brutos

# Configuração visual
plt.style.use('dark_background')
COR_TEXTO = '#FFA07A'
CORES_BARRAS = ['#B0E0E6', '#FFC107']

# Corregar dados
url_df_panorama_agua = 'https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_panorama_agua.csv'
df_panorama_agua = carregar_dados(url_df_panorama_agua)
#df_panorama_agua = df_panorama_agua.astype(str)

st.set_page_config(page_title="Panorama Água Potável", layout="wide", page_icon="🦜")

# Título da página
st.title('💧 Panorama da Oferta de Água Potável')
st.write(texto_pan_agua_intro()) 

#++++++++
# Subseção Metodologia
st.header('Metodologia')
st.write(texto_pan_agua_metodologia())

#++++++++
# Subseção dados brutos do Censo Escolar
st.header('Oferta de água potável segundo os dados brutos do Censo Escolar')
st.write(texto_pan_agua_dados_brutos_intro())

grafico_agua_dados_brutos(df_panorama_agua, ano_censo=2024)