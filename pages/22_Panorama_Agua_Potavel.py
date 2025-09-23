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
                           texto_pan_agua_dados_brutos_intro,
                           texto_pan_agua_dados_brutos_analise_01,
                           texto_pan_agua_dados_brutos_analise_02,
                           texto_pan_agua_dados_brutos_problematizacao_intro,
                           texto_pan_agua_dados_brutos_problematizacao_premissas,
                           texto_pan_agua_fontes_intro
)

from scripts.graficos import (grafico_agua_total_dados_brutos,
                              grafico_escolas_sem_agua_por_municipio,
                              grafico_alunos_por_disponibilidade_agua,
                              grafico_localizacao_escolas_sem_agua
)

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

# Selectbox do ano do Censo Escolar
anos_disponiveis = sorted(df_panorama_agua['NU_ANO_CENSO'].unique())
ano_mais_recente = max(anos_disponiveis)

ano_censo = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente),
    key="agua_dados_brutos"
)

# Divide a tela em duas colunas e plota os gráficos
col1, col2 = st.columns(2)

with col1:
    grafico_agua_total_dados_brutos(df_panorama_agua, ano_censo=ano_censo)
    
with col2:
    grafico_escolas_sem_agua_por_municipio(df_panorama_agua, ano_censo=ano_censo)

st.write(texto_pan_agua_dados_brutos_analise_01())

# Selectbox do ano do Censo Escolar
anos_disponiveis = sorted(df_panorama_agua['NU_ANO_CENSO'].unique())
ano_mais_recente = max(anos_disponiveis)

ano_censo = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente),
    key="agua_dados_brutos_localizacao"
)

# Divide a tela em duas colunas e plota os gráficos
col1, col2 = st.columns(2)

with col1:
    grafico_localizacao_escolas_sem_agua(df_panorama_agua, ano_censo=ano_censo)
    
with col2:
    grafico_alunos_por_disponibilidade_agua(df_panorama_agua, ano_censo=ano_censo)
    
st.write(texto_pan_agua_dados_brutos_analise_02())

#++++++++
# Subseção Problematização dos dados brutos do Censo Escolar
st.header('Problematização dos dados brutos do Censo Escolar')
st.write(texto_pan_agua_dados_brutos_problematizacao_intro())

st.subheader('Premissas para o confronto dos dados brutos')
st.write(texto_pan_agua_dados_brutos_problematizacao_premissas())

st.subheader('Análise dos dados segundo as fontes de abastecimento de água')
st.write(texto_pan_agua_fontes_intro())


# lembrar de dizer que sao dois problemas essenciais: o erro no preenchimento do censo e do problema dos anexos