import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re



from scripts.utils import(carregar_dados,
                          COLUNAS_RENOMEADAS_CENSO
)

from scripts.textos import(texto_pan_agua_intro,
                           texto_pan_agua_metodologia,
                           texto_pan_agua_dados_brutos_intro,
                           texto_pan_agua_dados_brutos_analise_01,
                           texto_pan_agua_dados_brutos_analise_02,
                           texto_pan_agua_dados_brutos_fontes_intro,
                           texto_pan_agua_dados_brutos_fontes_analise,
                           texto_pan_agua_dados_brutos_problematizacao_intro,
                           texto_pan_agua_dados_brutos_problematizacao_premissas,
                           texto_pan_agua_fontes_intro_01,
                           texto_pan_agua_fontes_intro_02,
                           texto_pan_agua_fontes_analise,
                           texto_pan_agua_pdde_intro,
                           texto_pan_agua_pdde_agua_intro,
                           texto_pan_agua_pdde_agua_requisitos_censo,
                           texto_pan_agua_pdde_agua_requisitos_uex,
                           texto_pan_agua_pdde_agua_requisitos_uex_analise,
                           texto_pan_agua_pdde_agua_requisitos_uex_anexos,
                           texto_pan_agua_pdde_agua_requisitos_adesao
)

from scripts.graficos import (grafico_agua_total_dados_brutos,
                              grafico_escolas_sem_agua_por_municipio,
                              grafico_alunos_por_disponibilidade_agua,
                              grafico_localizacao_escolas_sem_agua,
                              grafico_abastecimento_agua_por_fonte,
                              grafico_agua_total_fontes,
                              grafico_agua_total_fontes_municipios,
                              grafico_escolas_uex_por_ano
)

# Configuração visual
plt.style.use('dark_background')
COR_TEXTO = '#FFA07A'
CORES_BARRAS = ['#B0E0E6', '#FFC107']

# Corregar dados
url_df_panorama_agua = 'https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_panorama_agua.csv'
df_panorama_agua = carregar_dados(url_df_panorama_agua)

url_df_uex = 'https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/pdde_info/df_uex.csv'
df_uex = carregar_dados(url_df_uex)

st.set_page_config(page_title="Panorama Água Potável", layout="wide", page_icon="🦜")

# Título da página
st.title('💧 Panorama da Oferta de Água Potável')
st.write(texto_pan_agua_intro()) 

#++++++++
# Subseção Metodologia
st.header('Metodologia')
st.write(texto_pan_agua_metodologia())

#++++++++
# Subseção dados brutos do Censo Escolar
st.header('Oferta de água potável segundo os dados brutos do Censo Escolar')
st.write(texto_pan_agua_dados_brutos_intro())

# Selectbox do ano do Censo Escolar
anos_disponiveis = sorted(df_panorama_agua['NU_ANO_CENSO'].unique())
ano_mais_recente = max(anos_disponiveis)

ano_censo = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente),
    key="agua_dados_brutos"
)

# Divide a tela em duas colunas e plota os gráficos
col1, col2 = st.columns(2)

with col1:
    grafico_agua_total_dados_brutos(df_panorama_agua, ano_censo=ano_censo)
    
with col2:
    grafico_escolas_sem_agua_por_municipio(df_panorama_agua, ano_censo=ano_censo)

st.write(texto_pan_agua_dados_brutos_analise_01())

# Selectbox do ano do Censo Escolar
anos_disponiveis = sorted(df_panorama_agua['NU_ANO_CENSO'].unique())
ano_mais_recente = max(anos_disponiveis)

ano_censo = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente),
    key="agua_dados_brutos_localizacao"
)

# Divide a tela em duas colunas e plota os gráficos
col1, col2 = st.columns(2)

with col1:
    grafico_localizacao_escolas_sem_agua(df_panorama_agua, ano_censo=ano_censo)
    
with col2:
    grafico_alunos_por_disponibilidade_agua(df_panorama_agua, ano_censo=ano_censo)
    
st.write(texto_pan_agua_dados_brutos_analise_02())

# Análise dos dados segundo as fontes de abastecimento de água
st.header('Oferta de água segundo as fontes de abastecimento')
st.write(texto_pan_agua_dados_brutos_fontes_intro())

col1, col2 = st.columns(2)

with col1:
    # Selectbox do ano do Censo Escolar
    anos_disponiveis = sorted(df_panorama_agua['NU_ANO_CENSO'].unique())
    ano_mais_recente = max(anos_disponiveis)

    ano_censo = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="agua_dados_brutos_fontes_abastecimento"
    )

    grafico_abastecimento_agua_por_fonte(df_panorama_agua, ano_censo=ano_censo)

st.write(texto_pan_agua_dados_brutos_fontes_analise())



