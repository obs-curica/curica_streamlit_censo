import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados_agua():
    """Carrega os dados de água potável de várias fontes CSV e combina em um único DataFrame."""
    
    # URLs do arquivo CSV no GitHub
    url_agua = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua.csv"
    
    # Carregar os dados diretamente dos links do GitHub
    df_censo_ac_agua = pd.read_csv(url_agua, delimiter=';', encoding='utf-8', low_memory=False)
    
    return df_censo_ac_agua

