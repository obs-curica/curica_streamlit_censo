
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import streamlit as st
import numpy as np
from utils import COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO

#============================
# PAGINA PANORAMA GERAL
#=============================

# Função para plotar gráfico de barras horizontal com o total de matriculas por município
def grafico_matriculas_por_municipio(df, ano_censo):
    """
    Gera um gráfico de barras horizontal com o total de matriculas por município.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'NO_MUNICIPIO', 'QT_MAT_BAS' e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import matplotlib.ticker as ticker
    import streamlit as st

    # Filtra o DataFrame pelo ano selecionado
    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    # Agrupar e somar os matriculas por município
    resultado_matriculas = df_filtrado.groupby('NO_MUNICIPIO')['QT_MAT_BAS'].sum().sort_values(ascending=True)

    # Gradiente de cores
    cmap = mcolors.LinearSegmentedColormap.from_list('custom_gradient', ['#B0E0E6', '#FFC107'])
    norm = plt.Normalize(vmin=resultado_matriculas.min(), vmax=resultado_matriculas.max())
    cores = [cmap(norm(valor)) for valor in resultado_matriculas]

    # Gráfico total de matriculas por município
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15, max(8, 0.5 * len(resultado_matriculas))))
    bars = ax.barh(resultado_matriculas.index, resultado_matriculas.values, color=cores)

    # Ajusta dinamicamente o limite superior do eixo X com uma folga de 10%
    limite_superior = resultado_matriculas.max() * 1.1
    ax.set_xlim(right=limite_superior)

    # Título e rótulos
    ax.set_title('Total de matrículas por Município', color='#FFA07A', fontsize=40)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    # Ticks
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=25)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=25)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1000)}mil'))

    # Inserir valores nas barras com base mil
    for i, valor in enumerate(resultado_matriculas):
        ax.text(valor + (resultado_matriculas.max() * 0.01), i, f'{int(valor/1000)}', va='center',
                color='white', fontweight='bold', fontsize=22)

    fig.tight_layout()
    st.pyplot(fig)

# Função para plotar gráfico de barras horizontal com o total de escolas 
def grafico_escolas_por_municipio(df, ano_censo):
    """
    Gera um gráfico de barras horizontal com o total de escolas por município.
    
    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'NO_MUNICIPIO' e 'CO_ENTIDADE'.
    """
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import streamlit as st

    # Filtra o DataFrame pelo ano selecionado
    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    # Agrupa por Município e conta as escolas
    resultado_escolas = df_filtrado.groupby('NO_MUNICIPIO')['CO_ENTIDADE'].count().sort_values(ascending=True)
    
        # Gradiente de cores
    cmap = mcolors.LinearSegmentedColormap.from_list('custom_gradient', ['#B0E0E6', '#FFC107'])
    norm = plt.Normalize(vmin=resultado_escolas.min(), vmax=resultado_escolas.max())
    cores = [cmap(norm(valor)) for valor in resultado_escolas]

    # Gráfico total de escolas por Município
    # Estilo escuro
    plt.style.use('dark_background')
    
    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(15, max(8, 0.5 * len(resultado_escolas))))
    bars = ax.barh(resultado_escolas.index, resultado_escolas.values, color=cores)
    
    # Ajusta dinamicamente o limite superior do eixo X com uma folga de 10%
    limite_superior = resultado_escolas.max() * 1.1
    ax.set_xlim(right=limite_superior)

    
    # Título e rótulos
    ax.set_title('Total de Escolas por Município', color='#FFA07A', fontsize=40)
    # Estilo dos spines
    ax = plt.gca()
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
        
    # Ticks
    plt.xticks(color='#FFA07A', fontsize=25)
    plt.yticks(color='#FFA07A', fontsize=25)
    
    # Inserir valores nas barras
    for i, valor in enumerate(resultado_escolas):
        plt.text(valor + (resultado_escolas.max() * 0.01), i, str(valor), va='center',
                 color='white', fontweight='bold', fontsize=22)
    
    plt.tight_layout()
    st.pyplot(plt)

# Função para gráfico de barras verticais para o total de escolas por dependência administrativa
def grafico_escolas_por_dependencia(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de escolas por dependência administrativa.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_DEPENDENCIA', e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Filtra o DataFrame pelo ano selecionado
    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    # Agrupa por Dependência Administrativa e conta as escolas
    dependencia_counts = df_filtrado['TP_DEPENDENCIA'].value_counts().sort_index()
    dependencia_counts.index = dependencia_counts.index.map({1: 'Federal', 2: 'Estadual', 3: 'Municipal'})

    # Cores fixas opacas por categoria (RGBA)
    cores_localizacao = {
        'Federal': (0/255, 191/255, 255/255, 0.7),     # Azul celeste com 50% opacidade
        'Estadual': (255/255, 160/255, 122/255, 0.7),  # Salmão com 50% opacidade
        'Municipal': (118/255, 238/255, 0/255, 0.7)     # Verde fosforescente com 50% opacidade
    }
   
    cores = [cores_localizacao[r] for r in dependencia_counts.index]

    # Estilo escuro
    plt.style.use('dark_background')

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(dependencia_counts.index, dependencia_counts.values, color=cores)

    # Título e rótulos
    ax.set_title('Total de Escolas por Dependência Administrativa', color='#FFA07A', fontsize=25)
    ax.set_ylabel('Número de Escolas', color='#FFA07A', fontsize=14)
    # ax.set_xlabel(f'Ano {ano_censo}', color='#FFA07A', fontsize=25)
    
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    # Ticks
    ax.set_ylim(0, dependencia_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)

    # Inserir valores nas barras
    for i, valor in enumerate(dependencia_counts):
        ax.text(i, valor + max(dependencia_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)

    fig.tight_layout()
    st.pyplot(fig)

# Função para gráfico de barras verticais para o total de matriculas por dependência administrativa
def grafico_matriculas_por_dependencia(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de matriculas por dependência administrativa.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_DEPENDENCIA', 'QT_MAT_BAS' e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    from matplotlib.ticker import MaxNLocator
    


    # Filtra o DataFrame pelo ano selecionado
    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    # Agrupa por Dependência Administrativa e soma os matriculas
    dependencia_counts = df_filtrado.groupby('TP_DEPENDENCIA')['QT_MAT_BAS'].sum().sort_index().astype(int)
    dependencia_counts.index = dependencia_counts.index.map({1: 'Federal', 2: 'Estadual', 3: 'Municipal'})

    # Cores fixas opacas por categoria (RGBA)
    cores_localizacao = {
        'Federal': (0/255, 191/255, 255/255, 0.7),     # Azul celeste com 50% opacidade
        'Estadual': (255/255, 160/255, 122/255, 0.7),  # Salmão com 50% opacidade
        'Municipal': (118/255, 238/255, 0/255, 0.7)     # Verde fosforescente com 50% opacidade
    }
   
    cores = [cores_localizacao[r] for r in dependencia_counts.index]

    # Estilo escuro
    plt.style.use('dark_background')

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(dependencia_counts.index, dependencia_counts.values, color=cores)

    # Título e rótulos
    ax.set_title(f'Total de matrículas por Dependência Administrativa', color='#FFA07A', fontsize=25)
    #ax.set_ylabel('Número de matriculas', color='#FFA07A', fontsize=14)
    #ax.set_xlabel(f'Ano {ano_censo}', color='#FFA07A', fontsize=25)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    # Ticks
    ax.set_ylim(0, dependencia_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    # Inserir valores nas barras
    for i, valor in enumerate(dependencia_counts):
        ax.text(i, valor + max(dependencia_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
    fig.tight_layout()
    st.pyplot(fig)

# Função para gráfico de barras total de matriculas por dependência, por município
def grafico_matriculas_por_dependencia_municipio(df, ano_censo, municipio):
    """
    Gera um gráfico de barras verticais com o total de matriculas por dependência administrativa.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_DEPENDENCIA', 'QT_MAT_BAS' e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    from matplotlib.ticker import MaxNLocator

    # Filtra o DataFrame pelo ano e município selecionados
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    # Agrupa por Dependência Administrativa e soma os matriculas
    dependencia_counts = df_filtrado.groupby('TP_DEPENDENCIA')['QT_MAT_BAS'].sum().sort_index().astype(int)
    dependencia_counts.index = dependencia_counts.index.map({1: 'Federal', 2: 'Estadual', 3: 'Municipal'})

    # Cores fixas opacas por categoria (RGBA)
    cores_localizacao = {
        'Federal': (0/255, 191/255, 255/255, 0.7),     # Azul celeste com 50% opacidade
        'Estadual': (255/255, 160/255, 122/255, 0.7),  # Salmão com 50% opacidade
        'Municipal': (118/255, 238/255, 0/255, 0.7)     # Verde fosforescente com 50% opacidade
    }
   
    cores = [cores_localizacao[r] for r in dependencia_counts.index]

    # Estilo escuro
    plt.style.use('dark_background')

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(dependencia_counts.index, dependencia_counts.values, color=cores)

    # Título e rótulos
    ax.set_title(f'Total de matrículas por Dep. Administrativa em {municipio}', color='#FFA07A', fontsize=25)
    
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    
    # Ticks
    ax.set_ylim(0, dependencia_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    
    # Inserir valores nas barras
    for i, valor in enumerate(dependencia_counts):
        ax.text(i, valor + max(dependencia_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
    
    fig.tight_layout()
    st.pyplot(fig)

# Função para gráfico de barras total de escolas por dependência, por município
def grafico_escolas_por_dependencia_municipio(df, ano_censo, municipio):
    """
    Gera um gráfico de barras verticais com o total de escolas por dependência administrativa.
    
    Parâmetros:
    ---------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_DEPENDENCIA', e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    
    # Filtra o DataFrame pelo ano e município selecionados
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]
    
    # Agrupa por Localização e conta as escolas
    dependencia_counts = df_filtrado['TP_DEPENDENCIA'].value_counts().sort_index()
    dependencia_counts.index = dependencia_counts.index.map({1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    # Cores fixas opacas por categoria (RGBA)
    cores_localizacao = {
        'Federal': (0/255, 191/255, 255/255, 0.7),     # Azul celeste com 50% opacidade
        'Estadual': (255/255, 160/255, 122/255, 0.7),  # Salmão com 50% opacidade
        'Municipal': (118/255, 238/255, 0/255, 0.7)     # Verde fosforescente com 50% opacidade
    }
    
    cores = [cores_localizacao[r] for r in dependencia_counts.index]
    
    # Estilo escuro
    plt.style.use('dark_background')
    
    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(dependencia_counts.index, dependencia_counts.values, color=cores)
    
    # Título e rótulos
    ax.set_title(f'Total de Escolas por Dep. Administrativa em {municipio}', color='#FFA07A', fontsize=25)
    # ax.set_ylabel('Número de Escolas', color='#FFA07A', fontsize=14)
    # ax.set_xlabel(f'Ano {ano_censo}', color='#FFA07A', fontsize=25)
    
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
        
    # Ticks
    ax.set_ylim(0, dependencia_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)
    
    # Inserir valores nas barras
    for i, valor in enumerate(dependencia_counts):
        ax.text(i, valor + max(dependencia_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
        
    fig.tight_layout()
    st.pyplot(fig)

# Função para gráfico de barras panorama Urbano vs Rural
def grafico_escolas_por_localizacao(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de escolas por localização.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_LOCALIZACAO', e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Filtra o DataFrame pelo ano selecionado
    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    # Agrupa por Dependência Administrativa e conta as escolas
    localizacao_counts = df_filtrado['TP_LOCALIZACAO'].value_counts().sort_index()
    localizacao_counts.index = localizacao_counts.index.map({1: 'Urbana', 2: 'Rural'})

    # Cores fixas opacas por categoria
    cores_localizacao = {
        'Rural': '#1FB029',
        'Urbana': '#C0C0C0'
    }
   
    cores = [cores_localizacao[r] for r in localizacao_counts.index]

    # Estilo escuro
    plt.style.use('dark_background')

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores)

    # Título e rótulos
    ax.set_title('Total de Escolas por Localização', color='#FFA07A', fontsize=25)
    # ax.set_ylabel('Número de Escolas', color='#FFA07A', fontsize=14)
    # ax.set_xlabel('Localização', color='#FFA07A', fontsize=14)
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    # Ticks
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)
    # Inserir valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
    fig.tight_layout()
    st.pyplot(fig)

# Função para gráfico de barras verticais para o total de matriculas por localizacao
def grafico_matriculas_por_localizacao(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de matriculas por localizacao.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_LOCALIZACAO', 'QT_MAT_BAS' e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    from matplotlib.ticker import MaxNLocator

    # Filtra o DataFrame pelo ano selecionado
    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    # Agrupa por Localização e soma os matriculas
    localizacao_counts = df_filtrado.groupby('TP_LOCALIZACAO')['QT_MAT_BAS'].sum().sort_index().astype(int)
    localizacao_counts.index = localizacao_counts.index.map({1: 'Urbana', 2: 'Rural'})

    # Cores fixas opacas por categoria
    cores_localizacao = {
        'Rural': '#1FB029',
        'Urbana': '#C0C0C0'
    }

  
    cores = [cores_localizacao[r] for r in localizacao_counts.index]

    # Estilo escuro
    plt.style.use('dark_background')

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores)

    # Título e rótulos
    ax.set_title('Total de matrículas por Localização', color='#FFA07A', fontsize=25)
    # ax.set_ylabel('Número de matriculas', color='#FFA07A', fontsize=14)
    # ax.set_xlabel('Localização', color='#FFA07A', fontsize=14)
    
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    
    # Ticks
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    
    # Inserir valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
    fig.tight_layout()
    st.pyplot(fig)

# Função gráfico de barras total de matriculas por localizacao, por município
def grafico_matriculas_por_localizacao_municipio(df, ano_censo, municipio):
    """
    Gera um gráfico de barras verticais com o total de matriculas por localização.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_LOCALIZACAO', 'QT_MAT_BAS' e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    municipio : str
        Nome do município para filtrar os dados.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    from matplotlib.ticker import MaxNLocator

    # Filtra o DataFrame pelo ano e município selecionados
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    # Agrupa por Localização e soma os matriculas
    localizacao_counts = df_filtrado.groupby('TP_LOCALIZACAO')['QT_MAT_BAS'].sum().sort_index().astype(int)
    localizacao_counts.index = localizacao_counts.index.map({1: 'Urbana', 2: 'Rural'})

    # Cores fixas opacas por categoria
    cores_localizacao = {
        'Rural': '#1FB029',
        'Urbana': '#C0C0C0'
    }

  
    cores = [cores_localizacao[r] for r in localizacao_counts.index]

    # Estilo escuro
    plt.style.use('dark_background')

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores)

    # Título e rótulos
    ax.set_title(f'Total de matrículas por Localização em {municipio}', color='#FFA07A', fontsize=25)
    
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    
    # Ticks
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)
    
    # Definindo o número de ticks no eixo y
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    # Inserir valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
    fig.tight_layout()
    st.pyplot(fig)

# Função gráfico de barras total de escolas por localizacao, por município
def grafico_escolas_por_localizacao_municipio(df, ano_censo, municipio):
    """
    Gera um gráfico de barras verticais com o total de escolas por localização.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_LOCALIZACAO', e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    # Filtra o DataFrame pelo ano e município selecionados
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio) &
        (df['TP_LOCALIZACAO'].notnull())
    ]

    # Agrupa por Localização e soma os matriculas
    localizacao_counts = df_filtrado['TP_LOCALIZACAO'].value_counts().sort_index()
    localizacao_counts.index = localizacao_counts.index.map({1: 'Urbana', 2: 'Rural'})

    # Cores fixas opacas por categoria
    cores_localizacao = {
        'Rural': '#1FB029',
        'Urbana': '#C0C0C0'
    }
    cores = [cores_localizacao[r] for r in localizacao_counts.index]

    # Estilo escuro
    plt.style.use('dark_background')

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores)

    # Título e rótulos
    ax.set_title(f'Total de Escolas por Localização em {municipio}', color='#FFA07A', fontsize=25)
    
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    # Ticks
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)

    # Inserir valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)

    fig.tight_layout()
    st.pyplot(fig)

# Função gráfico barras agrupadas matriculas por dependência e localização
def grafico_matriculas_por_dependencia_localizacao(df, ano_censo):
    """
    Gera gráfico de barras agrupadas com total de matriculas por dependência e localização (urbana/rural).

    Parâmetros:
    - df : pd.DataFrame
        DataFrame contendo as colunas 'TP_DEPENDENCIA', 'TP_LOCALIZACAO', 'QT_MAT_BAS', 'NU_ANO_CENSO'
    - ano_censo : int
        Ano do censo escolar a ser filtrado
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import numpy as np

    # Filtro por ano
    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    # Agrupamento por dependência e localização, somando os matriculas
    agrupado = df_filtrado.groupby(['TP_DEPENDENCIA', 'TP_LOCALIZACAO'])['QT_MAT_BAS'].sum().unstack(fill_value=0)
    agrupado = agrupado.rename(index={1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    agrupado = agrupado.rename(columns={1: 'Urbana', 2: 'Rural'})

    # Preparar dados
    categorias = agrupado.index.tolist()
    urbana = agrupado['Urbana']
    rural = agrupado['Rural']
    x = np.arange(len(categorias))
    largura = 0.35

    # Estilo escuro
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotagem
    ax.bar(x - largura/2, urbana, width=largura, label='Urbana', color='#C0C0C0')
    ax.bar(x + largura/2, rural, width=largura, label='Rural', color='#1FB029')

    # Eixos e rótulos
    ax.set_title('Total de matrículas por Dependência e Localização', color='#FFA07A', fontsize=25)
    ax.set_xticks(x)
    ax.set_xticklabels(categorias, color='#FFA07A', fontsize=25)
    ax.tick_params(axis='y', colors='#FFA07A')
    ax.legend()

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite superior responsivo
    limite_superior = max(urbana.max(), rural.max()) * 1.15
    ax.set_ylim(0, limite_superior)

    # Inserção de valores nas barras com espaçamento dinâmico
    espaco_texto = limite_superior * 0.015
    for i in range(len(categorias)):
        ax.text(x[i] - largura/2, urbana[i] + espaco_texto, f'{urbana[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=17)
        ax.text(x[i] + largura/2, rural[i] + espaco_texto, f'{rural[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=17)

    plt.tight_layout()
    st.pyplot(fig)

# Função gráfico barras agrupadas escolas por dependência e localização
def grafico_escolas_por_dependencia_localizacao(df, ano_censo):
    """
    Gera gráfico de barras agrupadas com total de escolas por dependência e localização (urbana/rural).

    Parâmetros:
    - df : pd.DataFrame
        DataFrame contendo as colunas 'TP_DEPENDENCIA', 'TP_LOCALIZACAO', 'NU_ANO_CENSO'
    - ano_censo : int
        Ano do censo escolar a ser filtrado
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import numpy as np

    # Filtros iniciais
    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    # Agrupamento por dependência e localização
    agrupado = df_filtrado.groupby(['TP_DEPENDENCIA', 'TP_LOCALIZACAO'])['CO_ENTIDADE'].count().unstack(fill_value=0)
    agrupado = agrupado.rename(index={1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    agrupado = agrupado.rename(columns={1: 'Urbana', 2: 'Rural'})

    # Preparar os dados
    categorias = agrupado.index.tolist()
    urbana = agrupado['Urbana']
    rural = agrupado['Rural']

    x = np.arange(len(categorias))
    largura = 0.35

    # Estilo do projeto
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotagem das barras
    ax.bar(x - largura/2, urbana, width=largura, label='Urbana', color='#C0C0C0')
    ax.bar(x + largura/2, rural, width=largura, label='Rural', color='#1FB029')

    # Eixos e rótulos
    ax.set_title('Total de Escolas por Dependência e Localização', color='#FFA07A', fontsize=25)
    ax.set_xticks(x)
    ax.set_xticklabels(categorias, color='#FFA07A', fontsize=25)
    ax.tick_params(axis='y', colors='#FFA07A')
    ax.legend()

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite superior responsivo
    limite_superior = max(urbana.max(), rural.max()) * 1.15
    ax.set_ylim(0, limite_superior)

    # Inserção de valores nas barras com espaçamento dinâmico
    espaco_texto = limite_superior * 0.015
    for i in range(len(categorias)):
        ax.text(x[i] - largura/2, urbana[i] + espaco_texto, f'{urbana[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=20)
        ax.text(x[i] + largura/2, rural[i] + espaco_texto, f'{rural[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=20)

    plt.tight_layout()
    st.pyplot(fig)

# Função gráfico barras agrupadas matriculas por dependência e localização, por Município
def grafico_matriculas_por_dependencia_localizacao_municipio(df, ano_censo, municipio):
    """
    Gera gráfico de barras agrupadas com o total de matriculas por dependência e localização (urbana/rural) 
    no município e ano selecionados.

    Parâmetros:
    - df : pd.DataFrame
        DataFrame contendo as colunas 'TP_DEPENDENCIA', 'TP_LOCALIZACAO', 'QT_MAT_BAS', 'NU_ANO_CENSO', 'NO_MUNICIPIO'
    - ano_censo : int
        Ano do censo escolar a ser filtrado.
    - municipio : str
        Nome do município a ser filtrado.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import numpy as np

    # Filtro por ano e município
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    # Agrupamento por dependência e localização
    agrupado = df_filtrado.groupby(['TP_DEPENDENCIA', 'TP_LOCALIZACAO'])['QT_MAT_BAS'].sum().unstack(fill_value=0)
    agrupado = agrupado.rename(index={1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    agrupado = agrupado.rename(columns={1: 'Urbana', 2: 'Rural'})

    # Preparar dados
    categorias = agrupado.index.tolist()
    urbana = agrupado['Urbana']
    rural = agrupado['Rural']
    x = np.arange(len(categorias))
    largura = 0.35

    # Estilo escuro
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Barras
    ax.bar(x - largura/2, urbana, width=largura, label='Urbana', color='#C0C0C0')
    ax.bar(x + largura/2, rural, width=largura, label='Rural', color='#1FB029')

    # Eixos e rótulos
    ax.set_title(f'Matrículas por Dependência e Localização - {municipio} ({ano_censo})', color='#FFA07A', fontsize=25)
    ax.set_xticks(x)
    ax.set_xticklabels(categorias, color='#FFA07A', fontsize=25)
    ax.tick_params(axis='y', colors='#FFA07A')
    ax.legend()

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite superior responsivo
    limite_superior = max(urbana.max(), rural.max()) * 1.15
    ax.set_ylim(0, limite_superior)

    # Inserção de valores nas barras com espaçamento dinâmico
    espaco_texto = limite_superior * 0.015
    for i in range(len(categorias)):
        ax.text(x[i] - largura/2, urbana[i] + espaco_texto, f'{urbana[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=20)
        ax.text(x[i] + largura/2, rural[i] + espaco_texto, f'{rural[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=20)

    plt.tight_layout()
    st.pyplot(fig)

# Função gráfico barras agrupadas escolas por dependência e localização, por Município
def grafico_escolas_por_dependencia_localizacao_municipio(df, ano_censo, municipio):
    """
    Gera gráfico de barras agrupadas com o total de escolas por dependência e localização (urbana/rural)
    no município e ano selecionados.

    Parâmetros:
    - df : pd.DataFrame
        DataFrame contendo as colunas 'TP_DEPENDENCIA', 'TP_LOCALIZACAO', 'CO_ENTIDADE', 'NU_ANO_CENSO', 'NO_MUNICIPIO'
    - ano_censo : int
        Ano do censo escolar a ser filtrado.
    - municipio : str
        Nome do município a ser filtrado.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import numpy as np

    # Filtro por ano e município
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    # Agrupamento por dependência e localização, contando entidades únicas
    agrupado = df_filtrado.groupby(['TP_DEPENDENCIA', 'TP_LOCALIZACAO'])['CO_ENTIDADE'].nunique().unstack(fill_value=0)
    agrupado = agrupado.rename(index={1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    agrupado = agrupado.rename(columns={1: 'Urbana', 2: 'Rural'})

    # Preparar dados
    categorias = agrupado.index.tolist()
    urbana = agrupado['Urbana']
    rural = agrupado['Rural']
    x = np.arange(len(categorias))
    largura = 0.35

    # Estilo escuro
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Barras
    ax.bar(x - largura/2, urbana, width=largura, label='Urbana', color='#C0C0C0')
    ax.bar(x + largura/2, rural, width=largura, label='Rural', color='#1FB029')

    # Eixos e rótulos
    ax.set_title(f'Escolas por Dependência e Localização - {municipio} ({ano_censo})', color='#FFA07A', fontsize=25)
    ax.set_xticks(x)
    ax.set_xticklabels(categorias, color='#FFA07A', fontsize=25)
    ax.tick_params(axis='y', colors='#FFA07A')
    ax.legend()

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite superior responsivo
    limite_superior = max(urbana.max(), rural.max()) * 1.15
    ax.set_ylim(0, limite_superior)

    # Inserção de valores nas barras com espaçamento dinâmico
    espaco_texto = limite_superior * 0.015
    for i in range(len(categorias)):
        ax.text(x[i] - largura/2, urbana[i] + espaco_texto, f'{urbana[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=20)
        ax.text(x[i] + largura/2, rural[i] + espaco_texto, f'{rural[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=20)


    plt.tight_layout()
    st.pyplot(fig)



#============================
# PAGINA PANORAMA FINANCIAMENTO
#=============================

# Gráfico de barras vertical com receita do FNDE por ano
def grafico_fnde_receita_total(df):
    """
    Gera um gráfico de barras verticais mostrando a evolução da receita total do FNDE ao longo dos anos.
    Os valores são exibidos em bilhões de reais (R$ bi).

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'Ano' e 'Pago'.
    """
    # Ordenar por ano
    df_filtrado = df.sort_values(by='Ano').copy()

    # Converter valores para bilhões
    df_filtrado['Pago_bi'] = df_filtrado['Pago'] / 1_000_000_000

    # Estilo escuro
    plt.style.use('dark_background')

    # Cor padrão (verde escuro para manter padrão visual financeiro)
    cor_barras = '#006400'

    # Criar gráfico
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.bar(df_filtrado['Ano'].astype(str), df_filtrado['Pago_bi'], color=cor_barras)

    # Título e rótulos
    ax.set_title('Evolução da Receita do FNDE', color='#FFA07A', fontsize=16)
    ax.set_ylabel('Valor em bilhões de R$ (bi)', color='#FFA07A', fontsize=10)
    ax.set_xlabel('Fonte: Painel do Orçamento Federal', color='#FFA07A', fontsize=10)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Ticks
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=12)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=12)

    # Inserir valores no topo das barras
    max_valor = df_filtrado['Pago_bi'].max()
    for i, valor in enumerate(df_filtrado['Pago_bi']):
        ax.text(
            i,
            valor + (max_valor * 0.01),
            f'{valor:.2f}',
            ha='center',
            color='white',
            fontsize=10,
            fontweight='bold'
        )

    fig.tight_layout()
    st.pyplot(fig)

# Gráfico FNDE despesas
def grafico_fnde_acoes(df, ano):
    """
    Gera um gráfico de barras horizontais com a dotação atual das ações do FNDE no ano selecionado.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'Ano', 'Ação' e 'Dotação Atual (R$)'
    ano : int
        Ano para o qual o gráfico será filtrado
    """

    # Filtrar o DataFrame pelo ano selecionado
    df_filtrado = df[df["Ano"] == ano].copy()

    # Remover valores nulos ou negativos
    df_filtrado = df_filtrado[df_filtrado["Dotação Atual (R$)"] > 0]

    # Ordenar pelo valor
    df_filtrado = df_filtrado.sort_values(by="Dotação Atual (R$)", ascending=True)

    # Converter para bilhões
    df_filtrado["Dotação (bi)"] = df_filtrado["Dotação Atual (R$)"] / 1_000_000_000

    # Gradiente da cor verde para branco
    cor_inicio = "#FFFFFF"  # Verde escuro
    cor_fim = "#006400"     # Branco
    cmap = mcolors.LinearSegmentedColormap.from_list("verde_para_branco", [cor_inicio, cor_fim])
    norm = mcolors.Normalize(vmin=df_filtrado["Dotação (bi)"].min(), vmax=df_filtrado["Dotação (bi)"].max())
    cores = [cmap(norm(v)) for v in df_filtrado["Dotação (bi)"]]

    # Plot
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 5.65))

    ax.barh(df_filtrado["Ação"], df_filtrado["Dotação (bi)"], color=cores)

    # Título e rótulos
    ax.set_title(f"Detalhamento por Ação - FNDE {ano}", color="#FFA07A", fontsize=18)
    ax.set_xlabel("Fonte: Relatório de Gestão do FNDE", color="#FFA07A", fontsize=11)
    ax.set_ylabel("Valor em bilhões de R$ (bi)", color="#FFA07A", fontsize=10)

    # Estilo dos eixos
    ax.tick_params(colors='#FFA07A', labelsize=12)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Ajuste do eixo X com margem para texto
    max_valor = df_filtrado["Dotação (bi)"].max()
    ax.set_xlim(0, max_valor * 1.15)

    # Inserir valores nas barras
    for i, valor in enumerate(df_filtrado["Dotação (bi)"]):
        ax.text(
            valor + max_valor * 0.01,
            i,
            f"{valor:.2f}",
            color="white",
            va="center",
            fontsize=11
        )

    fig.tight_layout(pad=2.0)
    st.pyplot(fig)

# Função gráfico de barras horizontal fundeb por ano
def grafico_fundeb_total_ano(df, ano):
    """
    Gera um gráfico de barras horizontal com o total de receita do FUNDEB por Município e Estado, para o ano selecionado.
    Os valores são convertidos e apresentados em milhões de reais (R$ mi).

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'nome', 'ano' e 'valor_receita_total_fundeb'.
    ano : int
        Ano selecionado pelo usuário na interface Streamlit.
    """
    # Filtra e ordena os dados
    df_filtrado = df[df['ano'] == ano].copy()
    df_filtrado.sort_values(by='valor_receita_total_fundeb', ascending=True, inplace=True)

    # Conversão para milhões
    df_filtrado['valor_milhoes'] = df_filtrado['valor_receita_total_fundeb'] / 1_000_000

    # Gradiente de verde (verde claro -> verde escuro)
    cmap = mcolors.LinearSegmentedColormap.from_list('verde_gradiente', ['#90ee90', '#006400'])
    norm = plt.Normalize(vmin=df_filtrado['valor_milhoes'].min(),
                         vmax=df_filtrado['valor_milhoes'].max())
    cores = [cmap(norm(v)) for v in df_filtrado['valor_milhoes']]

    # Estilo escuro
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, max(6, 0.48 * len(df_filtrado))))

    # Gráfico
    ax.barh(df_filtrado['nome'], df_filtrado['valor_milhoes'], color=cores)

    # Título e eixos
    ax.set_title(f'Total da Receita do Fundeb - {ano}', color='#FFA07A', fontsize=25)
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=16)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=16)
    
    # Estilo dos ticks e spines
    ax.tick_params(colors='#FFA07A', labelsize=17)
    # Define o número máximo de spines
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Limite dinâmico do eixo X
    max_valor = df_filtrado['valor_milhoes'].max()
    limite_superior = max_valor * 1.3
    ax.set_xlim(right=limite_superior)
    
    # Reduz o espaçamento superior e inferior
    n_barras = len(df_filtrado)
    ax.set_ylim(-0.7, n_barras - 0.3)


    # Alinha o spine direito com o limite superior dinâmico
    ax.spines['right'].set_position(('data', limite_superior * 1))  # ajusta a posição do spine direito para o limite superior + 2%
    
    # Inserir rótulos nas barras (em milhões com uma casa decimal)
    for i, valor in enumerate(df_filtrado['valor_milhoes']):
        deslocamento = limite_superior * 0.01
        ax.text(valor + deslocamento, i, f"R$ {valor:,.1f}",
                color='white', va='center', fontsize=17, fontweight='bold')

    fig.tight_layout()
    st.pyplot(fig)

# Função gráfico fundeb ente
def grafico_fundeb_total_ente(df, ente):
    """
    Gera um gráfico de barras verticais mostrando a evolução da receita total do FUNDEB
    ao longo dos anos para o ente federado selecionado, com valores em milhões de reais.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'nome', 'ano' e 'valor_receita_total_fundeb'.
    ente : str
        Nome do Município ou Estado selecionado pelo usuário.
    """
    # Filtra os dados para o ente selecionado
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão para milhões
    df_filtrado['valor_milhoes'] = df_filtrado['valor_receita_total_fundeb'] / 1_000_000

    # Estilo escuro
    plt.style.use('dark_background')

    # Cores: Verde escuro fixo
    cor_barras = '#006400'

    # Plot
    fig, ax = plt.subplots(figsize=(9, 8.3))
    ax.bar(df_filtrado['ano'].astype(str), df_filtrado['valor_milhoes'], color=cor_barras)

    # Título e eixos
    ax.set_title(f'Fundeb Total por Ente - {ente}', color='#FFA07A', fontsize=19)
    ax.set_ylabel('Valor em milhões de reais (R$ mi)', color='#FFA07A', fontsize=12)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=12)
    
    
    # Estilo dos spines e ticks
    ax.tick_params(colors='#FFA07A', labelsize=13)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Rótulos nas barras
    for i, valor in enumerate(df_filtrado['valor_milhoes']):
        deslocamento = df_filtrado['valor_milhoes'].max() * 0.01
        ax.text(i, valor + deslocamento,
                f"R$ {valor:,.1f} mi", ha='center', color='white', fontsize=12, fontweight='bold')

    fig.tight_layout()
    st.pyplot(fig)
    
# Gráfico de barras vertical com o indicador de gastos com remuneração
def grafico_indicador_despesa_profissionais(df, ente):
    """
    Gera um gráfico de barras verticais mostrando a evolução do indicador de gastos com 
    a remuneração dos profissionais da educação, ao longo dos anos, para o ente selecionado.
    """


    # Filtrar dados do ente
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float
    df_filtrado['indicador_despesa_fundeb_profissionais'] = pd.to_numeric(
        df_filtrado['indicador_despesa_fundeb_profissionais'].astype(str).str.replace(',', '.'),
        errors='coerce'
    )

    # Estilo do gráfico
    plt.style.use('dark_background')

    # Definir cores condicionais por linha
    cores = [
        '#8B0000' if valor < 70 else '#006400'
        for valor in df_filtrado['indicador_despesa_fundeb_profissionais']
    ]

    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(
        df_filtrado['ano'].astype(str),
        df_filtrado['indicador_despesa_fundeb_profissionais'],
        color=cores
    )

    # Título e eixos
    ax.set_title(f'Despesa com Profissionais da Educação Fundeb - {ente}',
                 color='#FFA07A', fontsize=15)
    ax.set_ylabel('Indicador (%)', color='#FFA07A', fontsize=12)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=10)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Estilo dos ticks
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=12)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=12)

    # Limite do eixo Y
    ax.set_ylim(0, 110)

    # Rótulos de valor nas barras
    for i, valor in enumerate(df_filtrado['indicador_despesa_fundeb_profissionais']):
        if pd.notnull(valor):
            ax.text(
                i,
                valor + 2,
                f'{valor:.1f}%',
                ha='center',
                color='white',
                fontsize=10,
                fontweight='bold'
            )

    fig.tight_layout()
    st.pyplot(fig)

# Gráfico de barras vertical com o indicador de receita não executada
def grafico_percentual_recursos_nao_utilizados(df, ente):
    """
    Gera um gráfico de barras verticais mostrando, ano a ano, o percentual dos recursos
    do Fundeb não utilizados (restos a pagar), para o ente selecionado.
    Utiliza diretamente a coluna 'indicador_receita_nao_aplicada' (valores já percentuais).
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import pandas as pd

    # Filtrar dados
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão robusta
    df_filtrado['indicador_receita_nao_aplicada'] = pd.to_numeric(
        df_filtrado['indicador_receita_nao_aplicada'].astype(str).str.replace(',', '.'),
        errors='coerce'
    )

    # Verificação de dados
    if df_filtrado['indicador_receita_nao_aplicada'].isnull().all():
        st.warning("Não foi possível carregar os percentuais de recursos não utilizados.")
        return

    # Estilo
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 6))

    # Cores condicionais
    cores = [
        '#8B0000' if valor > 10 else '#FFD700'
        for valor in df_filtrado['indicador_receita_nao_aplicada'].fillna(0)
    ]

    bars = ax.bar(
        df_filtrado['ano'].astype(str),
        df_filtrado['indicador_receita_nao_aplicada'],
        color=cores
    )

    # Título e eixos
    ax.set_title(f'Recursos Não Utilizados Fundeb - {ente}',
                 color='#FFA07A', fontsize=15)
    ax.set_ylabel('Percentual (%)', color='#FFA07A', fontsize=10)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=10)

    ax.tick_params(axis='x', colors='#FFA07A', labelsize=12)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=12)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Limite eixo y
    limite_y = max(105, df_filtrado['indicador_receita_nao_aplicada'].max() * 1.2)
    ax.set_ylim(0, limite_y)

    # Rótulos
    for i, valor in enumerate(df_filtrado['indicador_receita_nao_aplicada']):
        if pd.notnull(valor):
            ax.text(
                i,
                valor + (limite_y * 0.02),
                f'{valor:.1f}%',
                ha='center',
                color='white',
                fontsize=10,
                fontweight='bold'
            )

    fig.tight_layout()
    st.pyplot(fig)


# Gráfico de barras para o repasse do Fundeb
def grafico_valor_repasse_fundeb(df, ente):
    """
    Gera um gráfico de barras verticais mostrando a evolução do valor repassado do Fundeb
    ao longo dos anos para o ente federado selecionado, em milhões de reais.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'nome', 'ano' e 'valor_repasse_fundeb'.
    ente : str
        Nome do Município ou Estado selecionado pelo usuário.
    """
   
    # Filtrar dados do ente
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float
    df_filtrado['valor_repasse_fundeb'] = pd.to_numeric(
        df_filtrado['valor_repasse_fundeb'].astype(str).str.replace(',', '.'),
        errors='coerce'
    )

    # Converter para milhões
    df_filtrado['valor_milhoes'] = df_filtrado['valor_repasse_fundeb'] / 1_000_000

    # Estilo do gráfico
    plt.style.use('dark_background')

    # Cor das barras
    cor_barras = '#006400'

    # Criar gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(df_filtrado['ano'].astype(str), df_filtrado['valor_milhoes'], color=cor_barras)

    # Título e eixos
    ax.set_title(f'Evolução do Repasse do Fundeb - {ente}', color='#FFA07A', fontsize=16)
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=10)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=10)

    # Estilo dos eixos
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=12)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=12)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Inserção dos valores no topo das barras
    for i, valor in enumerate(df_filtrado['valor_milhoes']):
        if pd.notnull(valor):
            ax.text(
                i,
                valor + (df_filtrado['valor_milhoes'].max() * 0.02),
                f'R$ {valor:.1f} mi',
                ha='center',
                color='white',
                fontsize=10,
                fontweight='bold'
            )

    fig.tight_layout()
    st.pyplot(fig)

# Grafico de barras complementações
def grafico_complementacoes_fundeb(df, ente):
    """
    Gera um gráfico de barras agrupadas com os valores das complementações do Fundeb
    (VAAF, VAAT, VAAR), ao longo dos anos, para o ente selecionado.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com colunas: 'nome', 'ano', 'valor_receita_vaaf', 'valor_receita_vaat', 'valor_receita_vaar'
    ente : str
        Nome do Município ou Estado selecionado pelo usuário.
    """

    # Filtrar e ordenar os dados
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float
    for col in ['valor_receita_vaaf', 'valor_receita_vaat', 'valor_receita_vaar']:
        df_filtrado[col] = pd.to_numeric(
            df_filtrado[col].astype(str).str.replace(',', '.'),
            errors='coerce'
        ) / 1_000_000  # Converter para milhões

    # Estilo do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 6))

    # Largura e posição das barras agrupadas
    anos = df_filtrado['ano'].astype(str)
    x = np.arange(len(anos))
    largura = 0.25

    # Cores conforme padrão visual
    cor_vaaf = '#006400'   # Verde escuro
    cor_vaat = '#FFA500'   # Laranja
    cor_vaar = '#00BFFF'   # Azul claro

    # Plotagem
    ax.bar(x - largura, df_filtrado['valor_receita_vaaf'], width=largura, label='VAAF', color=cor_vaaf)
    ax.bar(x,            df_filtrado['valor_receita_vaat'], width=largura, label='VAAT', color=cor_vaat)
    ax.bar(x + largura, df_filtrado['valor_receita_vaar'], width=largura, label='VAAR', color=cor_vaar)

    # Título e rótulos
    ax.set_title(f'Complementações do Fundeb por Ano - {ente}', color='#FFA07A', fontsize=16)
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=10)
    ax.set_xlabel('Fonte: Siope', color='#FFA07A', fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(anos)

    # Estilo dos eixos
    ax.tick_params(colors='#FFA07A', labelsize=12)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Legenda
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    fig.tight_layout()
    st.pyplot(fig)

# Gráfico de barras receita impostos
def grafico_valor_receita_impostos(df, ente):
    """
    Gera um gráfico de barras verticais com os valores da receita de impostos
    ao longo dos anos para o ente selecionado.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'nome', 'ano' e 'valor_receita_impostos'.
    ente : str
        Nome do Município ou Estado selecionado pelo usuário.
    """

    # Filtrar e ordenar os dados
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float
    df_filtrado['valor_receita_impostos'] = pd.to_numeric(
        df_filtrado['valor_receita_impostos'].astype(str).str.replace(',', '.'),
        errors='coerce'
    )

    # Converter para milhões
    df_filtrado['valor_milhoes'] = df_filtrado['valor_receita_impostos'] / 1_000_000

    # Estilo
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 6))

    # Cor da barra
    cor_barras = '#006400'

    # Plot
    ax.bar(df_filtrado['ano'].astype(str), df_filtrado['valor_milhoes'], color=cor_barras)

    # Eixos e título
    ax.set_title(f'Total da Receita de Impostos - {ente}', color='#FFA07A', fontsize=16)
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=10)
    ax.set_xlabel('Fonte: Siope', color='#FFA07A', fontsize=10)

    # Estilo dos ticks e spines
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=12)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=12)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Rótulos no topo das barras
    for i, valor in enumerate(df_filtrado['valor_milhoes']):
        if pd.notnull(valor):
            ax.text(
                i,
                valor + (df_filtrado['valor_milhoes'].max() * 0.02),
                f'R$ {valor:.1f} mi',
                ha='center',
                color='white',
                fontsize=10,
                fontweight='bold'
            )

    fig.tight_layout()
    st.pyplot(fig)

