import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

from scripts.utils import carregar_dados

from scripts.textos import texto_pan_rede_intro
from scripts.textos import texto_pan_rede_caracterizacao
from scripts.textos import texto_pan_rede_totais
from scripts.textos import texto_pan_rede_analise
from scripts.textos import texto_pan_rede_dependencia_intro
from scripts.textos import texto_pan_rede_dependencia_analise
from scripts.textos import texto_pan_rede_dependencia_analise_2
from scripts.textos import texto_pan_rede_rural_intro_1
from scripts.textos import texto_pan_rede_rural_analise_1
from scripts.textos import texto_pan_rede_rural_intro_2
from scripts.textos import texto_pan_rede_rural_analise_2
from scripts.textos import texto_pan_rede_dependencia_rural_intro_1
from scripts.textos import texto_pan_rede_dependencia_rural_analise_1
from scripts.textos import texto_pan_rede_dependencia_rural_intro_2
from scripts.textos import texto_pan_rede_dependencia_rural_analise_2
from scripts.textos import text_pan_rede_dependencia_rural_conclusao
from scripts.textos import texto_pan_rede_relatorio_intro


from scripts.graficos import grafico_matriculas_por_municipio
from scripts.graficos import grafico_escolas_por_municipio
from scripts.graficos import grafico_escolas_por_dependencia
from scripts.graficos import grafico_matriculas_por_dependencia
from scripts.graficos import grafico_matriculas_por_dependencia_municipio
from scripts.graficos import grafico_escolas_por_dependencia_municipio
from scripts.graficos import grafico_matriculas_por_localizacao
from scripts.graficos import grafico_escolas_por_localizacao
from scripts.graficos import grafico_matriculas_por_localizacao_municipio
from scripts.graficos import grafico_escolas_por_localizacao_municipio
from scripts.graficos import grafico_escolas_por_dependencia_localizacao
from scripts.graficos import grafico_matriculas_por_dependencia_localizacao
from scripts.graficos import grafico_matriculas_por_dependencia_localizacao_municipio
from scripts.graficos import grafico_escolas_por_dependencia_localizacao_municipio

from scripts.relatorios import relatorio_rede_dados_escolas

# Configuração da página
st.set_page_config(page_title="Panorama Rede de Ensino", layout="wide", page_icon="🦜")

# Carregar os dados
url_panorama = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_geral/df_panorama_geral.csv"
df_panorama_geral = carregar_dados(url_panorama)

# Título da página
st.title("🏫 Panorama da Rede Pública de Ensino do Estado do Acre")
st.write(texto_pan_rede_intro())


#============================
# Seção 01 - Caracterização da Rede de Ensino
#============================
st.header("Caracterização da Rede de Ensino")
st.write(texto_pan_rede_caracterizacao())

#++++++++++++
# Subseção 01.1 - Total de matriculas e Escolas por Município
st.subheader("Total de matrículas e Escolas por Município")
st.write(texto_pan_rede_totais())

# Selectbox do ano do Censo Escolar
# ano_censo = st.selectbox("Selecione o ano do Censo Escolar:", sorted(df_panorama_geral['NU_ANO_CENSO'].unique()), key="ano_censo")
anos_disponiveis = sorted(df_panorama_geral['NU_ANO_CENSO'].unique())
ano_mais_recente = max(anos_disponiveis)

ano_censo = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente)
)

# Divide a tela em duas colunas e plota os gráficos
col1, col2 = st.columns(2)

with col1:
    grafico_matriculas_por_municipio(df_panorama_geral, ano_censo)

with col2:
    grafico_escolas_por_municipio(df_panorama_geral, ano_censo)

# Texto de análise dos gráficos
st.write(texto_pan_rede_analise())

#++++++++++++++
# Subseção 01.2 - Total de matriculas e Escolas por Dependência Administrativa
st.subheader("Total de matrículas e Escolas por Dependência Administrativa")
st.write(texto_pan_rede_dependencia_intro())

st.write("Ano Selecionado: ", ano_censo)

