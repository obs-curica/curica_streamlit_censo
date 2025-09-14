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
# Dicionário de renomeação de colunas do Censo Escolar
COLUNAS_RENOMEADAS_CENSO = {
    "NU_ANO_CENSO": "Ano do Censo",
    "SG_UF": "UF",
    "CO_UF": "Código UF",
    "NO_MUNICIPIO": "Município",
    "CO_MUNICIPIO": "Código Município",
    "NO_ENTIDADE": "Nome da Escola",
    "CO_ENTIDADE": "Código da Escola",
    "TP_DEPENDENCIA": "Dependência Administrativa",
    "TP_LOCALIZACAO": "Localização",
    "TP_LOCALIZACAO_DIFERENCIADA": "Loc. Diferenciada",
    "DS_ENDERECO": "Endereço",
    "NU_ENDERECO": "Número",
    "DS_COMPLEMENTO": "Complemento",
    "NO_BAIRRO": "Bairro",
    "CO_CEP": "CEP",
    "NU_DDD": "DDD",
    "NU_TELEFONE": "Telefone",
    "TP_SITUACAO_FUNCIONAMENTO": "Situação de Funcionamento",
    "CO_ESCOLA_SEDE_VINCULADA": "Escola Sede Vinculada",
    "IN_LOCAL_FUNC_PREDIO_ESCOLAR": "Funciona em Prédio Escolar",
    "TP_OCUPACAO_PREDIO_ESCOLAR": "Ocupação Prédio Escolar",
    "IN_AGUA_POTAVEL": "Água Potável",
    "IN_AGUA_REDE_PUBLICA": "Água Rede Pública",
    "IN_AGUA_POCO_ARTESIANO": "Água Poço Artesiano",
    "IN_AGUA_CACIMBA": "Água Cacimba",
    "IN_AGUA_FONTE_RIO": "Água de Fonte ou Rio",
    "IN_AGUA_INEXISTENTE": "Sem Abastecimento de Água",
    "IN_AGUA_CARRO_PIPA": "Água por Carro Pipa",
    "IN_ENERGIA_REDE_PUBLICA": "Energia Rede Pública",
    "IN_ENERGIA_GERADOR_FOSSIL": "Energia Gerador Fóssil",
    "IN_ENERGIA_RENOVAVEL": "Energia Renovável",
    "IN_ENERGIA_INEXISTENTE": "Sem Energia",
    "IN_ESGOTO_REDE_PUBLICA": "Esgoto Rede Pública",
    "IN_ESGOTO_FOSSA_SEPTICA": "Esgoto Fossa Séptica",
    "IN_ESGOTO_FOSSA_COMUM": "Esgoto Fossa Comum",
    "IN_ESGOTO_FOSSA": "Esgoto Fossa (outros)",
    "IN_ESGOTO_INEXISTENTE": "Sem Esgoto",
    "IN_BANHEIRO": "Banheiro",
    "IN_COZINHA": "Cozinha"
}


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
    "valor_receita_pnae": "PNAE",
    "valor_receita_pdde": "PDDE",
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