# Gráfico de barras agregadas para a receita mínima de impostos
def grafico_valores_despesa_minima_impostos(df, ente):
    """
    Gera um gráfico de barras agrupadas mostrando, por ano, o valor mínimo a ser aplicado em MDE
    e a despesa total liquidada com impostos para o ente selecionado.
    Caso a despesa não atinja o mínimo, a barra de despesa será colorida em vermelho.
    """

    # Filtrar dados do ente
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float e milhões
    for col in ['valor_minimo_mde', 'valor_total_despesa_impostos']:
        df_filtrado[col] = pd.to_numeric(
            df_filtrado[col].astype(str).str.replace(',', '.'),
            errors='coerce'
        ) / 1_000_000

    # Eixo X
    anos = df_filtrado['ano'].astype(str)
    x = np.arange(len(anos))
    largura = 0.35

    # Estilo visual
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 6))

    # Cores
    cor_exigido = '#00BFFF'            # Azul claro
    cor_despesa_ok = '#FFA500'     # Laranja
    cor_despesa_ruim = '#FF0000'   # Vermelho

    # Determinar cores das barras de despesa com base na comparação
    cores_despesa = [
        cor_despesa_ruim if mde > despesa else cor_despesa_ok
        for mde, despesa in zip(df_filtrado['valor_minimo_mde'], df_filtrado['valor_total_despesa_impostos'])
    ]

    # Plotar barras
    ax.bar(x - largura/2, df_filtrado['valor_minimo_mde'], width=largura, label='Mínimo MDE', color=cor_exigido)
    ax.bar(x + largura/2, df_filtrado['valor_total_despesa_impostos'], width=largura, label='Despesa MDE Impostos', color=cores_despesa)

    # Título e eixos
    ax.set_title(f'Mínimo MDE x Despesa MDE Impostos - {ente}', color='#FFA07A', fontsize=16)
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=10)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(anos)

    # Eixos e bordas
    ax.tick_params(colors='#FFA07A', labelsize=12)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite do eixo Y
    valor_maximo = max(df_filtrado[['valor_minimo_mde', 'valor_total_despesa_impostos']].max())
    ax.set_ylim(top=valor_maximo * 1.15)

    # Rótulos dinâmicos nas barras
    for i, (mde, despesa) in enumerate(zip(df_filtrado['valor_minimo_mde'], df_filtrado['valor_total_despesa_impostos'])):
        if pd.notnull(mde):
            ax.text(x[i] - largura/2, mde + valor_maximo * 0.015, f'{mde:.1f}',
                    ha='center', color='white', fontsize=9, fontweight='bold')
        if pd.notnull(despesa):
            ax.text(x[i] + largura/2, despesa + valor_maximo * 0.015, f'{despesa:.1f}',
                    ha='center', color='white', fontsize=9, fontweight='bold')

    # Legenda
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    fig.tight_layout()
    st.pyplot(fig)

