# Panorama Água

def relatorio_agua_dados_brutos(df_agua):
    """
    Relatório que leva em conta apenas a coluna 'IN_AGUA_POTAVEL' do Censo 
    Escolar, que contém a declaração sobre o fornecimento ou não de 
    água potável, sem considerar as fontes de abastecimento.
    
    Parâmetros:
    -----------
    df_agua : pd.DataFrame
        DataFrame do censo escolar contendo as colunas 'NU_ANO_CENSO' e 'IN_AGUA_POTAVEL'.
    """
    import streamlit as st
    from scripts.utils import COLUNAS_RENOMEADAS_CENSO
    from scripts.utils import aplicar_mapeamentos_censo
    
    
    with st.form("form_pan_agua_escolas_censo"):
    
        st.subheader("Escolas que declaram não fornecer Água Potável, segundo os dados brutos do Censo Escolar")
        st.write("Este relatório leva em conta apenas a coluna 'IN_AGUA_POTAVEL' do Censo Escolar, que contém a declaração sobre o fornecimento ou não de água potável, sem considerar as fontes de abastecimento.")

        # Selectbox do Município
        municipios_disponiveis = sorted(df_agua['NO_MUNICIPIO'].unique())

        municipio = st.selectbox(
            "Selecione o Município:",
            options=municipios_disponiveis,
            key="relatorio_escolas_agua_censo_municipio"
        )

        # Selectbox do ano
        anos_disponiveis = sorted(df_agua['NU_ANO_CENSO'].unique())
        ano_mais_recente = max(anos_disponiveis)

        ano_censo = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="relatorio_escolas_agua_censo_ano"
        )

        colunas_relatorio = [
            'NU_ANO_CENSO', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'CO_ENTIDADE',
            'TP_DEPENDENCIA', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA',
            'DS_ENDERECO', 'IN_LOCAL_FUNC_PREDIO_ESCOLAR', 'TP_OCUPACAO_PREDIO_ESCOLAR',
            'IN_AGUA_POTAVEL'
        ]

        # Botão
        submitted = st.form_submit_button("Gerar Relatório ")

        if submitted:
            df_filtrado = df_agua[
                (df_agua["NO_MUNICIPIO"] == municipio) &
                (df_agua["NU_ANO_CENSO"] == ano_censo) &
                (df_agua["IN_AGUA_POTAVEL"] == 0)
            ].copy()

            aplicar_mapeamentos_censo(df_filtrado)
            df_filtrado = df_filtrado[colunas_relatorio].rename(columns=COLUNAS_RENOMEADAS_CENSO)
            st.write(df_filtrado.reset_index(drop=True))

def relatorio_agua_fontes(df_agua):
    """
    Relatório sobre o fornecimento de água potável segundo as fontes de abastecimento.
    
    Parâmetros:
    -----------
    df_agua : pd.DataFrame
    """
    import streamlit as st
    from scripts.utils import COLUNAS_RENOMEADAS_CENSO
    from scripts.utils import aplicar_mapeamentos_censo
    
    with st.form("form_pan_agua_escolas_fontes"):

        st.subheader("Escolas que declaram fontes de abastecimento impróprias para o consumo")
        st.write("Este relatório leva em conta as fontes de abastecimento declaradas pelas escolas ao Censo Escolar. São mostradas as fontes consideradas impróprias para o consumo humano.")

        # Selectbox do Município
        municipios_disponiveis = sorted(df_agua['NO_MUNICIPIO'].unique())

        municipio = st.selectbox(
            "Selecione o Município:",
            options=municipios_disponiveis,
            key="relatorio_escolas_agua_fontes_municipio"
        )

        # Selectbox do ano
        anos_disponiveis = sorted(df_agua['NU_ANO_CENSO'].unique())
        ano_mais_recente = max(anos_disponiveis)

        ano_censo = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="relatorio_escolas_agua_fontes_ano"
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
            df_filtrado = df_agua[
                (df_agua["NO_MUNICIPIO"] == municipio) &
                (df_agua["NU_ANO_CENSO"] == ano_censo) &
                (df_agua["IN_AGUA_REDE_PUBLICA"] != 1) &
                (df_agua["IN_AGUA_POCO_ARTESIANO"] != 1)
            ].copy()

            aplicar_mapeamentos_censo(df_filtrado)
            df_filtrado = df_filtrado[colunas_relatorio].rename(columns=COLUNAS_RENOMEADAS_CENSO)
            st.write(df_filtrado.reset_index(drop=True))
            
