
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import streamlit as st
import numpy as np
from utils import COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO

#============================
# PAGINA PANORAMA GERAL
#=============================

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

    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

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

    ax.set_title('Total de matrículas por Município', color='#FFA07A', fontsize=40)

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    ax.tick_params(axis='x', colors='#FFA07A', labelsize=25)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=25)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1000)}mil'))
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=17)

    # Valores nas barras com base mil
    for i, valor in enumerate(resultado_matriculas):
        ax.text(valor + (resultado_matriculas.max() * 0.01), i, f'{int(valor/1000)}', va='center',
                color='white', fontweight='bold', fontsize=22)

    fig.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    resultado_escolas = df_filtrado.groupby('NO_MUNICIPIO')['CO_ENTIDADE'].count().sort_values(ascending=True)
    
    # Gradiente de cores
    cmap = mcolors.LinearSegmentedColormap.from_list('custom_gradient', ['#B0E0E6', '#FFC107'])
    norm = plt.Normalize(vmin=resultado_escolas.min(), vmax=resultado_escolas.max())
    cores = [cmap(norm(valor)) for valor in resultado_escolas]

    # Gráfico total de escolas por Município
    plt.style.use('dark_background')
    
    fig, ax = plt.subplots(figsize=(15, max(8, 0.5 * len(resultado_escolas))))
    bars = ax.barh(resultado_escolas.index, resultado_escolas.values, color=cores)
    
    # Ajusta dinamicamente o limite superior do eixo X com uma folga de 10%
    limite_superior = resultado_escolas.max() * 1.1
    ax.set_xlim(right=limite_superior)

    
    # Título e rótulos
    ax.set_title('Total de Escolas por Município', color='#FFA07A', fontsize=40)
    ax = plt.gca()
    
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
        
    plt.xticks(color='#FFA07A', fontsize=25)
    plt.yticks(color='#FFA07A', fontsize=25)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=17)
    
    # Valores nas barras
    for i, valor in enumerate(resultado_escolas):
        plt.text(valor + (resultado_escolas.max() * 0.01), i, str(valor), va='center',
                 color='white', fontweight='bold', fontsize=22)
    
    plt.tight_layout()
    st.pyplot(plt)

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
    
    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    dependencia_counts = df_filtrado.groupby('TP_DEPENDENCIA')['QT_MAT_BAS'].sum().sort_index().astype(int)
    dependencia_counts.index = dependencia_counts.index.map({1: 'Federal', 2: 'Estadual', 3: 'Municipal'})

    # Cores fixas opacas por categoria (RGBA)
    cores_localizacao = {
        'Federal': (0/255, 191/255, 255/255, 0.7),     # Azul celeste com 70% opacidade
        'Estadual': (255/255, 160/255, 122/255, 0.7),  # Salmão com 70% opacidade
        'Municipal': (118/255, 238/255, 0/255, 0.7)     # Verde fosforescente com 70% opacidade
    }
   
    cores = [cores_localizacao[r] for r in dependencia_counts.index]

    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(dependencia_counts.index, dependencia_counts.values, color=cores)

    ax.set_title(f'Total de matrículas por Dependência Administrativa', color='#FFA07A', fontsize=23)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)
    
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    ax.set_ylim(0, dependencia_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=15)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    
    # Valores nas barras
    for i, valor in enumerate(dependencia_counts):
        ax.text(i, valor + max(dependencia_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)
    
    fig.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    dependencia_counts = df_filtrado['TP_DEPENDENCIA'].value_counts().sort_index()
    dependencia_counts.index = dependencia_counts.index.map({1: 'Federal', 2: 'Estadual', 3: 'Municipal'})

    # Cores fixas opacas por categoria (RGBA)
    cores_localizacao = {
        'Federal': (0/255, 191/255, 255/255, 0.7),     # Azul celeste com 70% opacidade
        'Estadual': (255/255, 160/255, 122/255, 0.7),  # Salmão com 70% opacidade
        'Municipal': (118/255, 238/255, 0/255, 0.7)     # Verde fosforescente com 70% opacidade
    }
   
    cores = [cores_localizacao[r] for r in dependencia_counts.index]

    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(dependencia_counts.index, dependencia_counts.values, color=cores)

    ax.set_title('Total de Escolas por Dependência Administrativa', color='#FFA07A', fontsize=23)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)
    
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    ax.set_ylim(0, dependencia_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=17)

    # Valores nas barras
    for i, valor in enumerate(dependencia_counts):
        ax.text(i, valor + max(dependencia_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=14)

    fig.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    dependencia_counts = df_filtrado.groupby('TP_DEPENDENCIA')['QT_MAT_BAS'].sum().sort_index().astype(int)
    dependencia_counts.index = dependencia_counts.index.map({1: 'Federal', 2: 'Estadual', 3: 'Municipal'})

    # Cores fixas opacas por categoria (RGBA)
    cores_localizacao = {
        'Federal': (0/255, 191/255, 255/255, 0.7),     # Azul celeste com 70% opacidade
        'Estadual': (255/255, 160/255, 122/255, 0.7),  # Salmão com 70% opacidade
        'Municipal': (118/255, 238/255, 0/255, 0.7)     # Verde fosforescente com 70% opacidade
    }
   
    cores = [cores_localizacao[r] for r in dependencia_counts.index]

    plt.style.use('dark_background')

    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(dependencia_counts.index, dependencia_counts.values, color=cores)

    ax.set_title(f'Total de matrículas por Dep. Administrativa - {municipio} ({ano_censo})', color='#FFA07A', fontsize=19)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    
    ax.set_ylim(0, dependencia_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=15)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
        
    # Valores nas barras
    for i, valor in enumerate(dependencia_counts):
        ax.text(i, valor + max(dependencia_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=17)
    
    fig.tight_layout()
    st.pyplot(fig)

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
    
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]
    
    dependencia_counts = df_filtrado['TP_DEPENDENCIA'].value_counts().sort_index()
    dependencia_counts.index = dependencia_counts.index.map({1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    
    # Cores fixas opacas por categoria (RGBA)
    cores_localizacao = {
        'Federal': (0/255, 191/255, 255/255, 0.7),     # Azul celeste com 50% opacidade
        'Estadual': (255/255, 160/255, 122/255, 0.7),  # Salmão com 50% opacidade
        'Municipal': (118/255, 238/255, 0/255, 0.7)     # Verde fosforescente com 50% opacidade
    }
    
    cores = [cores_localizacao[r] for r in dependencia_counts.index]
    
    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.bar(dependencia_counts.index, dependencia_counts.values, color=cores)
    
    ax.set_title(f'Total de Escolas por Dep. Administrativa - {municipio} ({ano_censo})', color='#FFA07A', fontsize=19)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
        
    ax.set_ylim(0, dependencia_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=15)
    

    # Valores nas barras
    for i, valor in enumerate(dependencia_counts):
        ax.text(i, valor + max(dependencia_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=17)
        
    fig.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    localizacao_counts = df_filtrado.groupby('TP_LOCALIZACAO')['QT_MAT_BAS'].sum().sort_index().astype(int)
    localizacao_counts.index = localizacao_counts.index.map({1: 'Urbana', 2: 'Rural'})

    cores_localizacao = {
        'Rural': '#1FB029',
        'Urbana': '#C0C0C0'
    }
  
    cores = [cores_localizacao[r] for r in localizacao_counts.index]



    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores)

    # Título e rótulos
    ax.set_title('Total de matrículas por Localização', color='#FFA07A', fontsize=25)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)
    
    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    
    # Ticks
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=15)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    
    # Inserir valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=16)
    fig.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    localizacao_counts = df_filtrado['TP_LOCALIZACAO'].value_counts().sort_index()
    localizacao_counts.index = localizacao_counts.index.map({1: 'Urbana', 2: 'Rural'})

    cores_localizacao = {
        'Rural': '#1FB029',
        'Urbana': '#C0C0C0'
    }
   
    cores = [cores_localizacao[r] for r in localizacao_counts.index]

    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores)

    # Título e rótulos
    ax.set_title('Total de Escolas por Localização', color='#FFA07A', fontsize=25)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)
    
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=15)
    
    # Valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=16)
    
    fig.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    localizacao_counts = df_filtrado.groupby('TP_LOCALIZACAO')['QT_MAT_BAS'].sum().sort_index().astype(int)
    localizacao_counts.index = localizacao_counts.index.map({1: 'Urbana', 2: 'Rural'})

    cores_localizacao = {
        'Rural': '#1FB029',
        'Urbana': '#C0C0C0'
    }

    cores = [cores_localizacao[r] for r in localizacao_counts.index]



    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores)

    ax.set_title(f'Total de matrículas por Localização - {municipio} ({ano_censo})', color='#FFA07A', fontsize=19)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    
    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=15)
    
    # Definindo o número de ticks no eixo y
    ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
    # Inserir valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=16)
    fig.tight_layout()
    st.pyplot(fig)

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
    
    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio) &
        (df['TP_LOCALIZACAO'].notnull())
    ]

    localizacao_counts = df_filtrado['TP_LOCALIZACAO'].value_counts().sort_index()
    localizacao_counts.index = localizacao_counts.index.map({1: 'Urbana', 2: 'Rural'})

    cores_localizacao = {
        'Rural': '#1FB029',
        'Urbana': '#C0C0C0'
    }
    cores = [cores_localizacao[r] for r in localizacao_counts.index]

    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(localizacao_counts.index, localizacao_counts.values, color=cores)

    ax.set_title(f'Total de Escolas por Localização - {municipio} ({ano_censo})', color='#FFA07A', fontsize=19)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    ax.set_ylim(0, localizacao_counts.max() * 1.1)
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=15)

    # Valores nas barras
    for i, valor in enumerate(localizacao_counts):
        ax.text(i, valor + max(localizacao_counts) * 0.02, str(valor), ha='center',
                color='white', fontweight='bold', fontsize=16)

    fig.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    agrupado = df_filtrado.groupby(['TP_DEPENDENCIA', 'TP_LOCALIZACAO'])['QT_MAT_BAS'].sum().unstack(fill_value=0)
    agrupado = agrupado.rename(index={1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    agrupado = agrupado.rename(columns={1: 'Urbana', 2: 'Rural'})

    categorias = agrupado.index.tolist()
    urbana = agrupado['Urbana']
    rural = agrupado['Rural']
    x = np.arange(len(categorias))
    largura = 0.35

    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Barra dupla e Legenda
    ax.bar(x - largura/2, urbana, width=largura, label='Urbana', color='#C0C0C0')
    ax.bar(x + largura/2, rural, width=largura, label='Rural', color='#1FB029')

    ax.set_title(f'Total de matrículas por Dependência e Localização - ({ano_censo})', color='#FFA07A', fontsize=20)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)
    
    ax.set_xticks(x)
    ax.set_xticklabels(categorias, color='#FFA07A', fontsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=14)
    ax.legend()

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite superior responsivo
    limite_superior = max(urbana.max(), rural.max()) * 1.15
    ax.set_ylim(0, limite_superior)

    # Valores nas barras com espaçamento dinâmico
    espaco_texto = limite_superior * 0.015
    for i in range(len(categorias)):
        ax.text(x[i] - largura/2, urbana[i] + espaco_texto, f'{urbana[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=15)
        ax.text(x[i] + largura/2, rural[i] + espaco_texto, f'{rural[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=15)

    plt.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[df['NU_ANO_CENSO'] == ano_censo]

    agrupado = df_filtrado.groupby(['TP_DEPENDENCIA', 'TP_LOCALIZACAO'])['CO_ENTIDADE'].count().unstack(fill_value=0)
    agrupado = agrupado.rename(index={1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    agrupado = agrupado.rename(columns={1: 'Urbana', 2: 'Rural'})

    categorias = agrupado.index.tolist()
    urbana = agrupado['Urbana']
    rural = agrupado['Rural']

    x = np.arange(len(categorias))
    largura = 0.35

    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    # # Barra dupla e Legenda
    ax.bar(x - largura/2, urbana, width=largura, label='Urbana', color='#C0C0C0')
    ax.bar(x + largura/2, rural, width=largura, label='Rural', color='#1FB029')

    # Eixos e rótulos
    ax.set_title(f'Total de Escolas por Dependência e Localização - ({ano_censo})', color='#FFA07A', fontsize=20)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)
    
    ax.set_xticks(x)
    ax.set_xticklabels(categorias, color='#FFA07A', fontsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=14)
    ax.legend()

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite superior responsivo
    limite_superior = max(urbana.max(), rural.max()) * 1.15
    ax.set_ylim(0, limite_superior)

    # Valores nas barras com espaçamento dinâmico
    espaco_texto = limite_superior * 0.015
    for i in range(len(categorias)):
        ax.text(x[i] - largura/2, urbana[i] + espaco_texto, f'{urbana[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=16)
        ax.text(x[i] + largura/2, rural[i] + espaco_texto, f'{rural[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=16)

    plt.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    agrupado = df_filtrado.groupby(['TP_DEPENDENCIA', 'TP_LOCALIZACAO'])['QT_MAT_BAS'].sum().unstack(fill_value=0)
    agrupado = agrupado.rename(index={1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    agrupado = agrupado.rename(columns={1: 'Urbana', 2: 'Rural'})

    categorias = agrupado.index.tolist()
    urbana = agrupado['Urbana']
    rural = agrupado['Rural']
    x = np.arange(len(categorias))
    largura = 0.35

    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Barras duplas
    ax.bar(x - largura/2, urbana, width=largura, label='Urbana', color='#C0C0C0')
    ax.bar(x + largura/2, rural, width=largura, label='Rural', color='#1FB029')

    ax.set_title(f'Matrículas por Dependência e Localização - {municipio} ({ano_censo})', color='#FFA07A', fontsize=20)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)

    ax.set_xticks(x)
    ax.set_xticklabels(categorias, color='#FFA07A', fontsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=14)
    ax.legend()

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite superior responsivo
    limite_superior = max(urbana.max(), rural.max()) * 1.15
    ax.set_ylim(0, limite_superior)

    # Valores nas barras com espaçamento dinâmico
    espaco_texto = limite_superior * 0.015
    for i in range(len(categorias)):
        ax.text(x[i] - largura/2, urbana[i] + espaco_texto, f'{urbana[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=16)
        ax.text(x[i] + largura/2, rural[i] + espaco_texto, f'{rural[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=16)

    plt.tight_layout()
    st.pyplot(fig)

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

    df_filtrado = df[
        (df['NU_ANO_CENSO'] == ano_censo) &
        (df['NO_MUNICIPIO'] == municipio)
    ]

    agrupado = df_filtrado.groupby(['TP_DEPENDENCIA', 'TP_LOCALIZACAO'])['CO_ENTIDADE'].nunique().unstack(fill_value=0)
    agrupado = agrupado.rename(index={1: 'Federal', 2: 'Estadual', 3: 'Municipal'})
    agrupado = agrupado.rename(columns={1: 'Urbana', 2: 'Rural'})

    categorias = agrupado.index.tolist()
    urbana = agrupado['Urbana']
    rural = agrupado['Rural']
    x = np.arange(len(categorias))
    largura = 0.35

    # Plotagem do gráfico
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Barras duplas
    ax.bar(x - largura/2, urbana, width=largura, label='Urbana', color='#C0C0C0')
    ax.bar(x + largura/2, rural, width=largura, label='Rural', color='#1FB029')

    ax.set_title(f'Escolas por Dependência e Localização - {municipio} ({ano_censo})', color='#FFA07A', fontsize=20)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels(categorias, color='#FFA07A', fontsize=17)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=14)
    ax.legend()

    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Cálculo do limite superior responsivo
    limite_superior = max(urbana.max(), rural.max()) * 1.15
    ax.set_ylim(0, limite_superior)

    # Valores nas barras com espaçamento dinâmico
    espaco_texto = limite_superior * 0.015
    for i in range(len(categorias)):
        ax.text(x[i] - largura/2, urbana[i] + espaco_texto, f'{urbana[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=20)
        ax.text(x[i] + largura/2, rural[i] + espaco_texto, f'{rural[i]:,.0f}', ha='center', color='white', fontweight='bold', fontsize=20)

    plt.tight_layout()
    st.pyplot(fig)


#============================
# PAGINA PANORAMA FINANCIAMENTO
#=============================

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

def grafico_agua_total_dados_brutos(df, ano_censo):
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
    fig, ax = plt.subplots(figsize=(8, 7.5))

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
    ax.set_title(f"Fornecimento de Água Potável - {ano_censo}", color="#FFA07A", fontsize=20)
    ax.set_ylabel("Número de Escolas", color="#FFA07A", fontsize=12)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=12)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    # Estilo dos ticks
    ax.tick_params(axis="x", colors="#FFA07A", labelsize=16)
    ax.tick_params(axis="y", colors="#FFA07A", labelsize=14)

    ax.set_ylim(0, contagem.max() * 1.2)

    fig.tight_layout()
    st.pyplot(fig)

def grafico_escolas_sem_agua_por_municipio(df, ano_censo):
    """
    Gera gráfico de barras horizontais mostrando o total de escolas
    sem água potável por município, no ano selecionado.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'NU_ANO_CENSO', 'IN_AGUA_POTAVEL' e 'NO_MUNICIPIO'.
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário.
    """
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import matplotlib.cm as cm
    import streamlit as st

    # Filtrar dados do ano e escolas sem água potável
    df_filtrado = df[
        (df["NU_ANO_CENSO"] == ano_censo) & 
        (df["IN_AGUA_POTAVEL"] == 0)
    ]

    if df_filtrado.empty:
        st.warning(f"Não há registros de escolas sem água potável em {ano_censo}.")
        return

    # Agrupar por município
    contagem = df_filtrado["NO_MUNICIPIO"].value_counts().sort_values(ascending=True)

    # Criar gradiente entre azul e amarelo (crescente)
    cor_inicio = "#B0E0E6"
    cor_fim = "#FFC107"
    cmap = mcolors.LinearSegmentedColormap.from_list("gradiente_agua", [cor_inicio, cor_fim])
    norm = mcolors.Normalize(vmin=0, vmax=len(contagem) - 1)
    cores = [cmap(norm(i)) for i in range(len(contagem))]

    # Estilo
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, max(5, len(contagem) * 0.45)))

    # Plotar barras horizontais
    barras = ax.barh(contagem.index, contagem.values, color=cores)

    # Rótulos ao final de cada barra
    for barra, valor in zip(barras, contagem.values):
        ax.text(
            valor + max(contagem.values) * 0.01,
            barra.get_y() + barra.get_height() / 2,
            str(valor),
            va="center",
            ha="left",
            color="white",
            fontweight="bold",
            fontsize=12
        )

    # Título e eixos
    ax.set_title(f"Escolas sem Água Potável por Município - {ano_censo}", color="#FFA07A", fontsize=22, pad=10)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=15)

    # Estilo visual do projeto
    ax.tick_params(colors="#FFA07A", labelsize=15)
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    fig.tight_layout()
    st.pyplot(fig)

def grafico_alunos_por_disponibilidade_agua(df, ano_censo):
    """
    Gera gráfico de barras verticais com o total de alunos matriculados
    em escolas que fornecem e que não fornecem água potável.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com colunas 'NU_ANO_CENSO', 'IN_AGUA_POTAVEL' e 'QT_MAT_BAS'.
    ano_censo : int
        Ano do censo escolar a ser considerado.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import pandas as pd

    # Filtrar dados do ano
    df_filtrado = df[df["NU_ANO_CENSO"] == ano_censo]

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para o ano {ano_censo}.")
        return

    # Garantir que QT_MAT_BAS seja numérico
    df_filtrado["QT_MAT_BAS"] = pd.to_numeric(df_filtrado["QT_MAT_BAS"], errors="coerce").fillna(0)

    # Agrupar soma de alunos por fornecimento de água potável
    soma_alunos = df_filtrado.groupby("IN_AGUA_POTAVEL")["QT_MAT_BAS"].sum().sort_index(ascending=False)
    soma_alunos.index = soma_alunos.index.map({1: "Fornece", 0: "Não Fornece"})

    # Cores fixas
    cores = ["#B0E0E6" if idx == "Fornece" else "#FFC107" for idx in soma_alunos.index]

    # Estilo do projeto
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plotagem vertical
    barras = ax.bar(soma_alunos.index, soma_alunos.values, color=cores)

    # Rótulos nas barras
    for bar, valor in zip(barras, soma_alunos.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + (soma_alunos.max() * 0.02),
            f"{int(valor):,}".replace(",", "."),
            ha="center", va="bottom",
            color="white", fontweight="bold", fontsize=13
        )

    # Título e eixos
    ax.set_title(f"Alunos por Disponibilidade de Água Potável — {ano_censo}", color="#FFA07A", fontsize=18)
    ax.set_ylabel("Número total de alunos", color="#FFA07A", fontsize=12)
    ax.set_xlabel("Disponibilidade de Água", color="#FFA07A", fontsize=12)

    # Estilo dos eixos e spines
    ax.tick_params(colors="#FFA07A", labelsize=12)
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_ylim(0, soma_alunos.max() * 1.25)

    fig.tight_layout()
    st.pyplot(fig)

def grafico_localizacao_escolas_sem_agua(df, ano_censo):
    """
    Gera gráfico de barras verticais com o total de escolas sem água potável,
    classificadas por localização (urbana ou rural), para o ano selecionado.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'NU_ANO_CENSO', 'IN_AGUA_POTAVEL' e 'TP_LOCALIZACAO'.
    ano_censo : int
        Ano do Censo Escolar selecionado.
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Filtra escolas sem água potável no ano especificado
    df_filtrado = df[
        (df["NU_ANO_CENSO"] == ano_censo) &
        (df["IN_AGUA_POTAVEL"] == 0)
    ]

    if df_filtrado.empty:
        st.warning(f"Não há escolas sem água potável em {ano_censo}.")
        return

    # Contagem por localização
    contagem = df_filtrado["TP_LOCALIZACAO"].value_counts().reindex([1, 2], fill_value=0)
    contagem.index = contagem.index.map({1: "Urbana", 2: "Rural"})
    cores = ["#B0E0E6", "#FFC107"]

    # Estilo visual do projeto
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(7, 5))

    barras = ax.bar(contagem.index, contagem.values, color=cores)

    # Rótulos nas barras
    for bar, valor in zip(barras, contagem.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + max(contagem.values) * 0.02,
            f"{valor:,}".replace(",", "."),
            ha="center",
            va="bottom",
            color="white",
            fontsize=13,
            fontweight="bold"
        )

    # Título e eixos
    ax.set_title(f"Escolas Sem Água Potável por Localização — {ano_censo}", color="#FFA07A", fontsize=16)
    ax.set_ylabel("Número de Escolas", color="#FFA07A", fontsize=11)
    ax.set_xlabel("Localização", color="#FFA07A", fontsize=11)

    # Estilo dos eixos
    ax.tick_params(colors="#FFA07A", labelsize=12)
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_ylim(0, contagem.max() * 1.25)
    fig.tight_layout()
    st.pyplot(fig)

def grafico_abastecimento_agua_por_fonte(df, ano_censo):
    """
    Gera gráfico de barras verticais com o total de escolas que utilizam
    cada tipo de fonte de abastecimento de água (valores igual a 1).

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com colunas binárias de abastecimento de água.
    ano_censo : int
        Ano a ser filtrado (NU_ANO_CENSO).
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    from scripts.utils import COLUNAS_RENOMEADAS_CENSO

    # Colunas de interesse
    colunas_agua = [
        "IN_AGUA_REDE_PUBLICA",
        "IN_AGUA_POCO_ARTESIANO",
        "IN_AGUA_CACIMBA",
        "IN_AGUA_FONTE_RIO",
        "IN_AGUA_INEXISTENTE",
        "IN_AGUA_CARRO_PIPA"
    ]

    # Filtrar apenas o ano solicitado
    df_filtrado = df[df["NU_ANO_CENSO"] == ano_censo]

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para o ano {ano_censo}.")
        return

    # Contar valores iguais a 1 por coluna
    contagem = df_filtrado[colunas_agua].apply(lambda col: (col == 1).sum())
    contagem.rename(index=COLUNAS_RENOMEADAS_CENSO, inplace=True)
    contagem = contagem.sort_values(ascending=False)

    # Definir cores: azul padrão (#B0E0E6), amarelo para fontes inadequadas
    cor_padrao = "#B0E0E6"
    cor_destaque = "#FFC107"
    colunas_destaque = [
        "IN_AGUA_CACIMBA",
        "IN_AGUA_FONTE_RIO",
        "IN_AGUA_INEXISTENTE",
        "IN_AGUA_CARRO_PIPA"
    ]
    nomes_destaque = [COLUNAS_RENOMEADAS_CENSO[col] for col in colunas_destaque]
    cores_barras = [cor_destaque if nome in nomes_destaque else cor_padrao for nome in contagem.index]

    # Estilo visual
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(11, 8))

    # Barras com cores condicionais
    barras = ax.bar(contagem.index, contagem.values, color=cores_barras)

    # Rótulos nas barras
    for bar, valor in zip(barras, contagem.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + contagem.max() * 0.02,
            f"{valor:,}".replace(",", "."),
            ha="center", va="bottom",
            fontsize=13, fontweight="bold", color="white"
        )

    # Título e eixos
    ax.set_title(f"Fontes de Abastecimento de Água - {ano_censo}", color="#FFA07A", fontsize=26)
    ax.set_ylabel("Número de Escolas", color="#FFA07A", fontsize=17)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=14)

    # Eixos e contorno
    ax.tick_params(axis='y', colors="#FFA07A", labelsize=15)
    ax.tick_params(axis='x', colors="#FFA07A", labelsize=17, rotation=10)
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_ylim(0, contagem.max() * 1.25)
    fig.tight_layout()
    st.pyplot(fig)

def grafico_agua_total_fontes(df, ano_censo):
    """
    Gera gráfico de barras verticais com o total de escolas que fornecem ou não fornecem água potável,
    com base nas condições de localização e tipo de abastecimento.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo os dados com colunas de localização e fontes de água.
    ano_censo : int
        Ano do censo escolar a ser filtrado (NU_ANO_CENSO).
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Filtrar ano do Censo
    df_filtrado = df[df["NU_ANO_CENSO"] == ano_censo]

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para o ano {ano_censo}.")
        return

    # Condições para "Fornece"
    cond_urbana = df_filtrado["TP_LOCALIZACAO"] == 1
    cond_rural_com_abastecimento = (
        (df_filtrado["TP_LOCALIZACAO"] == 2) &
        (
            (df_filtrado["IN_AGUA_REDE_PUBLICA"] == 1) |
            (df_filtrado["IN_AGUA_POCO_ARTESIANO"] == 1)
        )
    )
    total_fornece = (cond_urbana | cond_rural_com_abastecimento).sum()

    # Condições para "Não Fornece"
    cond_rural_sem_abastecimento = (
        (df_filtrado["TP_LOCALIZACAO"] == 2) &
        (
            (df_filtrado["IN_AGUA_CACIMBA"] == 1) |
            (df_filtrado["IN_AGUA_FONTE_RIO"] == 1) |
            (df_filtrado["IN_AGUA_INEXISTENTE"] == 1) |
            (df_filtrado["IN_AGUA_CARRO_PIPA"] == 1)
        )
    )
    total_nao_fornece = cond_rural_sem_abastecimento.sum()

    # Dados para o gráfico
    categorias = ["Fornece", "Não Fornece"]
    valores = [total_fornece, total_nao_fornece]
    cores = ["#B0E0E6", "#FFC107"]

    # Estilo do gráfico
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(8, 6))

    barras = ax.bar(categorias, valores, color=cores)

    # Rótulos nas barras
    for bar, valor in zip(barras, valores):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + max(valores) * 0.02,
            f"{valor:,}".replace(",", "."),
            ha="center", va="bottom",
            fontsize=13, color="white", fontweight="bold"
        )

    # Título e eixos
    ax.set_title(f"Fornecimento de Água Potável por Fonte de Abastecimento - {ano_censo}", color="#FFA07A", fontsize=15)
    ax.set_ylabel("Número de Escolas", color="#FFA07A", fontsize=12)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=12)

    ax.tick_params(axis='x', colors="#FFA07A", labelsize=14)
    ax.tick_params(axis='y', colors="#FFA07A", labelsize=12)
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_ylim(0, max(valores) * 1.25)
    fig.tight_layout()
    st.pyplot(fig)

def grafico_agua_total_fontes_municipios(df, municipio):
    """
    Gera gráfico de barras verticais com o total de escolas que fornecem ou não fornecem água potável
    segundo a localização e fontes de abastecimento, para um municipio específico no último ano disponível.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame com os dados do panorama da água potável.
    municipio : str
        Nome do município (coluna NO_MUNICIPIO).
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Último ano do Censo
    ultimo_ano = df["NU_ANO_CENSO"].max()

    # Filtrar pelo ano e pelo municipio selecionado
    df_filtrado = df[
        (df["NU_ANO_CENSO"] == ultimo_ano) &
        (df["NO_MUNICIPIO"] == municipio)
    ]

    if df_filtrado.empty:
        st.warning(f"Não há dados disponíveis para o ente '{municipio}' no ano {ultimo_ano}.")
        return

    # Condições para "Fornece"
    cond_urbana = df_filtrado["TP_LOCALIZACAO"] == 1
    cond_rural_com_abastecimento = (
        (df_filtrado["TP_LOCALIZACAO"] == 2) &
        (
            (df_filtrado["IN_AGUA_REDE_PUBLICA"] == 1) |
            (df_filtrado["IN_AGUA_POCO_ARTESIANO"] == 1)
        )
    )
    total_fornece = (cond_urbana | cond_rural_com_abastecimento).sum()

    # Condições para "Não Fornece"
    cond_rural_sem_abastecimento = (
        (df_filtrado["TP_LOCALIZACAO"] == 2) &
        (
            (df_filtrado["IN_AGUA_CACIMBA"] == 1) |
            (df_filtrado["IN_AGUA_FONTE_RIO"] == 1) |
            (df_filtrado["IN_AGUA_INEXISTENTE"] == 1) |
            (df_filtrado["IN_AGUA_CARRO_PIPA"] == 1)
        )
    )
    total_nao_fornece = cond_rural_sem_abastecimento.sum()

    # Dados para o gráfico
    categorias = ["Fornece", "Não Fornece"]
    valores = [total_fornece, total_nao_fornece]
    cores = ["#B0E0E6", "#FFC107"]

    # Estilo do gráfico
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(8, 6))

    barras = ax.bar(categorias, valores, color=cores)

    # Rótulos nas barras
    for bar, valor in zip(barras, valores):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + max(valores) * 0.02,
            f"{valor:,}".replace(",", "."),
            ha="center", va="bottom",
            fontsize=13, color="white", fontweight="bold"
        )

    # Título e eixos
    ax.set_title(
        f"Fornecimento de Água Potável - {municipio} ({ultimo_ano})",
        color="#FFA07A",
        fontsize=20
    )
    ax.set_ylabel("Número de Escolas", color="#FFA07A", fontsize=12)
    ax.set_xlabel("Fonte: Censo Escolar", color="#FFA07A", fontsize=12)

    ax.tick_params(axis='x', colors="#FFA07A", labelsize=14)
    ax.tick_params(axis='y', colors="#FFA07A", labelsize=12)
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_ylim(0, max(valores) * 1.25)
    fig.tight_layout()
    st.pyplot(fig)
    
def grafico_escolas_uex_por_ano(df_agua, df_uex, ano):
    """
    Gera gráfico de barras verticais comparando:
    1. Total de escolas ativas no Censo Escolar;
    2. Total de escolas com CNPJ de Unidade Executora (UEX);
    3. Total de UEX únicas cadastradas;
    4. Total de escolas rurais no Censo;
    5. Total de UEX únicas vinculadas a escolas localizadas na zona rural.

    Parâmetros:
    -----------
    df_agua : pd.DataFrame
        DataFrame do panorama da água potável (Censo Escolar), com a coluna 'NU_ANO_CENSO' e 'CO_ENTIDADE'.
    df_uex : pd.DataFrame
        DataFrame das Unidades Executoras, com a coluna 'CNPJ UEX', 'Código Escola' e 'Localização'.
    ano : int
        Ano a ser considerado para o filtro dos dois DataFrames.
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Filtrar os DataFrames pelo ano informado
    df_agua_filtrado = df_agua[df_agua["NU_ANO_CENSO"] == ano]
    df_uex_filtrado = df_uex[df_uex["Ano"] == ano] if "Ano" in df_uex.columns else df_uex

    # Total de escolas ativas no Censo
    total_escolas_censo = df_agua_filtrado["CO_ENTIDADE"].nunique()

    # Total de escolas com CNPJ UEX informado (não nulo)
    total_escolas_com_uex = df_uex_filtrado[
        (df_uex_filtrado["CNPJ UEX"].notna()) &
        (df_uex_filtrado["CNPJ UEX"] != df_uex_filtrado["CNPJ EEX"])
        ]["Código Escola"].nunique()


    # Total de UEX únicas
    df_uex_unicas = df_uex_filtrado[
        (df_uex_filtrado["CNPJ UEX"].dropna().nunique()) &
        (df_uex_filtrado["CNPJ UEX"] != df_uex_filtrado["CNPJ EEX"])
    ]
    total_uex_unicas = df_uex_unicas["CNPJ UEX"].nunique()
    
    # Total escolas rurais
    total_escolas_rurais = df_agua_filtrado[df_agua_filtrado["TP_LOCALIZACAO"] == 2]["CO_ENTIDADE"].nunique()

    # Total de UEX próprias em escolas da zona rural
    df_rural = df_uex_filtrado[
        (df_uex_filtrado["Localização"].str.lower() == "rural") &
        (df_uex_filtrado["CNPJ UEX"].notna()) &
        (df_uex_filtrado["CNPJ UEX"] != df_uex_filtrado["CNPJ EEX"])
    ]
    total_uex_rural = df_rural["CNPJ UEX"].shape[0]

    # Dados do gráfico
    categorias = [
        "Escolas Ativas",
        "UEx próprias",
        "UEx únicas",
        "Escolas Rurais",
        "UEx Rurais próprias"
    ]
    valores = [
        total_escolas_censo,
        total_escolas_com_uex,
        total_uex_unicas,
        total_escolas_rurais,
        total_uex_rural
    ]
    cores = ["#B0E0E6", "#90CAF9", "#FFC107", "#006400", "#FF0000"]

    # Estilo visual
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(11, 7))

    barras = ax.bar(categorias, valores, color=cores)

    # Rótulos nas barras
    for bar, valor in zip(barras, valores):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + max(valores) * 0.02,
            f"{valor:,}".replace(",", "."),
            ha="center", va="bottom",
            fontsize=13, color="white", fontweight="bold"
        )

    # Título e eixos
    ax.set_title(f"Total de Escolas e Unidades Executoras - {ano}", color="#FFA07A", fontsize=24)
    ax.set_xlabel("Fonte: Censo Escolar e PDDE Info", color="#FFA07A", fontsize=10)

    ax.tick_params(axis='x', colors="#FFA07A", labelsize=13)
    ax.tick_params(axis='y', colors="#FFA07A", labelsize=13)
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_ylim(0, max(valores) * 1.25)
    fig.tight_layout()
    st.pyplot(fig)