def grafico_valores_limite_constitucional(df, ente):
    """
    Gera um gráfico de barras agrupadas mostrando, por ano, o valor mínimo a ser aplicado em MDE
    e a despesa total liquidada com impostos para o ente selecionado.
    Caso a despesa não atinja o mínimo, a barra de despesa será colorida em vermelho.
    """

    # Filtrar dados do ente
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float e milhões
    for col in ['valor_limite_const_exigido', 'valor_limite_const_aplicado']:
        df_filtrado[col] = pd.to_numeric(
            df_filtrado[col].astype(str).str.replace(',', '.'),
            errors='coerce'
        ) / 1_000_000

    # Eixo X
    anos = df_filtrado['ano'].astype(str)
    x = np.arange(len(anos))
    largura = 0.35

    # Estilo visual
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 6))

    # Cores
    cor_exigido = '#00BFFF'            # Azul claro
    cor_despesa_ok = '#FFA500'     # Laranja
    cor_despesa_ruim = '#FF0000'   # Vermelho

    # Determinar cores das barras de despesa com base na comparação
    cores_despesa = [
        cor_despesa_ruim if mde > despesa else cor_despesa_ok
        for mde, despesa in zip(df_filtrado['valor_limite_const_exigido'], df_filtrado['valor_limite_const_aplicado'])
    ]

    # Plotar barras
    ax.bar(x - largura/2, df_filtrado['valor_limite_const_exigido'], width=largura, label='Mínimo Constitucional exigido', color=cor_exigido)
    ax.bar(x + largura/2, df_filtrado['valor_limite_const_aplicado'], width=largura, label='Investimento total em MDE', color=cores_despesa)

    # Título e eixos
    ax.set_title(f'Investimento Mínimo Constitucional - {ente}', color='#FFA07A', fontsize=16)
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=10)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(anos)

    # Eixos e bordas
    ax.tick_params(colors='#FFA07A', labelsize=12)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite do eixo Y
    valor_maximo = max(df_filtrado[['valor_limite_const_exigido', 'valor_limite_const_aplicado']].max())
    ax.set_ylim(top=valor_maximo * 1.15)

    # Rótulos dinâmicos nas barras
    for i, (mde, despesa) in enumerate(zip(df_filtrado['valor_limite_const_exigido'], df_filtrado['valor_limite_const_aplicado'])):
        if pd.notnull(mde):
            ax.text(x[i] - largura/2, mde + valor_maximo * 0.015, f'{mde:.1f}',
                    ha='center', color='white', fontsize=9, fontweight='bold')
        if pd.notnull(despesa):
            ax.text(x[i] + largura/2, despesa + valor_maximo * 0.015, f'{despesa:.1f}',
                    ha='center', color='white', fontsize=9, fontweight='bold')

    # Legenda
    ax.legend(loc='upper left', frameon=False, fontsize=10)

    fig.tight_layout()
    st.pyplot(fig)

