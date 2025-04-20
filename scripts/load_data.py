import pandas as pd
import streamlit as st

#==========================================================
# Funções para carregar os dados para páginas do projeto
#==========================================================

@st.cache_data
def carregar_dados_agua():
    """Carrega os dados de água potável do link CSV."""
    
    # URLs do arquivo CSV no GitHub
    url_agua = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_agua/df_censo_ac_agua.csv"
    
    # Carregar os dados diretamente dos links do GitHub
    df_censo_ac_agua = pd.read_csv(url_agua, delimiter=';', encoding='utf-8', low_memory=False)
    
    return df_censo_ac_agua


@st.cache_data
def carregar_dados_panorama_geral():
    """Carrega os dados do panorama geral do link CSV."""
    
    # URLs do arquivo CSV no GitHub
    url_panorama_geral = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_geral/df_panorama_geral.csv"
    
    # Carregar os dados diretamente dos links do GitHub
    df_panorama_geral = pd.read_csv(url_panorama_geral, delimiter=';', encoding='utf-8', low_memory=False)
    
    return df_panorama_geral

@st.cache_data
def carregar_dados(url):
    """Carrega dados de um arquivo CSV a partir de uma URL fornecida."""
        # Carregar os dados diretamente do link fornecido
    df = pd.read_csv(url, delimiter=';', encoding='utf-8', low_memory=False)
    
    return df


#===========================================================
#Funcções para carregar tabelas em subseções
#===========================================================

# Função para gerar DataFrame com o total de alunos e escolas por dependência administrativa
def dataframe_dependencia_municipio(df, ano_censo, municipio):
    """
    Gera um DataFrame com o total de alunos e escolas por dependência administrativa no município selecionado.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'NU_ANO_CENSO', 'NO_MUNICIPIO', 'TP_DEPENDENCIA', 'QT_MAT_BAS', 'CO_ENTIDADE'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário.
    municipio : str
        Nome do município selecionado pelo usuário.

    Retorno:
    --------
    pd.DataFrame
        DataFrame com colunas: ['Dependência Administrativa', 'Total de Alunos', 'Total de Escolas']
    """

    # Filtra o DataFrame pelo ano e município selecionados
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    # Agrupa por Dependência Administrativa
    resultado = df_filtrado.groupby('TP_DEPENDENCIA').agg(
        Total_Alunos=('QT_MAT_BAS', 'sum'),
        Total_Escolas=('CO_ENTIDADE', 'count')
    ).reset_index()

    # Mapeia os valores numéricos de TP_DEPENDENCIA para categorias legíveis
    map_dependencia = {
        1: 'Federal',
        2: 'Estadual',
        3: 'Municipal',
        4: 'Privada'
    }
    resultado['Dependência Administrativa'] = resultado['TP_DEPENDENCIA'].map(map_dependencia)

    # Reorganiza colunas
    resultado = resultado[['Dependência Administrativa', 'Total_Alunos', 'Total_Escolas']]

    return resultado


# Função para gerar dataframe para o total de alunos por localizacao
def dataframe_totais_por_localizacao_municipio(df, ano_censo, municipio):
    """
    Gera um DataFrame com o total de alunos e escolas por localizacao no ano selecionado.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'NU_ANO_CENSO', 'TP_LOCALIZACAO', 'QT_MAT_BAS'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário.

    Retorno:
    --------
    pd.DataFrame
        DataFrame com colunas: ['Localização', 'Total de Alunos']
    """

    # Filtra o DataFrame pelo ano e Municípios selecionados
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio) &
        (df['TP_LOCALIZACAO'].notnull())
    ]

    # Agrupa por Localização e soma os alunos
    resultado = df_filtrado.groupby('TP_LOCALIZACAO').agg(
        Total_Alunos = ('QT_MAT_BAS', 'sum'),
        Total_Escolas = ('CO_ENTIDADE', 'count')
    ).reset_index()
    
    # Mapeia os valores numéricos de TP_LOCALIZACAO para categorias legíveis
    map_localizacao = {
        1: 'Urbana',
        2: 'Rural'
    }
    resultado['Localizacao'] = resultado['TP_LOCALIZACAO'].map(map_localizacao)
    resultado = resultado[['Localizacao', 'Total_Alunos', 'Total_Escolas']]
    
    return resultado


# Função para gerar dataframe para o total de escolas e alunos por localizacao diferenciada
def dataframe_totais_por_localizacao_diferenciada_municipio(df, ano_censo, municipio):    
    """
    Gera um DataFrame com o total de alunos e escolas por localizacao no ano selecionado.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'NU_ANO_CENSO', 'TP_LOCALIZACAO', 'QT_MAT_BAS'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário.

    Retorno:
    --------
    pd.DataFrame
        DataFrame com colunas: ['Localização', 'Total de Alunos']
    """
    
    # Filtra o DataFrame pelo ano e Municípios selecionados
    df_filtrado = df[
        (df['TP_LOCALIZACAO_DIFERENCIADA'] != 0) &
        (df['TP_LOCALIZACAO_DIFERENCIADA'].notnull()) &
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

        # Agrupa por Localização e soma os alunos
    resultado = df_filtrado.groupby('TP_LOCALIZACAO_DIFERENCIADA').agg(
        Total_Alunos = ('QT_MAT_BAS', 'sum'),
        Total_Escolas = ('CO_ENTIDADE', 'count')              
    ).reset_index()
    
    # Mapeamento os valores numériocos de TP_LOCALIZACAO_DIFERENCIADA para categorias legíveis
    map_localizacao = {
        1: 'Assentamento',
        2: 'Terra Indígena',
        3: 'Quilombola',
        8: 'Com. Tradicionais'
    }
    resultado['Loc. Diferenciada'] = resultado['TP_LOCALIZACAO_DIFERENCIADA'].map(map_localizacao)
    resultado = resultado[['Loc. Diferenciada', 'Total_Alunos', 'Total_Escolas']]
    return resultado