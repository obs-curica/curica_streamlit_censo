import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

from scripts.textos import texto_pan_rede_intro
from scripts.textos import texto_pan_rede_caracterizacao
from scripts.textos import texto_pan_rede_totais
from scripts.textos import texto_pan_rede_analise
from scripts.textos import texto_pan_rede_dependencia_intro
from scripts.textos import texto_pan_rede_dependencia_analise
from scripts.textos import texto_pan_rede_dependencia_analise_2
from scripts.textos import texto_pan_rede_rural_intro

from scripts.load_data import carregar_dados
from scripts.load_data import dataframe_totais_por_localizacao_municipio

from scripts.graficos import grafico_alunos_por_municipio
from scripts.graficos import grafico_escolas_por_municipio
from scripts.graficos import grafico_escolas_por_dependencia
from scripts.graficos import grafico_alunos_por_dependencia
from scripts.graficos import grafico_alunos_por_dependencia_municipio
from scripts.graficos import grafico_escolas_por_dependencia_municipio
from scripts.graficos import grafico_alunos_por_localizacao
from scripts.graficos import grafico_escolas_por_localizacao
from scripts.graficos import grafico_escolas_por_localizacao_municipio

# Configuração da página
st.set_page_config(page_title="Panorama Rede de Ensino", layout="wide", page_icon="🦜")

# Carregar os dados
url_panorama = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_geral/df_panorama_geral.csv"
df_panorama_geral = carregar_dados(url_panorama)

# Título da página
st.title("🏫 Panorama da Rede Pública de Ensino do Estado do Acre")
st.write(texto_pan_rede_intro())


#============================
# Seção 01 - Caracterização da Rede de Ensino
#============================
st.header("Caracterização da Rede de Ensino")
st.write(texto_pan_rede_caracterizacao())

#++++++++++++
# Subseção 01.1 - Total de Alunos e Escolas por Município
st.subheader("Total de Alunos e Escolas por Município")
st.write(texto_pan_rede_totais())

# Selectbox do ano do Censo Escolar
# ano_censo = st.selectbox("Selecione o ano do Censo Escolar:", sorted(df_panorama_geral['NU_ANO_CENSO'].unique()), key="ano_censo")
anos_disponiveis = sorted(df_panorama_geral['NU_ANO_CENSO'].unique())
ano_mais_recente = max(anos_disponiveis)

ano_censo = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente)
)

# Divide a tela em duas colunas e plota os gráficos
col1, col2 = st.columns(2)

with col1:
    grafico_alunos_por_municipio(df_panorama_geral, ano_censo)

with col2:
    grafico_escolas_por_municipio(df_panorama_geral, ano_censo)

# Texto de análise dos gráficos
st.write(texto_pan_rede_analise())

#++++++++++++++
# Subseção 01.2 - Total de Alunos e Escolas por Dependência Administrativa
st.subheader("Total de Alunos e Escolas por Dependência Administrativa")
st.write(texto_pan_rede_dependencia_intro())

st.write("Ano Selecionado: ", ano_censo)

#st.write(":green-badge[Ano Selecionado: ]", ano_censo)

# Divide a tela em duas colunas e plota os seus gráficos
col1, col2 = st.columns(2)
# Gráfico do total de alunos por dependência
with col1:
    grafico_alunos_por_dependencia(df_panorama_geral, ano_censo)
# Gráfico do total de escolas por dependência
with col2:
    grafico_escolas_por_dependencia(df_panorama_geral, ano_censo)

# Texto análise dos gráficos
st.write(texto_pan_rede_dependencia_analise())

# Tabela de dependência administrativa por Município
with st.form("form_dependencia"):
    ano_censo_dependencia = st.selectbox(
        "Selecione o ano do Censo Escolar:", 
        options=anos_disponiveis, 
        index=anos_disponiveis.index(ano_mais_recente), 
        key ="ano_censo_dependencia"
    )
    municipio_dependencia = st.selectbox("Selecione o município:", sorted(df_panorama_geral['NO_MUNICIPIO'].unique()), key="municipio_dependencia")
    submitted = st.form_submit_button("Gerar Dados")
    if submitted:
        col1, col2 = st.columns(2)
        # Dataframe do total de alunos e escolas por dependência
        with col1:
            grafico_alunos_por_dependencia_municipio(df_panorama_geral, ano_censo_dependencia, municipio_dependencia)
        # Gráfico do total de escolas por dependência
        with col2:
            grafico_escolas_por_dependencia_municipio(df_panorama_geral, ano_censo_dependencia, municipio_dependencia)

        # Texto de análise dos gráficos
        st.write(texto_pan_rede_dependencia_analise_2())

#===============================
# Seção 02 - Urbano vs. Rural
#===============================
st.header("Urbano vs. Rural")

# Texto de introdução
st.write(texto_pan_rede_rural_intro())

# Selectbox do ano do Censo Escolar
ano_censo_rural = st.selectbox(
    "Selecione o ano do Censo Escolar:", 
    options=anos_disponiveis, 
    index=anos_disponiveis.index(ano_mais_recente), 
    key ="ano_censo_rural"
)

# Divide a tela em duas colunas
col1, col2 = st.columns(2)
# Gráfico do total de alunos por localização
with col1:
    grafico_alunos_por_localizacao(df_panorama_geral, ano_censo_rural)
# Gráfico do total de escolas por localização
with col2:
    grafico_escolas_por_localizacao(df_panorama_geral, ano_censo_rural)
# Texto de análise dos gráficos
st.write("Texto analítico.")

# Tabela de localização por Município
with st.form("form_localizacao"):
    ano_censo_localizacao = st.selectbox("Selecione o ano do Censo Escolar:", sorted(df_panorama_geral['NU_ANO_CENSO'].unique()), key ="ano_censo_localizacao")
    municipio_localizacao = st.selectbox("Selecione o município:", sorted(df_panorama_geral['NO_MUNICIPIO'].unique()), key="municipio_localizacao")
    # localizacao = st.selectbox("Selecione a localização:", sorted(df_panorama_geral['TP_LOCALIZACAO'].unique()), key="localizacao")
    submitted = st.form_submit_button("Gerar Dados")
    if submitted:
        col1, col2 = st.columns(2)
        # Dataframe do total de alunos e escolas por localização
        with col1:
            st.write(dataframe_totais_por_localizacao_municipio(df_panorama_geral, ano_censo_localizacao, municipio_localizacao))
        # Gráfico do total de escolas por localização    
        with col2:
            grafico_escolas_por_localizacao_municipio(df_panorama_geral, ano_censo_localizacao, municipio_localizacao)
    
        # Texto de análise dos gráficos
        st.write("E então, como está a distribuição das escolas pelo território do seu Município?")
        st.write("Discorrer sobre logisticaa, transporte, acesso, etc.")
        st.write("Há recusos disponíveis para atender a demanda das escolas de dificil acesso?")



#===============================
# Seção 03 - Geração de Relatórios
#===============================
st.header("Geração de relatórios")
st.write("Seegue abaixo ferramente para geração de relatórios para download. Basta selecionar os filtros desejados e clicar no botão de download.")