def relatorio_pdde_agua_escolas_contempladas(df_agua, df_equidade):
    """Relatório das escolas contempladas com o pdde água, por Município e ano.

    Parâmetros:
    -----------
        df_agua : pd.DataFrame 
        df_equidade : pd.DataFrame
    """
    import streamlit as st
        
    with st.form("form_pan_agua_pdde_agua_escolas_contempladas"):
    
        st.subheader("Escolas que receberam recursos do PDDE Água")
        st.write("Este relatório enumera as escolas que receberam os recursos do PDDE Água, por Município.")

        # Selectbox do Município
        municipios_disponiveis = sorted(df_agua['NO_MUNICIPIO'].unique())

        municipio = st.selectbox(
            "Selecione o Município:",
            options=municipios_disponiveis,
            key="relatorio_escolas_pdde_agua_contempladas_municipio"
        )

        # Selectbox do ano
        anos_disponiveis = sorted(df_agua['NU_ANO_CENSO'].unique())
        ano_mais_recente = max(anos_disponiveis)

        ano = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="relatorio_escolas_pdde_agua_contempladas_ano"
        )

        colunas_relatorio = ["Ano", "Município", "Código Escola", "Nome Escola",
                             "Quantidade Alunos", "Rede Atendimento", "CNPJ Executora",
                             "Nome Executora", "Destinação", "Valor Total", 
                             "Data da Ord. de Pagamento"        
        ]

        # Botão
        submitted = st.form_submit_button("Gerar Relatório ")

        if submitted:
            filtro_agua = df_equidade["Destinação"].str.contains(r"\b(água|agua)\b", case=False, na=False, regex=True).copy()
            df_pdde_agua = df_equidade[filtro_agua]
            df_filtrado = df_pdde_agua[
                (df_pdde_agua["Município"] == municipio) &
                (df_pdde_agua["Ano"] == ano)
            ].copy()

            if df_filtrado.empty:
                st.warning(f"O Município de {municipio} não recebeu recursos do PDDE Água no ano de {ano}.")

            else:
                st.write(df_filtrado[colunas_relatorio].reset_index(drop=True))
                