def grafico_indicador_limite_constitucional(df, ente):
    """
    Gera um gráfico de barras verticais mostrando a evolução do indicador de gastos com 
    a remuneração dos profissionais da educação, ao longo dos anos, para o ente selecionado.
    """


    # Filtrar dados do ente
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float
    df_filtrado['indicador_limite_constitucional'] = pd.to_numeric(
        df_filtrado['indicador_limite_constitucional'].astype(str).str.replace(',', '.'),
        errors='coerce'
    )

    # Estilo do gráfico
    plt.style.use('dark_background')

    # Definir cores condicionais por linha
    cores = [
        '#8B0000' if valor < 25 else '#006400'
        for valor in df_filtrado['indicador_limite_constitucional']
    ]

    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(
        df_filtrado['ano'].astype(str),
        df_filtrado['indicador_limite_constitucional'],
        color=cores
    )

    # Título e eixos
    ax.set_title(f'Indicador do Mínimo Constitucional - {ente}',
                 color='#FFA07A', fontsize=15)
    ax.set_ylabel('Indicador (%)', color='#FFA07A', fontsize=12)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=10)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Estilo dos ticks
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=12)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=12)

    # Limite do eixo Y
    ax.set_ylim(0, 110)

    # Rótulos de valor nas barras
    for i, valor in enumerate(df_filtrado['indicador_limite_constitucional']):
        if pd.notnull(valor):
            ax.text(
                i,
                valor + 2,
                f'{valor:.1f}%',
                ha='center',
                color='white',
                fontsize=10,
                fontweight='bold'
            )

    fig.tight_layout()
    st.pyplot(fig)