def grafico_uex_por_municipio(df_agua, df_uex, municipio):
    """
    Gera gráfico de barras verticais com dados das Unidades Executoras (UEx)
    e do Censo Escolar para um município específico, no ano mais recente.

    Parâmetros:
    -----------
    df_uex : pd.DataFrame
        DataFrame com dados das Unidades Executoras, contendo colunas:
        'Ano', 'Município', 'Código Escola', 'CNPJ UEX', 'CNPJ EEX', 'Localização'.
    
    df_agua : pd.DataFrame
        DataFrame do Censo Escolar (água potável), contendo colunas:
        'NU_ANO_CENSO', 'NO_MUNICIPIO', 'TP_LOCALIZACAO', 'CO_ENTIDADE'.
    
    municipio : str
        Nome do município a ser filtrado (exato).
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Ano mais recente disponível em df_uex
    ano = df_uex["Ano"].max()

    # === Filtragem dos DataFrames ===
    df_uex_mun = df_uex[
        (df_uex["Ano"] == ano) &
        (df_uex["Municipio"].str.upper() == municipio.upper())
    ]
    df_agua_mun = df_agua[
        (df_agua["NU_ANO_CENSO"] == ano) &
        (df_agua["NO_MUNICIPIO"].str.upper() == municipio.upper())
    ]

    if df_uex_mun.empty or df_agua_mun.empty:
        st.warning(f"Não há dados disponíveis para o município '{municipio}' no ano {ano}.")
        return

    # === Métricas ===
    total_escolas = df_agua_mun["CO_ENTIDADE"].nunique()
    total_escolas_rurais = df_agua_mun[df_agua_mun["TP_LOCALIZACAO"] == 2]["CO_ENTIDADE"].nunique()

    total_escolas_com_uex = df_uex_mun[df_uex_mun["CNPJ UEX"].notna()]["Código Escola"].nunique()

    total_uex_unicas = df_uex_mun[
        (df_uex_mun["CNPJ UEX"].notna()) &
        (df_uex_mun["CNPJ UEX"] != df_uex_mun["CNPJ EEX"])
    ]["CNPJ UEX"].nunique()

    total_uex_rural = df_uex_mun[
        (df_uex_mun["Localização"].str.lower() == "rural") &
        (df_uex_mun["CNPJ UEX"].notna()) &
        (df_uex_mun["CNPJ UEX"] != df_uex_mun["CNPJ EEX"])
    ].shape[0]

    # === Gráfico ===
    categorias = [
        "Escolas Ativas",
        "UEx próprias",
        "UEx únicas",
        "Escolas Rurais",
        "UEx Rurais próprias"
    ]
    valores = [
        total_escolas,
        total_escolas_com_uex,
        total_uex_unicas,
        total_escolas_rurais,
        total_uex_rural
    ]
    cores = ["#B0E0E6", "#90CAF9", "#FFC107", "#006400", "#FF0000"]

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(11, 7))

    barras = ax.bar(categorias, valores, color=cores)

    # Rótulos nas barras
    for bar, valor in zip(barras, valores):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + max(valores) * 0.02,
            f"{valor:,}".replace(",", "."),
            ha="center", va="bottom",
            fontsize=13, color="white", fontweight="bold"
        )

    # Estética
    ax.set_title(f"Escolas e Unidades Executoras - {municipio} ({ano})", color="#FFA07A", fontsize=22)
    ax.set_xlabel("Fonte: Censo Escolar e PDDE Info", color="#FFA07A", fontsize=11)
    ax.tick_params(axis='x', colors="#FFA07A", labelsize=13)
    ax.tick_params(axis='y', colors="#FFA07A", labelsize=13)

    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_ylim(0, max(valores) * 1.25)
    fig.tight_layout()
    st.pyplot(fig)

def grafico_pdde_agua_por_ano(df):
    """
    Gera gráfico de barras verticais com o total de escolas que acessaram o PDDE Água por ano,
    com base nas ocorrências da palavra 'água' (em diferentes grafias) na coluna 'Destinação'.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'Ano' e 'Destinação'.
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # Garantir que colunas existam
    if "Ano" not in df.columns or "Destinação" not in df.columns:
        st.error("O DataFrame deve conter as colunas 'Ano' e 'Destinação'.")
        return

    # Filtrar linhas onde 'Destinação' menciona "água" (tolerante a maiúsculas/minúsculas/acentos)
    filtro_agua = df["Destinação"].str.contains(r"\b(água|agua)\b", case=False, na=False, regex=True)
    df_filtrado = df[filtro_agua]

    if df_filtrado.empty:
        st.warning("Não há registros com 'água' na coluna 'Destinação'.")
        return

    # Agrupar por ano e contar ocorrências
    contagem_por_ano = df_filtrado["Ano"].value_counts().sort_index()

    # Estilo visual
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, 8.9))

    cor_barras = "#B0E0E6"  # Azul do projeto
    barras = ax.bar(contagem_por_ano.index.astype(str), contagem_por_ano.values, color=cor_barras)

    # Rótulos nas barras
    for bar, valor in zip(barras, contagem_por_ano.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            valor + contagem_por_ano.max() * 0.02,
            f"{valor:,}".replace(",", "."),
            ha="center", va="bottom",
            fontsize=15, color="white", fontweight="bold"
        )

    # Título e eixos
    ax.set_title("Escolas que acessaram o PDDE Água por ano", color="#FFA07A", fontsize=24)
    ax.set_xlabel("Fonte: PDDE Info", color="#FFA07A", fontsize=11)

    ax.tick_params(axis='x', colors="#FFA07A", labelsize=17)
    ax.tick_params(axis='y', colors="#FFA07A", labelsize=12)
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_ylim(0, contagem_por_ano.max() * 1.25)
    fig.tight_layout()
    st.pyplot(fig)

