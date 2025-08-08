import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

st.set_page_config(
    page_title="Observatório Curica",
    page_icon="🦜",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
            <iframe src="https://portaldatransparencia.gov.br/graficos/embed/visualizacaoGraficaTabela/barras/barras-verticais?titulo=Receita%20realizada%20(valor%20arrecadado)%20de%20receitas%20por%20Ano&funcionalidade=%2Freceitas%2Fconsulta&colunaOrdenacao=valorRealizado&colunasSelecionadas=ano%2CvalorRealizado&de=2025&ate=2025&orgaos=OR26298" width="100%" height="100%" frameborder="0" style="border:0" allowfullscreen></iframe>
            """, unsafe_allow_html=True)

st.markdown("""
            <a href="https://portaldatransparencia.gov.br/graficos/visualizacaoGraficaTabela/barras/barras-verticais?titulo=Receita%20realizada%20(valor%20arrecadado)%20de%20receitas%20por%20Ano&funcionalidade=%2Freceitas%2Fconsulta&colunaOrdenacao=valorRealizado&colunasSelecionadas=ano%2CvalorRealizado&de=2025&ate=2025&orgaos=OR26298" target="_blank">Receita realizada (valor arrecadado) de receitas por Ano</a>
            """, unsafe_allow_html=True)            