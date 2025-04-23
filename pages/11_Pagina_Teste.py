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

st.title("🦜 Observatório Curica")
st.subheader("E̴͘͡s̷͘t̸̕͞a͡ ͢v̶̸͘e͠͏n̛͘͏d̶̡o͜?")
#st.subheader("E͢͠͡s̷͞͞t̸̢̡a͢͡ ̡v̷́͞e̷̸̢n̛͝͞d̵̡͠ǫ̢͡?")
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