def grafico_pdde_agua_por_municipio(df, ano):
    """
    Gera gráfico de barras horizontais com o total de escolas que acessaram o PDDE Água por município,
    para um determinado ano. Considera menções a 'água' na coluna 'Destinação'.

    Se o município não aparecer no ano selecionado, seu valor será 0.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'Ano', 'Destinação' e 'Município'.
    ano : int
        Ano a ser filtrado na análise.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import pandas as pd

    # Verificações básicas
    colunas_necessarias = {"Ano", "Destinação", "Município"}
    if not colunas_necessarias.issubset(df.columns):
        st.error("O DataFrame deve conter as colunas: 'Ano', 'Destinação' e 'Município'.")
        return

    # Lista de todos os municípios existentes no DataFrame (mesmo que não apareçam no ano)
    todos_municipios = sorted(df["Município"].dropna().unique())

    # Filtrar apenas o ano indicado
    df_ano = df[df["Ano"] == ano]

    # Se não houver dados, cria DataFrame vazio com municípios zerados
    if df_ano.empty:
        contagem = pd.Series(0, index=todos_municipios, dtype=int)
    else:
        # Coluna booleana para menções à "água"
        df_ano["ACESSOU_PDDE_AGUA"] = df_ano["Destinação"].str.contains(
            r"\b(água|agua)\b", case=False, na=False, regex=True
        )

        # Contar quantas escolas acessaram PDDE Água por município
        contagem = df_ano.groupby("Município")["ACESSOU_PDDE_AGUA"].sum().astype(int)

        # Garantir que todos os municípios existam no índice (preencher os ausentes com 0)
        contagem = contagem.reindex(todos_municipios, fill_value=0)

    # Ordenar alfabeticamente ou por valor (opcional)
    contagem = contagem.sort_values(ascending=True)

    # Estilo visual do projeto
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, max(6, len(contagem) * 0.4)))

    barras = ax.barh(contagem.index, contagem.values, color="#B0E0E6")

    # Rótulos ao final das barras (inclusive 0)
    for bar, valor in zip(barras, contagem.values):
        ax.text(
            valor + (contagem.max() * 0.01 if contagem.max() > 0 else 0.1),
            bar.get_y() + bar.get_height() / 2,
            f"{int(valor)}",
            va="center", ha="left",
            fontsize=12, color="white", fontweight="bold"
        )

    # Título e eixos
    ax.set_title(f"Escolas que acessaram o PDDE Água por Município — {ano}", color="#FFA07A", fontsize=20)
    ax.set_xlabel("Fonte: PDDE Info", color="#FFA07A", fontsize=12)
    

    ax.tick_params(axis='x', colors="#FFA07A", labelsize=12)
    ax.tick_params(axis='y', colors="#FFA07A", labelsize=11)

    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    ax.set_xlim(0, contagem.max() * 1.25 if contagem.max() > 0 else 1)
    fig.tight_layout()
    st.pyplot(fig)

def grafico_pdde_agua_escolas(df_censo, df_uex, df_equidade):
    """
    Gera gráfico de barras verticais para o último ano disponível,
    representando:
    1. Escolas que acessaram PDDE Água
    2. Escolas elegíveis que não acessaram
    3. Escolas potenciais com falhas de gestão

    Parâmetros:
    ------------
    df_censo : pd.DataFrame
    df_uex : pd.DataFrame
    df_equidade : pd.DataFrame
    """
    import matplotlib.pyplot as plt
    import streamlit as st

    # ============
    # Selecionar último ano
    # ============
    ultimo_ano = df_censo["NU_ANO_CENSO"].max()

    df_censo_ano = df_censo[df_censo["NU_ANO_CENSO"] == ultimo_ano].copy()
    df_uex_ano = df_uex[df_uex["Ano"] == ultimo_ano].copy()
    df_eq_ano = df_equidade[df_equidade["Ano"] == ultimo_ano].copy()

    # ============
    # Renomear colunas para merge
    # ============
    df_uex_ano = df_uex_ano.rename(columns={"Código Escola": "CO_ENTIDADE"})
    df_eq_ano = df_eq_ano.rename(columns={"Código Escola": "CO_ENTIDADE"})

    # ============
    # Merge dos 3 dataframes
    # ============
    df_merged = df_censo_ano.merge(df_uex_ano, on="CO_ENTIDADE", how="left", suffixes=('', '_uex'))
    df_merged = df_merged.merge(df_eq_ano, on="CO_ENTIDADE", how="left", suffixes=('', '_eq'))

    # ============
    # Coluna auxiliar: acessou PDDE com destinação para água
    # ============
    df_merged["acessou_pdde_agua"] = df_merged["Destinação"].fillna("").str.contains(r"\b(água|agua)\b", case=False)

    # ============
    # Coluna auxiliar: tem UEX própria
    # ============
    df_merged["tem_uex"] = df_merged["CNPJ UEX"].notna() & (df_merged["CNPJ UEX"] != df_merged["CNPJ EEX"])

    # ============
    # Escolas elegíveis
    # ============
    df_merged["elegivel"] = (
        (df_merged["TP_LOCALIZACAO"] == 2) &
        (df_merged["IN_AGUA_POTAVEL"] == 0) &
        (df_merged["TP_OCUPACAO_PREDIO_ESCOLAR"] == 1) &
        (df_merged["tem_uex"]) &
        (~df_merged["acessou_pdde_agua"]) &
        (
            (
                (df_merged["IN_AGUA_POCO_ARTESIANO"] != 1) &
                (df_merged["IN_AGUA_REDE_PUBLICA"] != 1)
            ) 
        )
    )

    # ============
    # Escolas potenciais
    # ============
    df_merged["potencial"] = (
        (df_merged["TP_LOCALIZACAO"] == 2) &
        (~df_merged["acessou_pdde_agua"]) &
        (
            (df_merged["IN_AGUA_POCO_ARTESIANO"] != 1) &
            (df_merged["IN_AGUA_REDE_PUBLICA"] != 1) 
        )
    )

    # ============
    # Contagens
    # ============
    n_acessaram = df_merged["acessou_pdde_agua"].sum()
    n_elegiveis = df_merged["elegivel"].sum()
    n_potenciais = df_merged["potencial"].sum() - n_elegiveis

    # ============
    # Gráfico
    # ============
    categorias = [
        "Acessaram\nPDDE Água",
        "Escolas Elegíveis",
        "Escolas Potenciais"
    ]
    valores = [n_acessaram, n_elegiveis, n_potenciais]
    cores = ['#B0E0E6', '#FFC107', '#FFA07A']

    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.bar(categorias, valores, color=cores, edgecolor='white')

    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")
    ax.set_title(f"Acesso ao PDDE Água por Escola - {ultimo_ano}", color="#FFA07A", fontsize=20)
    ax.tick_params(axis='x', colors="#FFA07A", labelsize=15)
    ax.tick_params(axis='y', colors="#FFA07A", labelsize=12)
    ax.set_xlabel("Fonte: PDDE Info", color="#FFA07A", fontsize=12)
    
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    for bar in bars:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2.0, 
            yval + 1, f'{yval}', ha='center', va='bottom', 
            fontsize=15, color='white', fontweight="bold")

    st.pyplot(fig)
    
def grafico_pdde_agua_financeiro(df_censo, df_uex, df_equidade):
    """
    Gera gráfico de barras verticais com valores financeiros estimados ou pagos
    referentes ao PDDE Água, com base em dados de execução e matrículas.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import numpy as np

    # ============
    # Selecionar último ano
    # ============
    ano = df_censo["NU_ANO_CENSO"].max()
    df_censo = df_censo[df_censo["NU_ANO_CENSO"] == ano].copy()
    df_uex = df_uex[df_uex["Ano"] == ano].copy().rename(columns={"Código Escola": "CO_ENTIDADE"})
    df_equidade = df_equidade[df_equidade["Ano"] == ano].copy().rename(columns={"Código Escola": "CO_ENTIDADE"})

    # ============
    # Merge
    # ============
    df = df_censo.merge(df_uex, on="CO_ENTIDADE", how="left", suffixes=('', '_uex'))
    df = df.merge(df_equidade, on="CO_ENTIDADE", how="left", suffixes=('', '_eq'))

    # ============
    # Marcadores auxiliares
    # ============
    df["acessou_pdde_agua"] = df["Destinação"].fillna("").str.contains(r"\b(água|agua)\b", case=False)
    df["tem_uex"] = df["CNPJ UEX"].notna() & (df["CNPJ UEX"] != df["CNPJ EEX"])

    df["elegivel"] = (
        (df["TP_LOCALIZACAO"] == 2) &
        (df["IN_AGUA_POTAVEL"] == 0) &
        (df["TP_OCUPACAO_PREDIO_ESCOLAR"] == 1) &
        df["tem_uex"] &
        ~df["acessou_pdde_agua"] &
        ((df["IN_AGUA_POCO_ARTESIANO"] != 1) & (df["IN_AGUA_REDE_PUBLICA"] != 1))
    )

    df["potencial"] = (
        (df["TP_LOCALIZACAO"] == 2) &
        ~df["acessou_pdde_agua"] &
        ((df["IN_AGUA_POCO_ARTESIANO"] != 1) & (df["IN_AGUA_REDE_PUBLICA"] != 1))
    )

    # Evitar dupla contagem
    df["potencial"] = df["potencial"] & (~df["elegivel"])

    # ============
    # Faixa de repasse estimado por escola
    # ============
    def calcular_faixa_recurso(matriculas):
        if pd.isna(matriculas):
            return 0
        elif matriculas <= 50:
            return 30000
        elif matriculas <= 150:
            return 35000
        else:
            return 45000

    df["repasse_estimado"] = df["QT_MAT_BAS"].apply(calcular_faixa_recurso)

    # ============
    # Valores por grupo
    # ============
    # 1. Acessaram: soma real dos valores pagos
    acessaram_valor = df[df["acessou_pdde_agua"]]["Valor Total"].fillna(0).sum()

    # 2. Elegíveis: soma estimada
    elegiveis_valor = df[df["elegivel"]]["repasse_estimado"].sum()

    # 3. Potenciais: soma estimada
    potenciais_valor = df[df["potencial"]]["repasse_estimado"].sum()

    # ============
    # Gráfico
    # ============
    categorias = [
        "Acessaram\nPDDE Água",
        "Escolas Elegíveis",
        "Escolas Potenciais"
    ]
    valores = [acessaram_valor, elegiveis_valor, potenciais_valor]
    cores = ['#B0E0E6', '#FFC107', '#FFA07A']

    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.bar(categorias, valores, color=cores, edgecolor='white')

    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")
    ax.set_title(f"Impacto Financeiro do PDDE Água - {ano}", color="#FFA07A", fontsize=21)
    ax.tick_params(axis='x', colors="#FFA07A", labelsize=15)
    ax.tick_params(axis='y', colors="#FFA07A", labelsize=12)
    ax.set_xlabel("Fonte: PDDE Info e Censo Escolar", color="#FFA07A", fontsize=13)
    for spine in ax.spines.values():
        spine.set_color("#FFA07A")

    for bar in bars:
        yval = bar.get_height()
        label = f'R$ {yval:,.0f}'.replace(',', '.')
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + (yval * 0.01),
                label, ha='center', va='bottom',
                fontsize=14, color='white', fontweight="bold")

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