def relatorio_pdde_agua_escolas_elegiveis(df_agua, df_uex, df_equidade):
    """
    Relatório das escolas elegíveis ao PDDE água, por Município e ano.

    Parâmetros:
    -----------
        df_agua : pd.DataFrame
    """
    import streamlit as st
    from scripts.utils import COLUNAS_RENOMEADAS_CENSO
    from scripts.utils import aplicar_mapeamentos_censo
    
    with st.form("form_pan_agua_escolas_elegiveis"):
        
        st.subheader("Escolas elegíveis ao PDDE Água")
        st.write("Este relatório detalha as escolas que poderiam acessar o PDDE Água imediatamente e não o fazem por falta de adesão.")

        # Selectbox do Município
        municipios_disponiveis = sorted(df_agua['NO_MUNICIPIO'].unique())

        municipio = st.selectbox(
            "Selecione o Município:",
            options=municipios_disponiveis,
            key="relatorio_escolas_elegiveis_municipio"
        )

        # Selectbox do ano
        anos_disponiveis = sorted(df_agua['NU_ANO_CENSO'].unique())
        ano_mais_recente = max(anos_disponiveis)

        ano_censo = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="relatorio_escolas_elegiveis_ano"
        )

        colunas_relatorio = [
            'NU_ANO_CENSO', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'CO_ENTIDADE',
            'TP_DEPENDENCIA', 'CNPJ UEX', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA',
            'DS_ENDERECO', 'IN_LOCAL_FUNC_PREDIO_ESCOLAR', 'TP_OCUPACAO_PREDIO_ESCOLAR',
            'IN_AGUA_POTAVEL', 'IN_AGUA_REDE_PUBLICA', 'IN_AGUA_POCO_ARTESIANO',
            'IN_AGUA_CACIMBA', 'IN_AGUA_FONTE_RIO', 'IN_AGUA_INEXISTENTE',
            'IN_AGUA_CARRO_PIPA'
        ]

        # Botão
        submitted = st.form_submit_button("Gerar Relatório ")

        if submitted:
            df_agua_ano = df_agua[df_agua["NU_ANO_CENSO"] == ano_censo].copy()
            df_uex_ano = df_uex[df_uex["Ano"] == ano_censo].copy()
            df_eq_ano = df_equidade[df_equidade["Ano"] == ano_censo].copy()

            # Renomear colunas para merge
            df_uex_ano = df_uex_ano.rename(columns={"Código Escola": "CO_ENTIDADE"})
            df_eq_ano = df_eq_ano.rename(columns={"Código Escola": "CO_ENTIDADE"})

            # Merge dos 3 dataframes
            df_merged = df_agua_ano.merge(df_uex_ano, on="CO_ENTIDADE", how="left", suffixes=('', '_uex'))
            df_merged = df_merged.merge(df_eq_ano, on="CO_ENTIDADE", how="left", suffixes=('', '_eq'))

            # Coluna auxiliar: acessou PDDE com destinação para água
            df_merged["acessou_pdde_agua"] = df_merged["Destinação"].fillna("").str.contains(r"\b(água|agua)\b", case=False)

            # Coluna auxiliar: tem UEX própria
            df_merged["tem_uex"] = df_merged["CNPJ UEX"].notna() & (df_merged["CNPJ UEX"] != df_merged["CNPJ EEX"])

            # Escolas elegíveis
            df_elegiveis = df_merged[
                (df_merged["NO_MUNICIPIO"] == municipio) &
                (df_merged["NU_ANO_CENSO"] == ano_censo) &
                (df_merged["TP_LOCALIZACAO"] == 2) &
                (df_merged["IN_AGUA_POTAVEL"] == 0) &
                (df_merged["TP_OCUPACAO_PREDIO_ESCOLAR"] == 1) &
                (df_merged["tem_uex"] == True) &
                (~df_merged["acessou_pdde_agua"]) &
                (
                    (
                        (df_merged["IN_AGUA_POCO_ARTESIANO"] != 1) &
                        (df_merged["IN_AGUA_REDE_PUBLICA"] != 1)
                    ) 
                )
            ].copy()
        
            if df_elegiveis.empty:
                st.warning(f"O Município de {municipio} não possui escolas elegíveis ao PDDE Água no ano de {ano_censo}.")
            else: 
                aplicar_mapeamentos_censo(df_elegiveis)
                df_elegiveis = df_elegiveis[colunas_relatorio].rename(columns=COLUNAS_RENOMEADAS_CENSO)
                st.write(df_elegiveis.reset_index(drop=True))
            