def grafico_receita_salario_educacao_ano(df, ano):
    """
    Gera um gráfico de barras horizontal com o total de receita do Salário-Educação por Município e Estado, para o ano selecionado.
    Os valores são convertidos e apresentados em milhões de reais (R$ mi).

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'nome', 'ano' e 'valor_receita_salario_educacao'.
    ano : int
        Ano selecionado pelo usuário na interface Streamlit.
    """
    # Filtra e ordena os dados
    df_filtrado = df[df['ano'] == ano].copy()
    df_filtrado.sort_values(by='valor_receita_salario_educacao', ascending=True, inplace=True)

    # Conversão para milhões
    df_filtrado['valor_milhoes'] = df_filtrado['valor_receita_salario_educacao'] / 1_000_000

    # Gradiente de verde (verde claro -> verde escuro)
    cmap = mcolors.LinearSegmentedColormap.from_list('verde_gradiente', ['#90ee90', '#006400'])
    norm = plt.Normalize(vmin=df_filtrado['valor_milhoes'].min(),
                         vmax=df_filtrado['valor_milhoes'].max())
    cores = [cmap(norm(v)) for v in df_filtrado['valor_milhoes']]

    # Estilo escuro
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, max(6, 0.48 * len(df_filtrado))))

    # Gráfico
    ax.barh(df_filtrado['nome'], df_filtrado['valor_milhoes'], color=cores)

    # Título e eixos
    ax.set_title('Total da Receita do Salário-Educação (R$ milhões)', color='#FFA07A', fontsize=23)
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=15)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=15)
    # Estilo dos ticks e spines
    ax.tick_params(colors='#FFA07A', labelsize=20)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Limite dinâmico do eixo X
    max_valor = df_filtrado['valor_milhoes'].max()
    limite_superior = max_valor * 1.3
    ax.set_xlim(right=limite_superior)
    
    # Reduz o espaçamento superior e inferior
    n_barras = len(df_filtrado)
    ax.set_ylim(-0.7, n_barras - 0.3)


    # Alinha o spine direito com o limite superior dinâmico
    ax.spines['right'].set_position(('data', limite_superior * 1))  # ajusta a posição do spine direito para o limite superior + 2%
    
    # Inserir rótulos nas barras (em milhões com uma casa decimal)
    for i, valor in enumerate(df_filtrado['valor_milhoes']):
        deslocamento = limite_superior * 0.01
        ax.text(valor + deslocamento, i, f"R$ {valor:,.1f} mi",
                color='white', va='center', fontsize=17, fontweight='bold')

    fig.tight_layout()
    st.pyplot(fig)

