
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import streamlit as st

#============================
# Função para plotar gráfico de barras sobre o fornecimento de água potável
#============================
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



#==========================
# Função para plotar gráfico de barras horizontal com o total de alunos por município
#==========================
def grafico_alunos_por_municipio(df, ano_censo):
    """
    Gera um gráfico de barras horizontal com o total de alunos por município.

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

    # Agrupar e somar os alunos por município
    resultado_alunos = df_filtrado.groupby('NO_MUNICIPIO')['QT_MAT_BAS'].sum().sort_values(ascending=True)

    # Gradiente de cores
    cmap = mcolors.LinearSegmentedColormap.from_list('custom_gradient', ['#B0E0E6', '#FFC107'])
    norm = plt.Normalize(vmin=resultado_alunos.min(), vmax=resultado_alunos.max())
    cores = [cmap(norm(valor)) for valor in resultado_alunos]

    # Gráfico total de alunos por município
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15, max(8, 0.5 * len(resultado_alunos))))
    bars = ax.barh(resultado_alunos.index, resultado_alunos.values, color=cores)

    # Ajusta dinamicamente o limite superior do eixo X com uma folga de 10%
    limite_superior = resultado_alunos.max() * 1.1
    ax.set_xlim(right=limite_superior)

    # Título e rótulos
    ax.set_title('Total de Alunos por Município', color='#FFA07A', fontsize=40)

    # Estilo dos spines
    for spine in ax.spines.values():
        spine.set_color('#FFA07A')
        spine.set_linewidth(1)

    # Ticks
    ax.tick_params(axis='x', colors='#FFA07A', labelsize=25)
    ax.tick_params(axis='y', colors='#FFA07A', labelsize=25)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1000)}mil'))

    # Inserir valores nas barras com base mil
    for i, valor in enumerate(resultado_alunos):
        ax.text(valor + (resultado_alunos.max() * 0.01), i, f'{int(valor/1000)}', va='center',
                color='white', fontweight='bold', fontsize=22)

    fig.tight_layout()
    st.pyplot(fig)




#===========================
# Função para plotar gráfico de barras horizontal com o total de escolas
#============================    
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


#===========================
# Função para gráfico de barras verticais para o total de escolas por dependência administrativa
#===========================
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


#===========================
# Função para gráfico de barras verticais para o total de alunos por dependência administrativa
#===========================
def grafico_alunos_por_dependencia(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de alunos por dependência administrativa.

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

    # Agrupa por Dependência Administrativa e soma os alunos
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
    ax.set_title(f'Total de Alunos por Dependência Administrativa', color='#FFA07A', fontsize=25)
    #ax.set_ylabel('Número de Alunos', color='#FFA07A', fontsize=14)
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


#===========================
# Função para panorama Urbano vs Rural
#===========================
def grafico_escolas_por_localizacao(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de escolas por dependência administrativa.

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


#===========================
# Função para gráfico de barras verticais para o total de alunos por localizacao
#===========================
def grafico_alunos_por_localizacao(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de alunos por localizacao.

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

    # Agrupa por Localização e soma os alunos
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
    ax.set_title('Total de Alunos por Localização', color='#FFA07A', fontsize=25)
    # ax.set_ylabel('Número de Alunos', color='#FFA07A', fontsize=14)
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


#===========================
# Função gráfico de barras total de alunos por localizacao diferenciada
#===========================

def grafico_alunos_por_localizacao_diferenciada(df, ano_censo):
    """
    Gera um gráfico de barras verticais com o total de alunos por localizacao diferenciada.

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
    
    # Agrupa por Localização e soma os alunos
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
    ax.set_title('Total de Alunos por Localização Diferenciada', color='#FFA07A', fontsize=25)
    # ax.set_ylabel('Número de Alunos', color='#FFA07A', fontsize=14)
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
    
#===========================
# Função gráfico de barras total de escolas por localizacao diferenciada
#===========================
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
    
#===========================
