
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import streamlit as st
import numpy as np

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
    ax.set_title('Total da Receita do Fundeb (R$ milhões)', color='#FFA07A', fontsize=30)
    
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
    fig, ax = plt.subplots(figsize=(9, 8))
    ax.bar(df_filtrado['ano'].astype(str), df_filtrado['valor_milhoes'], color=cor_barras)

    # Título e eixos
    ax.set_title(f'Fundeb Total por Ente - {ente}', color='#FFA07A', fontsize=23)
    ax.set_ylabel('Valor em milhões de reais (R$ mi)', color='#FFA07A', fontsize=15)
    
    # Estilo dos spines e ticks
    ax.tick_params(colors='#FFA07A', labelsize=12)
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

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'nome', 'ano' e 'indicador_despesa_fundeb_profissionais'.
    ente : str
        Nome do Município ou Estado selecionado pelo usuário.
    """
    import matplotlib.pyplot as plt
    import streamlit as st
    import pandas as pd

    # Filtrar dados do ente
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float (caso esteja como string com vírgula)
    df_filtrado['indicador_despesa_fundeb_profissionais'] = pd.to_numeric(
        df_filtrado['indicador_despesa_fundeb_profissionais'].astype(str).str.replace(',', '.'),
        errors='coerce'
    )

    # Estilo do gráfico
    plt.style.use('dark_background')

    # Cor padrão
    cor_barras = '#006400'  # Verde escuro

    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(
        df_filtrado['ano'].astype(str),
        df_filtrado['indicador_despesa_fundeb_profissionais'],
        color=cor_barras
    )

    # Título e eixos
    ax.set_title(f'Evolução da Despesa com Profissionais da Educação - {ente}',
                 color='#FFA07A', fontsize=16)
    ax.set_ylabel('Indicador (%)', color='#FFA07A', fontsize=12)
    ax.set_xlabel('Ano', color='#FFA07A', fontsize=12)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Estilo dos ticks
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=12)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=12)

    # Limite do eixo Y
    ax.set_ylim(0, 100)

    # Inserção dos valores
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

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'nome', 'ano', 'valor_receita_nao_aplicada' e 'valor_receita_total_fundeb'.
    ente : str
        Nome do Município ou Estado selecionado pelo usuário.
    """

    # Filtrar dados para o ente
    df_filtrado = df[df['nome'] == ente].sort_values(by='ano').copy()

    # Conversão segura para float (caso existam vírgulas)
    df_filtrado['valor_receita_nao_aplicada'] = pd.to_numeric(
        df_filtrado['valor_receita_nao_aplicada'].astype(str).str.replace(',', '.'),
        errors='coerce'
    )
    df_filtrado['valor_receita_total_fundeb'] = pd.to_numeric(
        df_filtrado['valor_receita_total_fundeb'].astype(str).str.replace(',', '.'),
        errors='coerce'
    )

    # Calcular o percentual de recursos não utilizados
    df_filtrado['percentual_nao_utilizado'] = (
        (df_filtrado['valor_receita_nao_aplicada'] / df_filtrado['valor_receita_total_fundeb']) * 100
    ).round(1)

    # Estilo do gráfico
    plt.style.use('dark_background')

    # Cor das barras
    cor_barras = '#FFD700'  # Amarelo ouro (para destacar "não aplicado")

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(
        df_filtrado['ano'].astype(str),
        df_filtrado['percentual_nao_utilizado'],
        color=cor_barras
    )

    # Título e eixos
    ax.set_title(f'Percentual de Recursos do Fundeb Não Utilizados - {ente}',
                 color='#FFA07A', fontsize=16)
    ax.set_ylabel('Percentual (%)', color='#FFA07A', fontsize=12)
    ax.set_xlabel('Ano', color='#FFA07A', fontsize=12)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')

    # Estilo dos ticks
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=12)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=12)

    # Definir limite do eixo y até o maior valor + margem (ou até 100% se desejar fixar)
    limite_y = max(100, df_filtrado['percentual_nao_utilizado'].max() * 1.2)
    ax.set_ylim(0, limite_y)

    # Inserção dos valores no topo das barras
    for i, valor in enumerate(df_filtrado['percentual_nao_utilizado']):
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
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=12)
    ax.set_xlabel('Fonte: SIOPE', color='#FFA07A', fontsize=12)

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
    ax.set_ylabel('Valor em milhões de R$ (mi)', color='#FFA07A', fontsize=12)
    ax.set_xlabel('Fonte: Siope', color='#FFA07A', fontsize=12)
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



#==========================
# PAGINA PANORAMA ÁGUA
#==========================
    
# Função para plotar gráfico de barras sobre o fornecimento de água potável
def plot_agua_potavel_por_municipio(df_censo_agua, ano_censo, municipio_selecionado, CORES_BARRAS, COR_TEXTO):
    """
    Gera gráfico de barras sobre o fornecimento de água potável em um município específico e ano selecionado.

    Parâmetros:
    - df_censo_agua: DataFrame contendo os dados do censo escolar.
    - ano_censo: Ano do censo a ser filtrado (int).
    - municipio_selecionado: Nome do município (string).
    - CORES_BARRAS: Dicionário com cores personalizadas para as categorias 0 e 1.
    - COR_TEXTO: Cor padrão dos textos e títulos (hexadecimal string).
    """
    # Filtrar o DataFrame
    df_grafico = df_censo_agua[
        (df_censo_agua['NU_ANO_CENSO'] == ano_censo) &
        (df_censo_agua['NO_MUNICIPIO'] == municipio_selecionado)
    ]

    # Contar categorias de fornecimento de água potável
    agua_counts = df_grafico['IN_AGUA_POTAVEL'].value_counts().sort_index()
    agua_counts.index = agua_counts.index.map({0: 'Não Fornece', 1: 'Fornece'})

    # Dividir layout em colunas
    col1, _ = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(6, 5))

        # Cores das barras com base no índice
        cores_barras = [CORES_BARRAS[1] if cat == 'Não Fornece' else CORES_BARRAS[0] for cat in agua_counts.index]

        ax.bar(agua_counts.index, agua_counts.values, color=cores_barras)

        # Ajustes visuais
        ax.set_ylim(0, agua_counts.max() * 1.2)
        ax.set_title(f"Fornecimento de Água Potável em {municipio_selecionado} ({ano_censo})", color=COR_TEXTO)
        ax.set_ylabel('Número de Escolas', color=COR_TEXTO)
        ax.set_xticklabels(agua_counts.index, color=COR_TEXTO)
        ax.tick_params(axis='y', colors=COR_TEXTO)

        for spine in ax.spines.values():
            spine.set_color(COR_TEXTO)

        # Adicionar rótulos nas barras
        for i, v in enumerate(agua_counts):
            ax.text(i, v + 0.2, str(v), ha='center', color='white', fontweight='bold')

        plt.tight_layout()
        st.pyplot(fig)