#Gráfico de barras Salário Educação
def grafico_receita_salario_educacao_ente(df, ente):
    """
    Gera um gráfico de barras verticais mostrando, por ano, a receita do salário educação
    para o ente selecionado, com altura dinâmica e rótulos bem posicionados.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com as colunas 'nome', 'ano', 'valor_receita_salario_educacao'.
    ente : str
        Nome do Município ou Estado selecionado.
    """

    # Filtrar dados do ente
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float (milhões)
    df_filtrado['valor_receita_salario_educacao'] = pd.to_numeric(
        df_filtrado['valor_receita_salario_educacao'].astype(str).str.replace(',', '.'),
        errors='coerce'
    ) / 1_000_000

    # Eixo X e valores
    anos = df_filtrado['ano'].astype(str)
    valores = df_filtrado['valor_receita_salario_educacao']
    x = np.arange(len(anos))

    # Estilo
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(7, 6.45))

    # Cor padrão do projeto
    cor_verde = '#006400'

    # Plotar barras
    ax.bar(anos, valores, color=cor_verde)

    # Título e eixos
    ax.set_title(f'Receita do Salário-Educação - {ente}', color='#FFA07A', fontsize=14)
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=9)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=9)

    # Estilo dos eixos
    ax.tick_params(colors='#FFA07A', labelsize=11)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Limite dinâmico do eixo Y
    valor_maximo = valores.max()
    ax.set_ylim(top=valor_maximo * 1.15)

    # Rótulos no topo das barras com deslocamento proporcional
    for i, valor in enumerate(valores):
        if pd.notnull(valor):
            ax.text(
                i,
                valor + valor_maximo * 0.015,
                f'R$ {valor:.1f} mi',
                ha='center',
                color='white',
                fontsize=10,
                fontweight='bold'
            )

    fig.tight_layout()
    st.pyplot(fig)

