# app.py

import streamlit as st
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

# st.title("🦜 Observatório Curica")
#st.markdown(
#    """
#    Bem-vindo ao Observatório Curica, uma iniciativa do grupo de pesquisa PoÉticas nas Amazônias,  
#    Grupo de Pesquisa Interdisciplinar em Linguagem e Educação, do Instituto Federal do Acre,  
#    em conjunto com a Promotoria Especializada de Defesa da Criança e do Adolescente de Cruzeiro do Sul-Acre.  
#      
#    O Observatório Curica é uma plataforma de visualização de dados para diagnóstico, monitoramento e intervenção  
#    nas políticas públicas educacionais do Estado do Acre e seus Municípios.       
#      
#    Utilize o menu lateral para navegar entre os panoramas e metas do Plano Nacional de Educação.
#    """,
#    unsafe_allow_html=True
#)

st.code(
""".   
   __
  / _ \  | |__    ___    ___   _ __  __   __   __ _  | |_    ___    _ __  (_)   ___  
 | | | | | '_ \  / __|  / _ \ | '__| \ \ / /  / _` | | __|  / _ \  | '__| | |  / _ \ 
 | |_| | | |_) | \__ \ |  __/ | |     \ V /  | (_| | | |_  | (_) | | |    | | | (_) |
  \___/__|_.__/  |___/  \___|_|_|      \_/    \__,_|  \__|  \___/  |_|    |_|  \___/ 
      / ___|  _   _   _ __  (_)   ___    __ _                                        
     | |     | | | | | '__| | |  / __|  / _` |                                       
     | |___  | |_| | | |    | | | (__  | (_| |                                       
      \____|  \__,_| |_|    |_|  \___|  \__,_|                                       
                                                                                     
"""
)

st.markdown(texto_app())




#st.code(
#    """.
# ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
#▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
#▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
#▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌  ▐░▌         ▐░▌  ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌
#▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌   ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌
#▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌
#▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀      ▐░▌   ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀      ▐░▌     ▐░▌       ▐░▌
#▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌▐░▌          ▐░▌     ▐░▌        ▐░▌ ▐░▌      ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌
#▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌        ▐░▐░▌       ▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
#▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌        ▐░▌        ▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
# ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀          ▀          ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
#                                                                                                                                                                  
# ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄                                                                                     
#▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌                                                                                    
#▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌                                                                                    
#▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌                                                                                    
#▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌                                                                                    
#▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌                                                                                    
#▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀      ▐░▌     ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌                                                                                    
#▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌                                                                                    
#▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌                                                                                    
#▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌                                                                                    
# ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀                                                                             
#""",
#    language="markdown"
#)

#st.subheader("E̴͘͡s̷͘t̸̕͞a͡ ͢v̶̸͘e͠͏n̛͘͏d̶̡o͜?")
#st.subheader("E̛s͠t̸a͘ ͜v̵̨e̡͞n̛͡d̢ó͘?")
st.subheader("E͢͠͡s̷͞͞t̸̢̡a͢͡ ̡v̷́͞e̷̸̢n̛͝͞d̵̡͠ǫ̢͡?")


st.sidebar.markdown("### 📌 Navegação")
st.sidebar.info("Escolha uma seção no menu lateral para começar sua análise.")