#st.write(":green-badge[Ano Selecionado: ]", ano_censo)

# Divide a tela em duas colunas e plota os seus gráficos
col1, col2 = st.columns(2)
# Gráfico do total de matriculas por dependência
with col1:
    grafico_matriculas_por_dependencia(df_panorama_geral, ano_censo)
# Gráfico do total de escolas por dependência
with col2:
    grafico_escolas_por_dependencia(df_panorama_geral, ano_censo)

# Texto análise dos gráficos
st.write(texto_pan_rede_dependencia_analise())

# Tabela de dependência administrativa por Município
with st.form("form_dependencia"):
    ano_censo_dependencia = st.selectbox(
        "Selecione o ano do Censo Escolar:", 
        options=anos_disponiveis, 
        index=anos_disponiveis.index(ano_mais_recente), 
        key ="ano_censo_dependencia"
    )
    municipio_dependencia = st.selectbox("Selecione o município:", sorted(df_panorama_geral['NO_MUNICIPIO'].unique()), key="municipio_dependencia")
    submitted = st.form_submit_button("Gerar Dados")
    if submitted:
        col1, col2 = st.columns(2)
        # Dataframe do total de matriculas e escolas por dependência
        with col1:
            grafico_matriculas_por_dependencia_municipio(df_panorama_geral, ano_censo_dependencia, municipio_dependencia)
        # Gráfico do total de escolas por dependência
        with col2:
            grafico_escolas_por_dependencia_municipio(df_panorama_geral, ano_censo_dependencia, municipio_dependencia)

        # Texto de análise dos gráficos
        st.write(texto_pan_rede_dependencia_analise_2())


#===============================
# Seção 02 - Urbano vs. Rural
#===============================
st.header("Urbano vs. Rural vs. Florestal")

# Texto de introdução
st.write(texto_pan_rede_rural_intro_1())

# Selectbox do ano do Censo Escolar
ano_censo_rural = st.selectbox(
    "Selecione o ano do Censo Escolar:", 
    options=anos_disponiveis, 
    index=anos_disponiveis.index(ano_mais_recente), 
    key ="ano_censo_rural"
)

# Divide a tela em duas colunas
col1, col2 = st.columns(2)
# Gráfico do total de matriculas por localização
with col1:
    grafico_matriculas_por_localizacao(df_panorama_geral, ano_censo_rural)
# Gráfico do total de escolas por localização
with col2:
    grafico_escolas_por_localizacao(df_panorama_geral, ano_censo_rural)
# Texto de análise dos gráficos
st.write(texto_pan_rede_rural_analise_1())


#++++++++++++++
# Subseção 02.2 - Total de matriculas e Escolas por Localização
st.subheader("Total de matrículas e Escolas por Localização, por Município")

# Texto introdutório xxxxxxxxxxxxxxxxxxxxxx
st.write(texto_pan_rede_rural_intro_2())

# Gráficos de localização por Município
with st.form("form_localizacao"):
    # Selectbox do ano do Censo Escolar, com valor padrão para o ano mais recente
    ano_censo_localizacao = st.selectbox(
        "Selecione o ano do Censo Escolar:", 
        options=anos_disponiveis, 
        index=anos_disponiveis.index(ano_mais_recente), 
        key ="ano_censo_localizacao")
    # Selectbox do município
    municipio_localizacao = st.selectbox(
        "Selecione o município:", 
        sorted(df_panorama_geral['NO_MUNICIPIO'].unique()), 
        key="municipio_localizacao"
    )
    # Botão de submissão
    submitted = st.form_submit_button("Gerar Dados")
    # Condicional para verificar se o botão foi pressionado
    # Se o botão foi pressionado, gera os gráficos
    if submitted:
        # divisão da tela em duas colunas
        col1, col2 = st.columns(2)
        # Grafico do total de matriculas por localização
        with col1:
            grafico_matriculas_por_localizacao_municipio(df_panorama_geral, ano_censo_localizacao, municipio_localizacao)
        
        # Gráfico do total de escolas por localização    
        with col2:
            grafico_escolas_por_localizacao_municipio(df_panorama_geral, ano_censo_localizacao, municipio_localizacao)
    
        # Texto de análise dos gráficos
        st.write(texto_pan_rede_rural_analise_2())
        
