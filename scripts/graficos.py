import matplotlib.pyplot as plt
import streamlit as st

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
