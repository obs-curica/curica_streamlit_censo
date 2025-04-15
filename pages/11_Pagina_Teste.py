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

st.set_page_config(page_title="Panorama Água Potável", layout="wide", page_icon="🦜")
st.title('💧 Panorama da Oferta de Água Potável')

# URLs dos arquivos CSV no GitHub
url_agua_2019 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2019.csv"
url_agua_2020 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2020.csv"
url_agua_2021 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2021.csv"
url_agua_2022 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2022.csv"
url_agua_2023 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2023.csv"
url_agua_2024 = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua_2024.csv"

# Carregar os dados diretamente dos links do GitHub
df_censo_ac_agua_2019 = pd.read_csv(url_agua_2019, delimiter=';', encoding='utf-8', low_memory=False)
df_censo_ac_agua_2020 = pd.read_csv(url_agua_2020, delimiter=';', encoding='utf-8', low_memory=False)
df_censo_ac_agua_2021 = pd.read_csv(url_agua_2021, delimiter=';', encoding='utf-8', low_memory=False)
df_censo_ac_agua_2022 = pd.read_csv(url_agua_2022, delimiter=';', encoding='utf-8', low_memory=False)
df_censo_ac_agua_2023 = pd.read_csv(url_agua_2023, delimiter=';', encoding='utf-8', low_memory=False)
df_censo_ac_agua_2024 = pd.read_csv(url_agua_2024, delimiter=';', encoding='utf-8', low_memory=False)

# Combina todos os dataframes em um único dataframe
df_combined = pd.concat([
    df_censo_ac_agua_2019,
    df_censo_ac_agua_2020,
    df_censo_ac_agua_2021,
    df_censo_ac_agua_2022,
    df_censo_ac_agua_2023,
    df_censo_ac_agua_2024
])

# Exibe as primeiras linhas para verificação
# st.write("Exibindo as primeiras linhas dos dados combinados:")
# st.write(df_combined.head())

# Filtros de Seleção
# Seleção do ano do Censo Escolar
ano_censo = st.selectbox("Selecione o ano do Censo Escolar:", options=df_combined['NU_ANO_CENSO'].unique())

# Seleção de Localização (Urbana/Rural)
localizacao = st.selectbox("Selecione a Localização (Urbana ou Rural):", options=["Urbana", "Rural"])

# Filtro de Fornecimento de Água
agua_potavel = st.selectbox("Selecione a condição de fornecimento de Água Potável:", options=["Sim", "Não"])

# Filtro de Município
municipio_selecionado = st.selectbox("Selecione o Município:", options=df_combined['NO_MUNICIPIO'].unique())

# Filtrando os dados com base nas seleções
df_filtered = df_combined.copy()

# Mapeando valores para filtros
localizacao_map = {"Urbana": 1, "Rural": 2}
agua_map = {"Sim": 1, "Não": 0}

df_filtered = df_filtered[df_filtered['NU_ANO_CENSO'] == ano_censo]
df_filtered = df_filtered[df_filtered['TP_LOCALIZACAO'] == localizacao_map[localizacao]]
df_filtered = df_filtered[df_filtered['IN_AGUA_POTAVEL'] == agua_map[agua_potavel]]
df_filtered = df_filtered[df_filtered['NO_MUNICIPIO'] == municipio_selecionado]

# Exibe o DataFrame filtrado
st.write(f"Exibindo dados filtrados para {municipio_selecionado} - {localizacao} - {agua_potavel}:")
st.write(df_filtered[['NU_ANO_CENSO', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'CO_ENTIDADE', 'TP_LOCALIZACAO', 'QT_MAT_BAS', 'IN_AGUA_POTAVEL']])

# Filtrar o DataFrame apenas pelo ano e município (não por água potável aqui!)
df_grafico = df_combined[
    (df_combined['NU_ANO_CENSO'] == ano_censo) & 
    (df_combined['NO_MUNICIPIO'] == municipio_selecionado)
]

# Realizar a contagem de escolas por categoria de água potável
agua_counts = df_grafico['IN_AGUA_POTAVEL'].value_counts().sort_index()

# Garantindo sempre duas categorias no gráfico
agua_counts.index = agua_counts.index.map({0: 'Não Fornece', 1: 'Fornece'})

# TESTE ALTAIR
import altair as alt

# Cria o DataFrame formatado
df_altair = pd.DataFrame({
    'Situação': agua_counts.index,
    'Quantidade': agua_counts.values
})

# Define cores customizadas para as categorias
cores_personalizadas = {
    'Não Fornece': '#FFC107',
    'Fornece': '#B0E0E6'
}

# Gera o gráfico com Altair
chart = alt.Chart(df_altair).mark_bar().encode(
    x=alt.X('Situação:N', axis=alt.Axis(labelAngle=0, labelColor='#FFA07A', titleColor='#FFA07A', title='')),
    y=alt.Y('Quantidade:Q', title='Número de Escolas', axis=alt.Axis(labelColor='#FFA07A', titleColor='#FFA07A')),
    color=alt.Color('Situação:N', scale=alt.Scale(domain=list(cores_personalizadas.keys()),
                                                  range=list(cores_personalizadas.values())),
                    legend=None),
    tooltip=['Situação', 'Quantidade']
).properties(
    title=f"Fornecimento de Água Potável em {municipio_selecionado} ({ano_censo})",
    width=400,
    height=300
).configure_title(
    fontSize=14,
    anchor='start',
    color='#FFA07A'
).configure_view(
    stroke=None
).configure_axis(
    grid=False
).configure_view(
    stroke='#FFA07A',  # Cor da borda (moldura)
)

# Exibe no Streamlit
st.altair_chart(chart, use_container_width=False)