def relatorio_pdde_agua_escolas_potenciais(df_agua, df_uex, df_equidade):
    """
    Relatório das escolas elegíveis ao pdde água, por Município e ano.

    Parâmetros:
    -----------
        df_agua : pd.DataFrame
        df_uex : pd.DataFrame
        df_equidade : pd.DataFrame
    """
    import streamlit as st
    from scripts.utils import COLUNAS_RENOMEADAS_CENSO
    from scripts.utils import aplicar_mapeamentos_censo
    
    with st.form("form_pan_agua_escolas_potenciais"):
        
        st.subheader("Escolas potenciais ao PDDE Água")
        st.write("Este relatório detalha as escolas que poderiam acessar o PDDE Água e não o fazem por erro no preenchimento do Censo Escolar ou por falta de Unidade Executora.")

        # Selectbox do Município
        municipios_disponiveis = sorted(df_agua['NO_MUNICIPIO'].unique())

        municipio = st.selectbox(
            "Selecione o Município:",
            options=municipios_disponiveis,
            key="relatorio_escolas_potenciais_municipio"
        )

        # Selectbox do ano
        anos_disponiveis = sorted(df_agua['NU_ANO_CENSO'].unique())
        ano_mais_recente = max(anos_disponiveis)

        ano_censo = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="relatorio_escolas_potenciais_ano"
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
        submitted = st.form_submit_button("Gerar Relatório")

        if submitted:
            df_agua_ano = df_agua[df_agua["NU_ANO_CENSO"] == ano_censo].copy()
            df_uex_ano = df_uex[df_uex["Ano"] == ano_censo].copy()
            df_eq_ano = df_equidade[df_equidade["Ano"] == ano_censo].copy()

            # Renomear colunas para merge
            df_uex_ano = df_uex_ano.rename(columns={"Código Escola": "CO_ENTIDADE"})
            df_eq_ano = df_eq_ano.rename(columns={"Código Escola": "CO_ENTIDADE"})

            # Merge dos 3 dataframes
            df_merged = df_agua_ano.merge(df_uex_ano, on="CO_ENTIDADE", how="left", suffixes=('', '_uex'))
            df_merged = df_merged.merge(df_eq_ano, on="CO_ENTIDADE", how="left", suffixes=('', '_eq'))

            # Coluna auxiliar: acessou PDDE com destinação para água
            df_merged["acessou_pdde_agua"] = df_merged["Destinação"].fillna("").str.contains(r"\b(água|agua)\b", case=False)

            # Coluna auxiliar: tem UEX própria
            df_merged["tem_uex"] = df_merged["CNPJ UEX"].notna() & (df_merged["CNPJ UEX"] != df_merged["CNPJ EEX"])

            df_merged["elegiveis"] = (
                    (df_merged["TP_LOCALIZACAO"] == 2) &
                    (df_merged["IN_AGUA_POTAVEL"] == 0) &
                    (df_merged["TP_OCUPACAO_PREDIO_ESCOLAR"] == 1) &
                    (df_merged["tem_uex"] == True) &
                    (~df_merged["acessou_pdde_agua"]) &
                    (
                        (
                            (df_merged["IN_AGUA_POCO_ARTESIANO"] != 1) &
                            (df_merged["IN_AGUA_REDE_PUBLICA"] != 1)
                        ) 
                    )
                )
        
            df_potencial = df_merged[(
                (df_merged["NO_MUNICIPIO"] == municipio) &
                (df_merged["NU_ANO_CENSO"] == ano_censo) &
                (df_merged["TP_LOCALIZACAO"] == 2) &
                (~df_merged["acessou_pdde_agua"]) &
                (~df_merged["elegiveis"]) &
                (
                    (df_merged["IN_AGUA_POCO_ARTESIANO"] != 1) &
                    (df_merged["IN_AGUA_REDE_PUBLICA"] != 1) 
                )
            )
            ].copy()
            
            if df_potencial.empty:
                st.warning(f"O Município de {municipio} não  possui escolas potenciais ao PDDE Água no ano de {ano_censo}.")
            else: 
                aplicar_mapeamentos_censo(df_potencial)
                df_potencial = df_potencial[colunas_relatorio].rename(columns=COLUNAS_RENOMEADAS_CENSO)
                st.write(df_potencial.reset_index(drop=True))

def relatorio_pdde_escolas_sem_uex(df_agua, df_uex):
    """
    Relatório das escolas sem Unidade Executora, por Município e ano.

    Parâmetros:
    -----------
        df_agua : pd.DataFrame
        df_uex : pd.DataFrame
    """
    import streamlit as st
    from scripts.utils import COLUNAS_RENOMEADAS_CENSO
    from scripts.utils import aplicar_mapeamentos_censo
    
    with st.form("form_pan_agua_escolas_sem_uex"):
        
        st.subheader("Escolas sem Unidade Executora")
        st.write("Este relatório detalha as escolas que não possuem Unidade Executora.")

        # Selectbox do Município
        municipios_disponiveis = sorted(df_agua['NO_MUNICIPIO'].unique())

        municipio = st.selectbox(
            "Selecione o Município:",
            options=municipios_disponiveis,
            key="relatorio_escolas_sem_uex_municipio"
        )

        # Selectbox do ano
        anos_disponiveis = sorted(df_agua['NU_ANO_CENSO'].unique())
        ano_mais_recente = max(anos_disponiveis)

        ano_censo = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="relatorio_escolas_sem_uex_ano"
        )

        colunas_relatorio = [
            'NU_ANO_CENSO', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'CO_ENTIDADE',
            'TP_DEPENDENCIA', 'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA',
            'DS_ENDERECO', 'QT_MAT_BAS', 'CNPJ UEX', 'Razão Social'
        ]
        
        # Botão
        submitted = st.form_submit_button("Gerar Relatório")

        if submitted:
            df_agua_ano = df_agua[df_agua["NU_ANO_CENSO"] == ano_censo].copy()
            df_uex_ano = df_uex[df_uex["Ano"] == ano_censo].copy()
            
            # Renomear colunas para merge
            df_uex_ano = df_uex_ano.rename(columns={"Código Escola": "CO_ENTIDADE"})
            
            # Merge dos 3 dataframes
            df_merged = df_agua_ano.merge(df_uex_ano, on="CO_ENTIDADE", how="left", suffixes=('', '_uex'))
            
            # Coluna auxiliar: tem UEX própria
            df_merged["tem_uex"] = df_merged["CNPJ UEX"].notna() & (df_merged["CNPJ UEX"] != df_merged["CNPJ EEX"])

            df_filtrado = df_merged[(
                (df_merged["NO_MUNICIPIO"] == municipio) &
                (df_merged["NU_ANO_CENSO"] == ano_censo) &
                (df_merged["tem_uex"] == False) 
            )
            ].copy()
            
            if df_filtrado.empty:
                st.warning(f"Todas as escolas do Município de {municipio} estão vinculadas a alguma UEx no ano de {ano_censo}.")
            else: 
                aplicar_mapeamentos_censo(df_filtrado)
                df_filtrado = df_filtrado[colunas_relatorio].rename(columns=COLUNAS_RENOMEADAS_CENSO)
                st.write(df_filtrado.reset_index(drop=True))

