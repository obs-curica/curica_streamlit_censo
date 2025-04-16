import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

from scripts.load_data import carregar_dados_agua

# Configuração visual
plt.style.use('dark_background')
COR_TEXTO = '#FFA07A'
CORES_BARRAS = ['#B0E0E6', '#FFC107']

st.set_page_config(page_title="Panorama Água Potável", layout="wide", page_icon="🦜")
st.title('💧 Panorama da Oferta de Água Potável')

st.subheader("Análise do Fornecimento de Água Potável nas Escolas Públicas do Acre")

st.write("Esta página apresenta uma análise do fornecimento de água potável nas escolas públicas do estado do Acre, com base nos dados do Censo Escolar. Você pode filtrar os dados por ano, localização (urbana ou rural), condição de fornecimento de água e município.") 

# Carregar os dados
df_censo_agua = carregar_dados_agua()

# Filtros de Seleção
# Seleção do ano do Censo Escolar
ano_censo = st.selectbox("Selecione o ano do Censo Escolar:", options=df_censo_agua['NU_ANO_CENSO'].unique())

# Seleção de Localização (Urbana/Rural)
localizacao = st.selectbox("Selecione a Localização (Urbana ou Rural):", options=["Urbana", "Rural"])

# Filtro de Fornecimento de Água
agua_potavel = st.selectbox("Selecione a condição de fornecimento de Água Potável:", options=["Sim", "Não"])

# Filtro de Município
municipio_selecionado = st.selectbox("Selecione o Município:", options=df_censo_agua['NO_MUNICIPIO'].unique())

# Filtrando os dados com base nas seleções
df_filtered = df_censo_agua.copy()

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
df_grafico = df_censo_agua[
    (df_censo_agua['NU_ANO_CENSO'] == ano_censo) & 
    (df_censo_agua['NO_MUNICIPIO'] == municipio_selecionado)
]

# Realizar a contagem de escolas por categoria de água potável
agua_counts = df_grafico['IN_AGUA_POTAVEL'].value_counts().sort_index()

# Garantindo sempre duas categorias no gráfico
agua_counts.index = agua_counts.index.map({0: 'Não Fornece', 1: 'Fornece'})

# Criando colunas na página do Streamlit para diminuir a largura do gráfico
# e melhorar a visualização
col1, col2 = st.columns(2)

with col1:

    # Plotagem correta do gráfico
    fig, ax = plt.subplots(figsize=(6, 5))

    # Barras com cores específicas para cada categoria
    cores_barras = [CORES_BARRAS[1] if categoria == 'Não Fornece' else CORES_BARRAS[0] for categoria in agua_counts.index]

    bars = ax.bar(agua_counts.index, agua_counts.values, color=cores_barras)

    # Define um espaço extra acima das barras
    ax.set_ylim(0, agua_counts.values.max() * 1.2)  # Aumenta o limite superior em 20%

    # Customização visual do gráfico
    ax.set_title(f"Fornecimento de Água Potável em {municipio_selecionado} ({ano_censo})", color=COR_TEXTO)
    ax.set_ylabel('Número de Escolas', color=COR_TEXTO)
    ax.set_xticklabels(agua_counts.index, color=COR_TEXTO)
    ax.tick_params(axis='y', colors=COR_TEXTO)

    for spine in ax.spines.values():
        spine.set_color(COR_TEXTO)

    # Adiciona valores acima das barras
    for i, v in enumerate(agua_counts):
        ax.text(i, v + 0.2, str(v), ha='center', color='white', fontweight='bold')

    # Exibe o gráfico no Streamlit
    plt.tight_layout()  # Ajusta automaticamente o layout para evitar sobreposição
    st.pyplot(fig)


st.write("     ")
st.write("     ")
st.write("     ")


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