#++++++++
# Subseção Problematização dos dados brutos do Censo Escolar
st.header('Problematização dos dados brutos do Censo Escolar')
st.write(texto_pan_agua_dados_brutos_problematizacao_intro())

st.subheader('Premissas para o confronto dos dados brutos')
st.write(texto_pan_agua_dados_brutos_problematizacao_premissas())

st.subheader('Análise dos dados segundo as fontes de abastecimento de água')
st.write(texto_pan_agua_fontes_intro_01())

# Consulta das escolas que declaram fornecer água potável de fontes insalubres
ano_censo = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente),
    key="agua_dados_brutos_problematizacao"
)

# Filtro para urbanas e rurais
filtro_fontes_improprias = (
    (df_panorama_agua["NU_ANO_CENSO"] == ano_censo) &
#   (df_panorama_agua["TP_LOCALIZACAO"] == 2) &  # Zona rural
    (df_panorama_agua["IN_AGUA_POTAVEL"] == 1) & (
        (df_panorama_agua["IN_AGUA_CACIMBA"] == 1) |
        (df_panorama_agua["IN_AGUA_FONTE_RIO"] == 1) |
        (df_panorama_agua["IN_AGUA_INEXISTENTE"] == 1) |
        (df_panorama_agua["IN_AGUA_CARRO_PIPA"] == 1)
    )
)
# Quantidade total
total_respostas_incoerentes_improprias = df_panorama_agua[filtro_fontes_improprias].shape[0]

filtro_fontes_proprias = (
    (df_panorama_agua["NU_ANO_CENSO"] == ano_censo) &
#   (df_panorama_agua["TP_LOCALIZACAO"] == 2) &  # Zona rural
    (df_panorama_agua["IN_AGUA_POTAVEL"] == 0) & (
        (df_panorama_agua["IN_AGUA_REDE_PUBLICA"] == 1) |
        (df_panorama_agua["IN_AGUA_POCO_ARTESIANO"] == 1)        
    )
)

total_respostas_incoerentes_proprias = df_panorama_agua[filtro_fontes_proprias].shape[0]

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    ##### Total de escolas que afirmam fornecer água potável de fontes impróprias:
    # `{total_respostas_incoerentes_improprias}`
    """)

with col2:
    st.markdown(f"""
    ##### Total de escolas que afirmam não fornecer água potável de fontes potencialmente potáveis:
    # `{total_respostas_incoerentes_proprias}`
    """)

st.write(texto_pan_agua_fontes_intro_02())

# Divide a tela em duas colunas e plota os gráficos
col1, col2 = st.columns(2)

with col1:
    # Selectbox do ano do Censo Escolar
    anos_disponiveis = sorted(df_panorama_agua['NU_ANO_CENSO'].unique())
    ano_mais_recente = max(anos_disponiveis)

    ano_censo = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="agua_total_fontes"
    )
    
    grafico_agua_total_fontes(df_panorama_agua, ano_censo=ano_censo)
    
with col2:
    # Selectbox do município
    municipios_disponiveis = sorted(df_panorama_agua['NO_MUNICIPIO'].unique())
    
    municipio = st.selectbox(
        "Selecione o município:",
        options=municipios_disponiveis,
        key="agua_total_municipios"
    )
    
    grafico_agua_total_fontes_municipios(df_panorama_agua, municipio=municipio)

st.write(texto_pan_agua_fontes_analise())


#++++++++
# Subseção PDDE Água
st.header('Programa Dinheiro Direto na Escola - PDDE')
st.write(texto_pan_agua_pdde_intro())

st.header('PDDE Água, Esgotamento Sanitário e Infraestrutura')
st.write(texto_pan_agua_pdde_agua_intro())

st.subheader("Preenchimento correto do Censo Escolar")
st.write(texto_pan_agua_pdde_agua_requisitos_censo())

st.subheader("Unidade Executora própria vs. Entidades Executoras")
st.write(texto_pan_agua_pdde_agua_requisitos_uex())

col1, col2 = st.columns(2)
with col1:
    # Selectbox do ano
    anos_disponiveis = sorted(df_uex['Ano'].unique())
    ano_mais_recente = max(anos_disponiveis)

    ano_uex = st.selectbox(
        "Selecione o ano:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="agua_uex_ano"
    )

    grafico_escolas_uex_por_ano(df_panorama_agua, df_uex, ano=ano_uex)

st.write(texto_pan_agua_pdde_agua_requisitos_uex_analise())

st.subheader("Escolas Anexas")
st.write(texto_pan_agua_pdde_agua_requisitos_uex_anexos())

st.subheader("Efetiva adesão ao Programa")
st.write(texto_pan_agua_pdde_agua_requisitos_adesao())