# Gráfico de barras horizontal de outras receitas
def grafico_receitas_adicionais_por_ente_ano(df, ente, ano):
    """
    Gera um gráfico de barras horizontais com as receitas adicionais por tipo,
    para um determinado ente e ano.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas de receitas adicionais e identificação por ente e ano.
    ente : str
        Nome do ente (município ou estado).
    ano : int
        Ano de referência dos dados.
    """

    # Lista de colunas que serão exibidas no gráfico
    colunas_receitas = [
        "valor_receita_pdde",
        "valor_receita_pnae",
        "valor_receita_pnate",
        "valor_receita_outras_fnde",
        "valor_receita_convenios",
        "valor_receita_royalties",
        "valor_receita_operacao_credito",
        "valor_receita_outras_outras"
    ]

    # Filtrar o DataFrame
    df_filtrado = df[(df["nome"] == ente) & (df["ano"] == ano)]

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para o ente '{ente}' no ano {ano}.")
        return

    # Selecionar apenas as colunas de interesse
    df_valores = df_filtrado[colunas_receitas].T.copy()
    df_valores.columns = ["valor"]
    df_valores["valor_mi"] = df_valores["valor"] / 1_000_000

    # Renomear para nomes amigáveis
    df_valores["fonte"] = df_valores.index.map(lambda col: COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO.get(col, col))

    # Ordenar valores crescentes
    df_valores = df_valores.sort_values(by="valor_mi", ascending=True)

    # Gradiente verde → branco
    cor_inicio = "#FFFFFF"
    cor_fim = "#006400"
    cmap = mcolors.LinearSegmentedColormap.from_list("verde_para_branco", [cor_inicio, cor_fim])
    norm = mcolors.Normalize(vmin=df_valores["valor_mi"].min(), vmax=df_valores["valor_mi"].max())
    cores = [cmap(norm(v)) for v in df_valores["valor_mi"]]

    # Estilo escuro
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, 7))

    ax.barh(df_valores["fonte"], df_valores["valor_mi"], color=cores)

    # Estilo do gráfico
    ax.set_title(f"Receitas Adicionais da Educação - {ente} ({ano})", color="#FFA07A", fontsize=18)
    ax.set_xlabel("Fonte: SIOPE", color="#FFA07A", fontsize=11)
    ax.set_ylabel("Valor em milhões de R$ (mi)", color="#FFA07A", fontsize=11)

    # Ticks e spines
    ax.tick_params(colors='#FFA07A', labelsize=14)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Espaço para rótulos
    max_valor = df_valores["valor_mi"].max()
    ax.set_xlim(0, max_valor * 1.15)

    for i, valor in enumerate(df_valores["valor_mi"]):
        ax.text(valor + (max_valor * 0.01), i, f"R${valor:.2f}mi", color="white", va="center", fontweight='bold', fontsize=10)

    fig.tight_layout(pad=2.0)
    st.pyplot(fig)

def grafico_receitas_adicionais_evolucao(df, ente, categoria):
    """
    Gera um gráfico de barras verticais com a evolução temporal de uma receita adicional específica.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo colunas de receitas adicionais e identificação por ente e ano.
    ente : str
        Nome do ente (município ou estado).
    categoria : str
        Nome da coluna da categoria de receita adicional (ex: 'valor_receita_pdde').
    """
    # Lista de categorias válidas
    colunas_receitas = [
        "valor_receita_pdde",
        "valor_receita_pnae",
        "valor_receita_pnate",
        "valor_receita_outras_fnde",
        "valor_receita_convenios",
        "valor_receita_royalties",
        "valor_receita_operacao_credito",
        "valor_receita_outras_outras"
    ]

    if categoria not in colunas_receitas:
        st.error(f"A categoria '{categoria}' não é reconhecida como uma receita adicional válida.")
        return

    # Filtrar o DataFrame
    df_filtrado = df[df["nome"] == ente][["ano", categoria]].copy()

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para o ente '{ente}'.")
        return

    # Conversão para milhões
    df_filtrado["valor_mi"] = df_filtrado[categoria] / 1_000_000
    df_filtrado["ano_str"] = df_filtrado["ano"].astype(str)
    df_filtrado = df_filtrado.sort_values(by="ano")

    # Nome legível da categoria
    nome_legivel = COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO.get(categoria, categoria)

    # Estilo e figura
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, 7))

    # Plot
    bars = ax.bar(df_filtrado["ano_str"], df_filtrado["valor_mi"], color="#006400")

    # Rótulos no topo
    for bar in bars:
        altura = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            altura + 0.03,
            f"R$ {altura:.2f} mi",
            ha='center',
            va='bottom',
            color="white",
            fontweight='bold',
            fontsize=13
        )

    # Título e eixos
    ax.set_title(f"Evolução da Receita de {nome_legivel} - {ente}", color="#FFA07A", fontsize=18)
    ax.set_ylabel("Valor em milhões de R$ (mi)", color="#FFA07A", fontsize=11)
    ax.set_xlabel("Fonte: SIOPE", color="#FFA07A", fontsize=11)

    # Estilo dos eixos
    ax.tick_params(colors='#FFA07A', labelsize=14)
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Ajustar eixo y com epsilon e mínimo de 1.0
    y_max = max(df_filtrado["valor_mi"].max(), 1.0)
    ax.set_ylim(0.001, y_max * 1.15)

    fig.tight_layout(pad=2.0)
    st.pyplot(fig)

def grafico_execucao_pdde_valores(df, ano, ente):
    """
    Gera um gráfico de barras verticais comparando saldos disponibilizado, executado e não utilizado
    para um determinado ente e ano.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'ano', 'nome', 'saldo_disponibilizado',
        'saldo_executado', 'saldo_nao_utilizado'
    ano : int
        Ano de referência
    ente : str
        Nome do município ou estado
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Filtrar o DataFrame
    df_filtrado = df[(df["ano"] == ano) & (df["nome"] == ente)]

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para {ente} no ano de {ano}.")
        return

    # Valores em milhões
    valores_mi = [
        df_filtrado["saldo_disponibilizado"].values[0] / 1_000_000,
        df_filtrado["saldo_executado"].values[0] / 1_000_000,
        df_filtrado["saldo_nao_utilizado"].values[0] / 1_000_000
    ]
    categorias = ["Disponibilizado", "Executado", "Não utilizado"]
    cores = ["#4682B4", "#006400", "#FFA500"]  # azul, verde, laranja

    # Estilo
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(8, 5.5))

    # Plot
    bars = ax.bar(categorias, valores_mi, color=cores)
    
    # Ajuste de altura do eixo Y
    y_max = max(valores_mi)
    ax.set_ylim(0, y_max * 1.2)


    # Rótulos
    for bar, valor in zip(bars, valores_mi):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(valores_mi) * 0.03,
            f"R$ {valor:.2f} mi",
            ha="center",
            va="bottom",
            color="white",
            fontweight='bold',
            fontsize=11
        )

    # Título e eixos
    ax.set_title(f"Execução dos Recursos do PDDE - {ente} ({ano})", color="#FFA07A", fontsize=14)
    ax.set_ylabel("Valor em milhões de R$ (mi)", color="#FFA07A", fontsize=10)
    ax.set_xlabel("Fonte: Painel de Monitoramento do PDDE - FNDE", color="#FFA07A", fontsize=10)

    # Estilo dos eixos
    ax.tick_params(axis="x", colors="#FFA07A", labelsize=12)
    ax.tick_params(axis="y", colors="#FFA07A")
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    # Legenda
    ax.legend(bars, categorias, loc="upper right", frameon=False, labelcolor="white")

    fig.tight_layout()
    st.pyplot(fig)

def grafico_execucao_pdde_porcentagem(df, ano):
    """
    Gera um gráfico de barras horizontais com a porcentagem de execução dos recursos do PDDE
    para todos os entes em um determinado ano.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'ano', 'nome', e 'porcentagem_execucao' (0.00 a 1.00).
    ano : int
        Ano de referência
    """
    
    # Filtrar por ano
    df_filtrado = df[df["ano"] == ano][["nome", "porcentagem_execucao"]].dropna()

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para o ano de {ano}.")
        return

    # Ordenar por porcentagem crescente
    df_filtrado = df_filtrado.sort_values(by="porcentagem_execucao", ascending=True)

    # Gradiente verde → vermelho
    cmap = mcolors.LinearSegmentedColormap.from_list("verde_vermelho", ["#8B0000", "#006400",])
    norm = mcolors.Normalize(vmin=0, vmax=1)
    cores = [cmap(norm(v)) for v in df_filtrado["porcentagem_execucao"]]

    # Estilo e plot
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, 8))

    ax.barh(df_filtrado["nome"], df_filtrado["porcentagem_execucao"] * 100, color=cores)

    # Rótulos nas barras
    for i, valor in enumerate(df_filtrado["porcentagem_execucao"]):
        ax.text(
            valor * 100 + 1,
            i,
            f"{valor * 100:.1f}%",
            va="center",
            color="white",
            fontweight='bold',
            fontsize=10
        )

    # Estilo dos eixos
    ax.set_title(f"Execução Percentual dos Recursos do PDDE - {ano}", color="#FFA07A", fontsize=18)
    ax.set_ylabel("Porcentagem de Execução (%)", color="#FFA07A", fontsize=12)
    ax.set_xlabel("Fonte: Painel de Monitoramento do PDDE - FNDE", color="#FFA07A", fontsize=12)
    
    ax.tick_params(colors="#FFA07A", labelsize=13)
    
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_xlim(0, 100)  # de 0% a 100%
    fig.tight_layout()
    st.pyplot(fig)

def grafico_receita_total_educacao(df, ente):
    """
    Gera gráfico de barras verticais com a receita total para educação ao longo dos anos
    para o ente selecionado, com barras no tom verde padrão do projeto.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com colunas: 'ano', 'nome', 'valor_total_receita_educacao'
    ente : str
        Nome do município ou estado
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import pandas as pd

    # Filtrar dados
    df_filtrado = df[df["nome"] == ente].copy()
    df_filtrado = df_filtrado.sort_values(by="ano")

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para o ente '{ente}'.")
        return

    # Conversão segura dos valores
    df_filtrado["valor_total_receita_educacao"] = pd.to_numeric(
        df_filtrado["valor_total_receita_educacao"].astype(str).str.replace(",", "."),
        errors="coerce"
    )

    # Em milhões
    df_filtrado["valor_mi"] = df_filtrado["valor_total_receita_educacao"] / 1_000_000

    # Estilo
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, 7))

    cor_verde = "#006400"
    bars = ax.bar(df_filtrado["ano"].astype(str), df_filtrado["valor_mi"], color=cor_verde)

    # Rótulos nas barras
    for bar, valor in zip(bars, df_filtrado["valor_mi"]):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + max(df_filtrado["valor_mi"]) * 0.02,
            f"R$ {valor:.1f} mi",
            ha="center",
            color="white",
            fontweight="bold",
            fontsize=13
        )

    # Título e eixos
    ax.set_title(f"Receita Total para Educação - {ente}", color="#FFA07A", fontsize=18)
    ax.set_ylabel("Valor em milhões de R$ (mi)", color="#FFA07A", fontsize=11)
    ax.set_xlabel("Fonte: SIOPE", color="#FFA07A", fontsize=11)

    ax.tick_params(colors='#FFA07A', labelsize=13)    
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    ax.set_ylim(0, df_filtrado["valor_mi"].max() * 1.25)

    fig.tight_layout()
    st.pyplot(fig)


