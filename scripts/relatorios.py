# Panorama Água

def pan_agua_relatorio_potavel_censo(df_censo, municipio, ano_censo):
    """
    Gera um relatório das escolas que marcaram fornecer água potável no Censo Escolar, por Município.
    
    Parâmetros:
    -----------
    df_censo : pd.DataFrame
        DataFrame df_panorama_agua.
    municipio : 
    ano_censo : int
        Ano do censo escolar selecionado pelo usuário na interface.
    """
    import streamlit as st
    import pandas as pd
    
    with st.form("pan_agua_relatorio_potavel_censo"):

    st.subheader("Escolas que declaram ofertar água potável no Censo Escolar")
    st.write("Dados disponíveis a partir do ano de 2019.")

    submitted = st.form_submit_button("Gerar Dados")

    if submitted:
        # Garantir que a coluna esteja numérica
        df = df_panorama_financiamento.copy()
        df["indicador_despesa_fundeb_profissionais"] = pd.to_numeric(
            df["indicador_despesa_fundeb_profissionais"].astype(str).str.replace(",", "."),
            errors="coerce"
        )

        # Filtrar por descumprimento (< 70%) a partir de 2021
        df_filtrado = df[
            (df["ano"] >= 2021) &
            (df["indicador_despesa_fundeb_profissionais"] < 70)
        ][["nome", "cod_ibge", "ano", "indicador_despesa_fundeb_profissionais"]].copy()

        if df_filtrado.empty:
            st.warning("Não houve descumprimento para os anos disponíveis.")
        else:
            # Renomear colunas com base no dicionário do projeto
            df_renomeado = df_filtrado.rename(columns=COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO)
            st.dataframe(df_renomeado)