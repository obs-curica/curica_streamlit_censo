import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

# Configuração visual
plt.style.use('dark_background')
COR_TEXTO = '#FFA07A'
CORES_BARRAS = ['#B0E0E6', '#FFC107']

st.set_page_config(page_title="Panorama Água Potável", layout="wide")
st.title('💧 Panorama da Oferta de Água Potável nas Escolas Públicas')

# Identificar arquivos de censo disponíveis
arquivos_censo = sorted([f for f in os.listdir("data") if re.match(r'censo_ac_\d{4}\.csv', f)])
anos_disponiveis = [int(re.search(r'\d{4}', arq).group()) for arq in arquivos_censo]

# Sidebar: seleção do ano
ano_selecionado = st.sidebar.selectbox("Selecione o ano do Censo Escolar", sorted(anos_disponiveis, reverse=True))
arquivo_censo = f"data/censo_ac_{ano_selecionado}.csv"

# Carregamento dos dados
@st.cache_data
def carregar_dados_censo(arquivo):
    return pd.read_csv(arquivo, delimiter=';', encoding='utf-8', low_memory=False)

df = carregar_dados_censo(arquivo_censo)

# Filtro: apenas escolas públicas ativas
df = df[df['TP_DEPENDENCIA'] != 4]
df = df[df['TP_SITUACAO_FUNCIONAMENTO'] == 1]

# Seleciona variáveis relevantes
colunas_agua = [
    'SG_UF', 'NO_MUNICIPIO', 'CO_MUNICIPIO', 'NO_ENTIDADE', 'CO_ENTIDADE',
    'TP_DEPENDENCIA', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA',
    'TP_OCUPACAO_PREDIO_ESCOLAR', 'IN_PREDIO_COMPARTILHADO',
    'IN_AGUA_POTAVEL', 'IN_AGUA_REDE_PUBLICA', 'IN_AGUA_POCO_ARTESIANO',
    'IN_AGUA_CACIMBA', 'IN_AGUA_FONTE_RIO', 'IN_AGUA_INEXISTENTE',
    'IN_ENERGIA_REDE_PUBLICA', 'IN_ENERGIA_GERADOR_FOSSIL',
    'IN_ENERGIA_RENOVAVEL', 'IN_ENERGIA_INEXISTENTE', 'QT_MAT_BAS'
]

df_agua = df[colunas_agua].copy()

# Gráfico 1: Escolarização por Localização
def plot_localizacao(df):
    localizacao = df['TP_LOCALIZACAO'].value_counts().sort_index()
    localizacao.index = ['Urbana', 'Rural']
    total = localizacao.sum()
    percentuais = (localizacao / total) * 100

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(localizacao.index, localizacao.values, color=['#696969', '#76EE00'])
    ax.set_title('Escolas Públicas por Localização', color=COR_TEXTO)
    ax.set_ylabel('Número de Escolas', color=COR_TEXTO)
    ax.set_xticks(range(len(localizacao)))
    ax.set_xticklabels(localizacao.index, color=COR_TEXTO)
    ax.set_yticks(ax.get_yticks())
    ax.set_yticklabels([int(y) for y in ax.get_yticks()], color=COR_TEXTO)

    for i, v in enumerate(localizacao):
        ax.text(i, v + 5, f'{percentuais[i]:.1f}%', ha='center', color=COR_TEXTO, fontweight='bold')

    for spine in ax.spines.values():
        spine.set_color(COR_TEXTO)

    st.pyplot(fig)

# Gráfico 2: Condição de Fornecimento de Água Potável
def plot_condicao_agua(df):
    contagem = df['IN_AGUA_POTAVEL'].value_counts().sort_index(ascending=False)
    contagem.index = ['Fornece', 'Não Fornece']
    total = contagem.sum()
    percentuais = (contagem / total) * 100

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(contagem.index, contagem.values, color=CORES_BARRAS)
    ax.set_title('Fornecimento de Água Potável', color=COR_TEXTO)
    ax.set_ylabel('Número de Escolas', color=COR_TEXTO)
    ax.set_xticks(range(len(contagem)))
    ax.set_xticklabels(contagem.index, color=COR_TEXTO)
    ax.set_yticks(ax.get_yticks())
    ax.set_yticklabels([int(y) for y in ax.get_yticks()], color=COR_TEXTO)

    for i, v in enumerate(contagem):
        ax.text(i, v + 5, f'{percentuais[i]:.1f}%', ha='center', color='white', fontweight='bold')

    for spine in ax.spines.values():
        spine.set_color(COR_TEXTO)

    st.pyplot(fig)

# Gráfico 3: Escolas sem Água Potável por Município
def plot_municipios_sem_agua(df):
    df_sem_agua = df[df['IN_AGUA_POTAVEL'] == 0]
    municipios = df_sem_agua.groupby('NO_MUNICIPIO').size().sort_values()

    cmap = mcolors.LinearSegmentedColormap.from_list('custom_gradient', CORES_BARRAS)
    norm = plt.Normalize(vmin=municipios.min(), vmax=municipios.max())
    cores = [cmap(norm(v)) for v in municipios]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(municipios.index, municipios.values, color=cores)
    ax.set_title('Escolas Sem Água Potável por Município', color=COR_TEXTO)
    ax.set_xlabel('Número de Escolas', color=COR_TEXTO)
    ax.tick_params(axis='x', colors=COR_TEXTO)
    ax.tick_params(axis='y', colors=COR_TEXTO)

    for spine in ax.spines.values():
        spine.set_color(COR_TEXTO)

    for i, v in enumerate(municipios):
        ax.text(v + 0.5, i, str(v), va='center', color='white', fontweight='bold')

    st.pyplot(fig)

# Exibição dos gráficos
st.subheader('Distribuição por Localização')
plot_localizacao(df_agua)

st.subheader('Censo Escolar - Situação de Água Potável')
plot_condicao_agua(df_agua)

st.subheader('Distribuição Geográfica das Escolas sem Água Potável')
plot_municipios_sem_agua(df_agua)
