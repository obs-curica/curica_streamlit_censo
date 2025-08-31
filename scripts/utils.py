import pandas as pd
import streamlit as st


# Função para carregar os dados para páginas do projeto
@st.cache_data
def carregar_dados(url):
    """Carrega dados de um arquivo CSV a partir de uma URL fornecida."""
    import pandas as pd
    import streamlit as st
        # Carregar os dados diretamente do link fornecido
    df = pd.read_csv(url, delimiter=';', encoding='utf-8', low_memory=False)
    
    return df


# Dicionário de renomeação de colunas para exibição amigável ao usuário
COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO = {
    "nome": "Ente",
    "cod_ibge": "Cód. IBGE",
    "ano": "Ano",
    "valor_receita_impostos": "Receita de Impostos",
    "valor_repasse_fundeb": "Repasse Fundeb",
    "valor_minimo_mde": "Mínimo MDE (5%)",
    "valor_receita_vaaf": "Receita VAAF",
    "valor_receita_vaat": "Receita VAAT",
    "valor_receita_vaar": "Receita VAAR",
    "valor_receita_total_fundeb": "Total Fundeb",
    "valor_total_despesa_impostos": "Despesa MDE Impostos",
    "valor_receita_nao_aplicada": "Fundeb Não Aplicado",
    "valor_limite_const_exigido": "Mínimo Constitucional Exigido (25%)",
    "valor_limite_const_aplicado": "Mínimo Constitucional Aplicado",
    "indicador_limite_constitucional": "Indicador Mínimo Constitucional (25%)",
    "indicador_despesa_fundeb_profissionais": "% Gasto com Profissionais",
    "indicador_receita_nao_aplicada": "% Fundeb Não Aplicado",
    "valor_receita_salario_educacao": "Salário-Educação",
    "valor_receita_pdde": "PDDE",
    "valor_receita_pnae": "PNAE",
    "valor_receita_pnate": "PNATE",
    "valor_receita_outras_fnde": "Outras FNDE",
    "valor_receita_convenios": "Convênios",
    "valor_receita_royalties": "Royalties",
    "valor_receita_operacao_credito": "Op. de Crédito",
    "valor_receita_outras_outras": "Outras Receitas",
    "valor_total_receitas_adicionais": "Total Receitas Adicionais",
    "valor_total_receita_educacao": "Total Receita Educação",
    "tipo_ente": "Tipo de Ente"
}



def renomear_colunas_financiamento(df):
    """
    Renomeia as colunas do DataFrame para nomes mais legíveis,
    conforme o dicionário COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame original com nomes técnicos das colunas.

    Retorno:
    --------
    pd.DataFrame
        DataFrame com colunas renomeadas para exibição amigável.
    """
    return df.rename(columns=COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO)
