import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

from scripts.load_data import carregar_dados

from scripts.textos import texto_pan_financiamento_intro
from scripts.textos import texto_pan_financiamento_intro_mde
from scripts.textos import texto_pan_financiamento_analise_mde
from scripts.textos import texto_pan_financiamento_intro_se
from scripts.textos import texto_pan_financiamento_analise_se
from scripts.textos import texto_pan_financiamento_fundeb_intro
from scripts.textos import texto_pan_financiamento_fundeb_analise
from scripts.textos import texto_pan_financiamento_fnde_intro
from scripts.textos import texto_pan_financiamento_fnde_programas

from scripts.graficos import grafico_fundeb_total_ano
from scripts.graficos import grafico_fundeb_total_ente
from scripts.graficos import grafico_indicador_despesa_profissionais
from scripts.graficos import grafico_percentual_recursos_nao_utilizados


# Configuração da página
st.set_page_config(page_title="Panorama Financiamento", layout="wide", page_icon="🦜")

# Carregar dados
url = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_financiamento/df_panorama_financiamento.csv"
df_panorama_financiamento = carregar_dados(url)
df_panorama_financiamento['nome'] = df_panorama_financiamento['nome'].astype(str)



st.title("💲 Considerações Gerais sobre o Financiamento da Educação Básica")

# texto introdutório financiamento
st.write(texto_pan_financiamento_intro())

#++++++++
# Subseção Fundeb
st.header("O Fundeb")
st.write(texto_pan_financiamento_fundeb_intro())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Fundeb Total por Ano")
    anos_disponiveis = sorted(df_panorama_financiamento['ano'].unique())
    ano_mais_recente = max(anos_disponiveis)

    ano = st.selectbox(
        "Selecione o ano:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="fundeb_ano"
    )

    # Gráfico do Fundeb total por ano
    grafico_fundeb_total_ano(df_panorama_financiamento, ano)
    
with col2:
    st.subheader("Fundeb Total por Ente")
    
    entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    
    entes = st.selectbox(
        "Selecione o ente:",
        options=entes_disponiveis,
        key="fundeb_ente"
    )
    
    grafico_fundeb_total_ente(df_panorama_financiamento, entes)
        
# Gráficos do Fundeb vaat e total
# funcao aqui

st.write(texto_pan_financiamento_fundeb_analise())

# Gráficos do Fundeb Estado e Municpios sob demanda
# funcao aqui

entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    
entes = st.selectbox(
    "Selecione o ente:",
    options=entes_disponiveis,
    key="fundeb_despesa_profissionais"
)

col1, col2 = st.columns(2)

with col1:
    grafico_indicador_despesa_profissionais(df_panorama_financiamento, entes)
    
with col2:
    grafico_percentual_recursos_nao_utilizados(df_panorama_financiamento, entes)

#+++++++++
# Subseção MDE
st.header("Manutenção e Desenvolvimento do Ensino - MDE")


#++++++++
# Subseção Salário Educação
st.header("Salário Educação")





#++++++++
# Subseção Programas do FNDE
st.subheader("Deficiências na execução dos recursos disponibilizados pelo FNDE")
st.write("conluir o financimento apresentando os programas e a não utilização de recursos. Aí fazer a chamada para os outros panoramas.")