#++++++++++++++
# Subseção 02.3 - A vinculação de matriculas e escolas, por localização
st.header("Dependência Administrativa de matrículas e escolas, por Localização")

st.write(texto_pan_rede_dependencia_rural_intro_1())

# Selectbox do ano do Censo Escolar
ano_censo_dependencia_rural = st.selectbox(
    "Selecione o ano do Censo Escolar:", 
    options=anos_disponiveis, 
    index=anos_disponiveis.index(ano_mais_recente), 
    key ="ano_censo_dependencia_rural"
)

col1, col2 = st.columns(2)

# Gráfico do total de matriculas por dependência
with col1:
    grafico_matriculas_por_dependencia_localizacao(df_panorama_geral, ano_censo_dependencia_rural)
# Gráfico do total de escolas por dependência
with col2:
    grafico_escolas_por_dependencia_localizacao(df_panorama_geral, ano_censo_dependencia_rural)

# Texto de análise dos gráficos
st.write(texto_pan_rede_dependencia_rural_analise_1())

#++++++++++++++
# Subseção 02.4 - Total de matriculas e Escolas por Dependência Administrativa, por Localização, por Município
st.subheader("Total de matrículas e Escolas por Dependência Administrativa, por Localização, por Município")

# Texto introdutório
st.write(texto_pan_rede_dependencia_rural_intro_2())

# Gera gráficos de dependência, por localização, por Município
with st.form("form_dependencia_localizacao_municipio"):
    # Selectbox do ano do Censo Escolar
    ano_censo_dependencia_rural = st.selectbox(
        "Selecione o ano do Censo Escolar:", 
        options=anos_disponiveis, 
        index=anos_disponiveis.index(ano_mais_recente), 
        key ="ano_censo_dependencia_localizacao_municipio"
    )

    # Selectbox do Município
    municipio_dependencia_rural = st.selectbox(
        "Selecione o Município:", 
        sorted(df_panorama_geral['NO_MUNICIPIO'].unique()), 
        key="municipio_dependencia_localizacao_municipio"
    )

    # Botão de submissão
    submitted = st.form_submit_button("Gerar Dados")
    # Condicional para verificar se o botão foi pressionado
    # Se o botão foi pressionado, gera os gráficos
    if submitted:
        # divisão da tela em duas colunas
        col1, col2 = st.columns(2)
        # Gráfico do total de matriculas por dependência
        with col1:
            grafico_matriculas_por_dependencia_localizacao_municipio(df_panorama_geral, ano_censo_dependencia_rural, municipio_dependencia_rural)
        # Gráfico do total de escolas por dependência
        with col2:
            grafico_escolas_por_dependencia_localizacao_municipio(df_panorama_geral, ano_censo_dependencia_rural, municipio_dependencia_rural)

        # Texto de análise dos gráficos
        st.write(texto_pan_rede_dependencia_rural_analise_2())

st.write(text_pan_rede_dependencia_rural_conclusao())


#===============================
# Seção 03 - Geração de Relatórios
#===============================
st.header("Geração de relatórios")
st.write(texto_pan_rede_relatorio_intro())

relatorio_rede_dados_escolas(df_panorama_geral)

