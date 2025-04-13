# app.py

import streamlit as st
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

# ======================
# CONFIGURAÇÃO DE INTERFACE
# ======================
st.set_page_config(
    page_title="Observatório Curica",
    page_icon="🦜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================
# LOGGING DIÁRIO
# ======================
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"curica_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()
logger.info("Aplicação Streamlit iniciada.")

# ======================
# SUPORTE A IMPORTAÇÃO DE SCRIPTS
# ======================
scripts_path = Path(__file__).resolve().parent / "scripts"
if str(scripts_path) not in sys.path:
    sys.path.append(str(scripts_path))

# ======================
# APRESENTAÇÃO
# ======================
st.markdown("""
    <style>
        .main {background-color: #0E1117;}
        h1 {color: #FFA07A;}
    </style>
""", unsafe_allow_html=True)

st.title("🦜 Observatório Curica")
st.markdown(
    """
    Bem-vindo ao Observatório Curica, uma iniciativa do grupo de pesquisa PoÉticas nas Amazônias,  
    Grupo de Pesquisa Interdisciplinar em Linguagem e Educação, do Instituto Federal do Acre,  
    em conjunto com a Promotoria Especializada de Defesa da Criança e do Adolescente de Cruzeiro do Sul-Acre.  
      
    O Observatório Curica é uma plataforma de visualização de dados para diagnóstico, monitoramento e intervenção  
    nas políticas públicas educacionais do Estado do Acre e seus Municípios.       
      
    Utilize o menu lateral para navegar entre os panoramas e metas do Plano Nacional de Educação.
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("### 📌 Navegação")
st.sidebar.info("Escolha uma seção no menu lateral para começar sua análise.")
