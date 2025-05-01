# app.py

import streamlit as st
import pandas as pd
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

from scripts.textos import texto_app

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
# CONFIGURAÇÃO GLOBAL DE EXIBIÇÃO DE NÚMEROS
# ======================
# Força o pandas a exibir floats sem notação científica
pd.set_option('display.float_format', '{:,.2f}'.format)

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

st.markdown(texto_app())

st.subheader("E̴͘͡s̷͘t̸̕͞a͡ ͢v̶̸͘e͠͏n̛͘͏d̶̡o͜?")
#st.subheader("E̛s͠t̸a͘ ͜v̵̨e̡͞n̛͡d̢ó͘?")
#st.subheader("E͢͠͡s̷͞͞t̸̢̡a͢͡ ̡v̷́͞e̷̸̢n̛͝͞d̵̡͠ǫ̢͡?")

st.sidebar.markdown("### 📌 Navegação")
st.sidebar.info("Escolha uma seção no menu lateral para iniciar sua análise.")
