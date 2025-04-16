import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados_agua():
    """Carrega os dados de água potável do link CSV."""
    
    # URLs do arquivo CSV no GitHub
    url_agua = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua.csv"
    
    # Carregar os dados diretamente dos links do GitHub
    df_censo_ac_agua = pd.read_csv(url_agua, delimiter=';', encoding='utf-8', low_memory=False)
    
    return df_censo_ac_agua


@st.cache_data
def carregar_dados_panorama_geral():
    """Carrega os dados do panorama geral do link CSV."""
    
    # URLs do arquivo CSV no GitHub
    url_panorama_geral = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_geral/df_panorama_geral.csv"
    
    # Carregar os dados diretamente dos links do GitHub
    df_panorama_geral = pd.read_csv(url_panorama_geral, delimiter=';', encoding='utf-8', low_memory=False)
    
    return df_panorama_geral

@st.cache_data
def carregar_dados(url):
    """Carrega dados de um arquivo CSV a partir de uma URL fornecida."""
        # Carregar os dados diretamente do link fornecido
    df = pd.read_csv(url, delimiter=';', encoding='utf-8', low_memory=False)
    
    return df
