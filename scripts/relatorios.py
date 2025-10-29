# Panorama Água

def teste(df):
    # Relatório das escolas elegíveis ao PDDE Água
    import streamlit as st
    import pandas as pd
    from scripts.utils import aplicar_mapeamentos_censo
    from scripts.utils import COLUNAS_RENOMEADAS_CENSO
    
    with st.form("form_pan_agua_teste"):

        st.subheader("Escolas elegíveis ao PDDE Água")
        st.write("Este relatório detalha as escolas que poderiam acessar o PDDE Água imediatamente e não o fazem por falta de adesão.")

        # Selectbox do Município
        municipios_disponiveis = sorted(df['NO_MUNICIPIO'].unique())

        municipio = st.selectbox(
            "Selecione o Município:",
            options=municipios_disponiveis,
            key="relatorio_teste_mun"
        )

        # Selectbox do ano
        anos_disponiveis = sorted(df['NU_ANO_CENSO'].unique())
        ano_mais_recente = max(anos_disponiveis)

        ano_censo = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="relatorio_teste_ano"
        )

        colunas_relatorio = [
            'NU_ANO_CENSO', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'CO_ENTIDADE',
            'TP_DEPENDENCIA', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA',
            'DS_ENDERECO', 'IN_LOCAL_FUNC_PREDIO_ESCOLAR', 'TP_OCUPACAO_PREDIO_ESCOLAR',
            'IN_AGUA_POTAVEL', 'IN_AGUA_REDE_PUBLICA', 'IN_AGUA_POCO_ARTESIANO',
            'IN_AGUA_CACIMBA', 'IN_AGUA_FONTE_RIO', 'IN_AGUA_INEXISTENTE',
            'IN_AGUA_CARRO_PIPA'
        ]

        # Botão
        submitted = st.form_submit_button("Gerar Relatório ")

        if submitted:
            df_filtrado = df[
                (df["NO_MUNICIPIO"] == municipio) &
                (df["NU_ANO_CENSO"] == ano_censo) &
                (df["IN_AGUA_REDE_PUBLICA"] != 1) &
                (df["IN_AGUA_POCO_ARTESIANO"] != 1)
            ].copy()

            aplicar_mapeamentos_censo(df_filtrado)
            df_filtrado = df_filtrado[colunas_relatorio].rename(columns=COLUNAS_RENOMEADAS_CENSO)
            st.write(df_filtrado.reset_index(drop=True))