def relatorio_pdde_escolas_sem_uex_proprias(df_agua, df_uex):
    """
    Relatório das escolas com mais de 50 alunos sem Unidade Executora própria, por Município e ano.

    Parâmetros:
    -----------
        df_agua : pd.DataFrame
        df_uex : pd.DataFrame
    """
    import streamlit as st
    from scripts.utils import COLUNAS_RENOMEADAS_CENSO
    from scripts.utils import aplicar_mapeamentos_censo
    
    with st.form("form_pan_agua_escolas_sem_uex_proprias"):
        
        st.subheader("Escolas com mais de 50 alunos sem Unidade Executora própria")
        st.write("Este relatório detalha as escolas que possuem mais de cinquenta alunos matriculados e que não possui Unidade Executora própria.")

        # Selectbox do Município
        municipios_disponiveis = sorted(df_agua['NO_MUNICIPIO'].unique())

        municipio = st.selectbox(
            "Selecione o Município:",
            options=municipios_disponiveis,
            key="relatorio_escolas_sem_uex_propria_municipio"
        )

        # Selectbox do ano
        anos_disponiveis = sorted(df_agua['NU_ANO_CENSO'].unique())
        ano_mais_recente = max(anos_disponiveis)

        ano_censo = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="relatorio_escolas_sem_uex_propria_ano"
        )

        colunas_relatorio = [
            'NU_ANO_CENSO', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'CO_ENTIDADE',
            'TP_DEPENDENCIA', 'QT_MAT_BAS', 'CNPJ UEX', 'Razão Social', 
            'TP_LOCALIZACAO', 'TP_LOCALIZACAO_DIFERENCIADA', 'DS_ENDERECO'
        ]
        
        # Botão
        submitted = st.form_submit_button("Gerar Relatório")

        if submitted:
            # Filtra os DataFrames pelo ano selecionado
            df_agua_ano = df_agua[df_agua["NU_ANO_CENSO"] == ano_censo].copy()
            df_uex_ano = df_uex[df_uex["Ano"] == ano_censo].copy()

            # Renomear colunas para merge
            df_uex_ano = df_uex_ano.rename(columns={"Código Escola": "CO_ENTIDADE"})

            # Merge dos dataframes
            df_merged = df_agua_ano.merge(df_uex_ano, on="CO_ENTIDADE", how="left", suffixes=('', '_uex'))

            # 🔹 Filtrar somente o município selecionado (para limitar a contagem de CNPJs)
            df_mun = df_merged[df_merged["NO_MUNICIPIO"] == municipio].copy()

            # 🔹 Contar quantas vezes cada CNPJ UEX aparece dentro do município e ano
            cnpjs_repetidos = (
                df_mun["CNPJ UEX"]
                .value_counts()
                .loc[lambda x: x > 1]  # consórcios (repetidos)
                .index
            )

            # 🔹 Filtrar escolas que atendem às condições:
            df_filtrado = df_mun[
                (df_mun["QT_MAT_BAS"] > 50) &
                (
                    (df_mun["CNPJ UEX"].isin(cnpjs_repetidos)) |       # CNPJ aparece mais de uma vez
                    (df_mun["CNPJ UEX"].isna()) |                      # CNPJ válido
                    (df_mun["CNPJ UEX"] == df_mun["CNPJ EEX"])
                )
            ].copy()

            # 🔹 Exibir resultado
            if df_filtrado.empty:
                st.warning(f"O Município de {municipio} não possui escolas com mais de 50 alunos que compartilham a mesma Unidade Executora (UEX) no ano de {ano_censo}.")
            else:
                aplicar_mapeamentos_censo(df_filtrado)
                df_filtrado = df_filtrado[colunas_relatorio].rename(columns=COLUNAS_RENOMEADAS_CENSO)
                st.write(df_filtrado.reset_index(drop=True))
                