#==========================
# PAGINA PANORAMA ÁGUA
#==========================
    
def grafico_agua_dados_brutos(df, ano_censo):
    """
    Gera um gráfico de barras verticais mostrando o total de escolas
    que fornecem ou não fornecem água potável em determinado ano.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'NU_ANO_CENSO' e 'IN_AGUA_POTAVEL'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário.
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Filtrar DataFrame pelo ano
    df_filtrado = df[df["NU_ANO_CENSO"] == ano_censo]

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para o ano {ano_censo}.")
        return

    # Contagem das respostas
    contagem = df_filtrado["IN_AGUA_POTAVEL"].value_counts().sort_index(ascending=False)
    contagem.index = contagem.index.map({1: "Fornece", 0: "Não Fornece"})

    # Cores fixas conforme solicitado
    cores = ["#B0E0E6" if idx == "Fornece" else "#FFC107" for idx in contagem.index]

    # Estilo escuro
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(8, 6))

    # Barras
    bars = ax.bar(contagem.index, contagem.values, color=cores)

    # Inserir valores nas barras
    for i, valor in enumerate(contagem.values):
        ax.text(
            i,
            valor + (contagem.max() * 0.02),
            str(valor),
            ha="center",
            color="white",
            fontweight="bold",
            fontsize=14
        )

    # Título e eixos
    ax.set_title(f"Fornecimento de Água Potável ({ano_censo})", color="#FFA07A", fontsize=20)
    ax.set_ylabel("Número de Escolas", color="#FFA07A", fontsize=12)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    # Estilo dos ticks
    ax.tick_params(axis="x", colors="#FFA07A", labelsize=14)
    ax.tick_params(axis="y", colors="#FFA07A", labelsize=14)

    ax.set_ylim(0, contagem.max() * 1.2)

    fig.tight_layout()
    st.pyplot(fig)




#===========================
# PAGINA POVOS TRADICIONAIS
#===========================
# Função gráfico de barras total de matriculas por localizacao diferenciada
def grafico_matriculas_por_localizacao_diferenciada(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de matriculas por localizacao diferenciada.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_LOCALIZACAO_DIFERENCIADA', 'QT_MAT_BAS' e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    from matplotlib.ticker import MaxNLocator
    
    # Filtra o DataFrame pelo ano selecionado
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) & 
        (df['TP_LOCALIZACAO_DIFERENCIADA'] != 0) & 
        (df['TP_LOCALIZACAO_DIFERENCIADA'].notnull())
    ]
    
    # Agrupa por Localização e soma os matriculas
    localizacao_counts = df_filtrado.groupby('TP_LOCALIZACAO_DIFERENCIADA')['QT_MAT_BAS'].sum().sort_index().astype(int)
    localizacao_counts.index = localizacao_counts.index.map({1: 'Assentamento', 2: 'Terra Indígena', 3: 'Quilombola', 8: 'Com. Tradicionais'})
    
    # Cores fixas opacas por categoria
    cores_localizacao = {
        'Assentamento': '#1FB029',
        'Terra Indígena': '#C0C0C0',
        'Quilombola': '#FFA07A',
        'Com. Tradicionais': '#FF6347'
    }
    
    cores_localizacao = [cores_localizacao[r] for r in localizacao_counts.index]
    
    # Estilo escuro
    plt.style.use('dark_background')
    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores_localizacao)
    # Título e rótulos
    ax.set_title('Total de matriculas por Localização Diferenciada', color='#FFA07A', fontsize=25)
    # ax.set_ylabel('Número de matriculas', color='#FFA07A', fontsize=14)
    # ax.set_xlabel('Localização', color='#FFA07A', fontsize=14)
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    # Ticks
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    # Inserir valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
    fig.tight_layout()
    st.pyplot(fig)
  
# Função gráfico de barras total de escolas por localizacao diferenciada
def grafico_escolas_por_localizacao_diferenciada(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de escolas por localizacao diferenciada.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_LOCALIZACAO_DIFERENCIADA', e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    from matplotlib.ticker import MaxNLocator

    # Filtra o DataFrame pelo ano selecionado
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) & 
        (df['TP_LOCALIZACAO_DIFERENCIADA'] != 0) & 
        (df['TP_LOCALIZACAO_DIFERENCIADA'].notnull())
    ]

    # Agrupa por Localização e conta as escolas
    localizacao_counts = df_filtrado['TP_LOCALIZACAO_DIFERENCIADA'].value_counts().sort_index()
    localizacao_counts.index = localizacao_counts.index.map({1: 'Assentamento', 2: 'Terra Indígena', 3: 'Quilombola', 8: 'Com. Tradicionais'})

    # Cores fixas opacas por categoria
    cores_localizacao = {
        'Assentamento': '#1FB029',
        'Terra Indígena': '#C0C0C0',
        'Quilombola': '#FFA07A',
        'Com. Tradicionais': '#FF6347'
    }
    
    cores_localizacao = [cores_localizacao[r] for r in localizacao_counts.index]
    
    # Estilo escuro
    plt.style.use('dark_background')
    
    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores_localizacao)
    
    # Título e rótulos
    ax.set_title('Total de Escolas por Localização Diferenciada', color='#FFA07A', fontsize=25)
    # ax.set_ylabel('Número de Escolas', color='#FFA07A', fontsize=14)
    # ax.set_xlabel('Localização', color='#FFA07A', fontsize=14)
    
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    
    # Ticks
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)
    
    # Inserir valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
    
    fig.tight_layout()
    st.pyplot(fig)
    
# Função para gráfico de barras total de escolas por localizacao diferenciada, por município
def grafico_escolas_por_localizacao_diferenciada_municipio(df, ano_censo, municipio):
    """
    Gera um gráfico de barras verticais com o total de escolas por localização diferenciada.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'TP_LOCALIZACAO_DIFERENCIADA', e 'NU_ANO_CENSO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Filtra o DataFrame pelo ano e município selecionados
    df_filtrado = df[
        (df['TP_LOCALIZACAO_DIFERENCIADA'] != 0) &
        (df['TP_LOCALIZACAO_DIFERENCIADA'].notnull()) &
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    # Agrupa por Localização e conta as escolas
    localizacao_counts = df_filtrado['TP_LOCALIZACAO_DIFERENCIADA'].value_counts().sort_index()
    localizacao_counts.index = localizacao_counts.index.map({1: 'Assentamento', 2: 'Terra Indígena', 3: 'Quilombola', 8: 'Com. Tradicionais'})

    # Cores fixas opacas por categoria
    cores_localizacao = {
        'Assentamento': '#1FB029',
        'Terra Indígena': '#C0C0C0',
        'Quilombola': '#FFA07A',
        'Com. Tradicionais': '#FF6347'
    }
    
    cores_localizacao = [cores_localizacao[r] for r in localizacao_counts.index]
    
    # Estilo escuro
    plt.style.use('dark_background')

    # Criação do gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores_localizacao)

    # Título e rótulos
    ax.set_title(f'Total de Escolas por Localização Diferenciada em {municipio}', color='#FFA07A', fontsize=25)
    
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    # Ticks
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=20)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=20)
    # Inserir valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
    fig.tight_layout()
    st.pyplot(fig)