## Colunas excluídas
#colunas_excluidas = [
#    'CO_MUNICIPIO', 
#    'TP_LOCALIZACAO_DIFERENCIADA', 
#    'IN_ENERGIA_REDE_PUBLICA', 
#    'IN_ENERGIA_GERADOR_FOSSIL',
#    'IN_ENERGIA_RENOVAVEL',
#    'IN_ENERGIA_INEXISTENTE'
#    ]
#
## Remover colunas excluídas
#df_panorama_geral = df_panorama_geral.drop(columns=colunas_excluidas)
#
## Renomear colunas para exibição
#colunas_renomeadas = {
#    'NU_ANO_CENSO': 'Ano do Censo',
#    'NO_MUNICIPIO': 'Município',
#    'NO_ENTIDADE': 'Nome da Escola',
#    'CO_ENTIDADE': 'Código da Escola',
#    'TP_DEPENDENCIA': 'Dep. Administrativa',
#    'TP_LOCALIZACAO': 'Localização',
#    'DS_ENDERECO': 'Endereço',
#    'DS_COMPLEMENTO': 'Complemento',
#    'QT_MAT_BAS': 'Matrículas'
#}
#df_panorama_geral = df_panorama_geral.rename(columns=colunas_renomeadas)
#
## Renomear valores da dependência administrativa e localização
#map_dependencia = {1: 'Federal', 2: 'Estadual', 3: 'Municipal'}
#map_localizacao = {1: 'Urbana', 2: 'Rural'}
#
#df_panorama_geral['Dep. Administrativa'] = df_panorama_geral['Dep. Administrativa'].map(map_dependencia)
#df_panorama_geral['Localização'] = df_panorama_geral['Localização'].map(map_localizacao)
#
## Identificar anos disponíveis
#anos_disponiveis = sorted(df_panorama_geral['Ano do Censo'].unique())
#ano_mais_recente = max(anos_disponiveis)
#
#
## Formulário principal
#with st.form("form_pan_rede_relatorio"):
#
#    col1, col2 = st.columns(2)
#    
#    with col1:
#
#        # Selectbox do ano
#        ano_censo_rede_relatorio = st.selectbox(
#            "Selecione o ano do Censo Escolar:",
#            options=anos_disponiveis,
#            index=anos_disponiveis.index(ano_mais_recente),
#            key="ano_censo_pan_rede_relatorio"
#        )
#
#        # Selectbox do Município
#        municipio_pan_rede_relatorio = st.selectbox(
#            "Selecione o Município:",
#            sorted(df_panorama_geral['Município'].unique()),
#            key="municipio_pan_rede_relatorio"
#        )
#
#    with col2:
#        # Cartão de filtros de dependência
#        with st.container(border=True):
#            st.markdown("##### Filtrar por Dependência Administrativa")
#            col1, col2, col3 = st.columns(3)
#            with col1:
#                federal = st.checkbox("Federal", value=True, key="dep_federal")
#            with col2:
#                estadual = st.checkbox("Estadual", value=True, key="dep_estadual")
#            with col3:
#                municipal = st.checkbox("Municipal", value=True, key="dep_municipal")
#            
#        dependencia_selecionada = []
#        if federal: dependencia_selecionada.append("Federal")
#        if estadual: dependencia_selecionada.append("Estadual")
#        if municipal: dependencia_selecionada.append("Municipal")
#    
#        # Cartão de filtros de localização
#        with st.container(border=True):
#            st.markdown("##### Filtrar por Localização")
#            col4, col5 = st.columns(2)
#            with col4:
#                urbana = st.checkbox("Urbana", value=True, key="loc_urbana")
#            with col5:
#                rural = st.checkbox("Rural", value=True, key="loc_rural")
#            
#        localizacao_selecionada = []
#        if urbana: localizacao_selecionada.append("Urbana")
#        if rural: localizacao_selecionada.append("Rural")
#
#    # Botão
#    submitted = st.form_submit_button("Gerar Dados")
#
#    if submitted:
#        df_filtrado = df_panorama_geral[
#            (df_panorama_geral['Ano do Censo'] == ano_censo_rede_relatorio) &
#            (df_panorama_geral['Município'] == municipio_pan_rede_relatorio) &
#            (df_panorama_geral['Dep. Administrativa'].isin(dependencia_selecionada)) &
#            (df_panorama_geral['Localização'].isin(localizacao_selecionada))
#        ]
#
#        st.write("### 📋 Dados filtrados:")
#        st.dataframe(df_filtrado)