def relatorio_pdde_agua_escolas_contempladas_irregulares(df_agua, df_equidade):
    """
    Relatório das escolas contempladas com o pdde água, por Município e ano,
    que declaram não fornecer água potável ou que declaram fontes impróprias de
    abastecimento

    Parâmetros:
    -----------
        df_agua : pd.DataFrame 
        df_equidade : pd.DataFrame
    """
    import streamlit as st
        
    with st.form("form_pan_agua_pdde_agua_escolas_contempladas_irregulares"):
    
        st.subheader("👀 Escolas que receberam recursos do PDDE Água e declaram não fornecer água potável")
        st.write("Este relatório enumera as escolas que receberam os recursos do PDDE Água, mas que declaram não fornecer água potável ou que possuem fontes de abastecimento impróprias para o consumo.")

        # Selectbox do Município
        municipios_disponiveis = sorted(df_agua['NO_MUNICIPIO'].unique())

        municipio = st.selectbox(
            "Selecione o Município:",
            options=municipios_disponiveis,
            key="relatorio_escolas_pdde_agua_irregulares_municipio"
        )

        # Selectbox do ano
        anos_disponiveis = sorted(df_agua['NU_ANO_CENSO'].unique())
        ano_mais_recente = max(anos_disponiveis)

        ano = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="relatorio_escolas_pdde_agua_irregulares_ano"
        )

        colunas_relatorio = ["Ano", "Município", "Código Escola", "Nome Escola",
                             "Quantidade Alunos", "Rede Atendimento", "CNPJ Executora",
                             "Nome Executora", "Destinação", "Valor Total", 
                             "Data da Ord. de Pagamento", "IN_AGUA_POTAVEL", "IN_AGUA_REDE_PUBLICA", 
                             "IN_AGUA_POCO_ARTESIANO", "IN_AGUA_CACIMBA", "IN_AGUA_FONTE_RIO", 
                             "IN_AGUA_INEXISTENTE", "IN_AGUA_CARRO_PIPA"
        ]

        # Botão
        submitted = st.form_submit_button("Gerar Relatório ")

        if submitted:
            df_eq_agua = df_equidade.merge(
                df_agua,
                how="left",
                left_on=["Código Escola", "Ano"],
                right_on=["CO_ENTIDADE", "NU_ANO_CENSO"]
            )

            filtro_agua = df_eq_agua["Destinação"].str.contains(r"\b(água|agua)\b", case=False, na=False, regex=True)
            df_eq_agua = df_eq_agua[filtro_agua]
            df_filtrado = df_eq_agua[
                (df_eq_agua["Município"] == municipio) &
                (df_eq_agua["Ano"] == ano) &
                (
                    (df_eq_agua["IN_AGUA_POTAVEL"] == 0) |
                    (
                        (df_eq_agua["IN_AGUA_REDE_PUBLICA"] != 1) &
                        (df_eq_agua["IN_AGUA_POCO_ARTESIANO"] != 1)
                    )
                )
            ].copy()

            if df_filtrado.empty:
                st.warning(f"Nenhuma escola do Município de {municipio} recebeu recursos do PDDE Água no ano de {ano}.")

            else:
                st.write(df_filtrado[colunas_relatorio].reset_index(drop=True))
                
# escolas que não possuem nenhuma UEx

# escolas com mais de 50 alunos que não possuem UEx própria (integram consorcios)