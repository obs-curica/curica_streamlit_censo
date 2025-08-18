

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
    "valor_receita_nao_aplicada": "Receita Fundeb Não Aplicada",
    "indicador_despesa_fundeb_profissionais": "% Gasto c/ Profissionais",
    "valor_receita_salario_educacao": "Receita Salário-Educação",
    "valor_receita_pdde": "PDDE",
    "valor_receita_pnae": "PNAE",
    "valor_receita_pnate": "PNATE",
    "valor_receita_outras_fnde": "Outras Receitas FNDE",
    "valor_receita_convenios": "Convênios",
    "valor_receita_royalties": "Royalties",
    "valor_receita_operacao_credito": "Operações de Crédito",
    "valor_receita_outras_outras": "Outras Receitas",
    "tipo_ente": "Tipo de Ente",
    "valor_total_receitas_adicionais": "Total Receitas Adicionais",
    "valor_total_receita_educacao": "Total Receita Educação"
}


def renomear_colunas_financiamento(df):
    """
    Renomeia as colunas do DataFrame para nomes mais legíveis,
    conforme o dicionário COLUNAS_RENOMEADAS_FINANCIAMENTO.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame original com nomes técnicos das colunas.

    Retorno:
    --------
    pd.DataFrame
        DataFrame com colunas renomeadas para exibição amigável.
    """
    return df.rename(columns=COLUNAS_RENOMEADAS_FINANCIAMENTO)
