import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

from scripts.textos import texto_pan_financiamento_intro
from scripts.textos import texto_pan_financiamento_fundeb_intro
from scripts.textos import texto_pan_financiamento_fundeb_analise


st.set_page_config(page_title="Panorama Financiamento", layout="wide", page_icon="🦜")

st.title("💵 Considerações Gerais sobre o Financiamento da Educação Básica")

# Carrega dados FUNDEB
# url_fundeb_estado = ""
# url_fundeb_municipios = ""
# df_fundeb_estado = carregar_dados(url_fundeb_estado)
# df_fundeb_municipios = carregar_dados(url_fundeb_municipios)

# texto introdutório financiamento
st.write(texto_pan_financiamento_intro())

st.header("O Fundeb")
st.write(texto_pan_financiamento_fundeb_intro())

# Gráficos do Fundeb vaat e total
# funcao aqui

st.write(texto_pan_financiamento_fundeb_analise())

# Gráficos do Fundeb Estado e Municpios sob demanda
# funcao aqui

st.subheader("Deficiências na execução dos recursos disponibilizados pelo FNDE")
st.write("conluir o financimento apresentando os programas e a não utilização de recursos. Aí fazer a chamada para os outros panoramas.")