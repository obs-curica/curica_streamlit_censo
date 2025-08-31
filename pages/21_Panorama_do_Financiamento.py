import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import re

from scripts.utils import carregar_dados
from scripts.utils import COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO

from scripts.textos import(
    texto_pan_financiamento_intro, 
    texto_pan_financiamento_fnde_intro,
    texto_pan_financiamento_fnde_analise,
    texto_pan_financiamento_fundeb_intro,
    texto_pan_financiamento_fundeb_analise_1,
    texto_pan_financiamento_fundeb_analise_2,
    texto_pan_financiamento_fundeb_complementacao_intro,
    texto_pan_financiamento_fundeb_complementacao_analise,
    texto_pan_financiamento_receita_minima_impostos_intro,
    texto_pan_financiamento_receita_minima_impostos_analise,
    texto_pan_financiamento_minimo_constitucional_intro,
    texto_pan_financiamento_minimo_constitucional_analise,
    texto_pan_financiamento_salario_educacao_intro,
    texto_pan_financiamento_salario_educacao_analise,
    texto_pan_financiamento_receitas_adicionais_intro,
    texto_pan_financiamento_receitas_adicionais_analise,
    texto_pan_financiamento_execucao_pdde_intro,
    texto_pan_financiamento_execucao_pdde_analise,
    texto_pan_financiamento_responsabilidade_criminal,
    texto_pan_fin_consideracoes_finais_intro,
    texto_pan_fin_consideracoes_finais_analise,
    texto_pan_fin_relatorio_intro
)

from scripts.graficos import(
    grafico_fnde_receita_total,
    grafico_fnde_acoes,
    grafico_fundeb_total_ano,
    grafico_fundeb_total_ente,
    grafico_indicador_despesa_profissionais,
    grafico_percentual_recursos_nao_utilizados,
    grafico_valor_repasse_fundeb,
    grafico_complementacoes_fundeb,
    grafico_valor_receita_impostos,
    grafico_valores_despesa_minima_impostos,
    grafico_valores_limite_constitucional,
    grafico_indicador_limite_constitucional,
    grafico_receita_salario_educacao_ano,
    grafico_receita_salario_educacao_ente,
    grafico_receitas_adicionais_por_ente_ano,
    grafico_receitas_adicionais_evolucao,
    grafico_execucao_pdde_valores,
    grafico_execucao_pdde_porcentagem,
    grafico_receita_total_educacao
)

# Configuração da página
st.set_page_config(page_title="Panorama Financiamento", layout="wide", page_icon="🦜")

# Carregar dados
# df_panorama_financiamento
url_panorama_financiamento = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_financiamento/df_panorama_financiamento.csv"
df_panorama_financiamento = carregar_dados(url_panorama_financiamento)
df_panorama_financiamento['nome'] = df_panorama_financiamento['nome'].astype(str)

# df_receita_fnde
url_receita_fnde = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_financiamento/df_receita_fnde.csv"
df_receita_fnde = carregar_dados(url_receita_fnde)

# df_despesas_fnde
url_despesas_fnde = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_financiamento/df_despesas_fnde.csv"
df_despesas_fnde = carregar_dados(url_despesas_fnde)

# df_execucao_pdde
url_execucao_pdde = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_financiamento/df_execucao_pdde.csv"
df_execucao_pdde = carregar_dados(url_execucao_pdde)

# Título da página
st.title("💲 Considerações Gerais sobre o Financiamento da Educação Básica")

# texto introdutório financiamento
st.write(texto_pan_financiamento_intro())

#++++++++
# Subsção FNDE
st.header("O Fundo Nacional de Desenvolvimento da Educação (FNDE)")

st.write(texto_pan_financiamento_fnde_intro())

col1, col2 = st.columns(2)

with col1:
    grafico_fnde_receita_total(df_receita_fnde)
    
with col2:
    
    anos_disponiveis = sorted(df_despesas_fnde['Ano'].unique())
    ano_mais_recente = max(anos_disponiveis)

    ano = st.selectbox(
        "Selecione o ano:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="fnde_ano"
    )

    grafico_fnde_acoes(df_despesas_fnde, ano)



st.write(texto_pan_financiamento_fnde_analise())



#++++++++
# Subseção Fundeb
st.header("Fundeb")
st.write(texto_pan_financiamento_fundeb_intro())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Fundeb Total por Ano")
    anos_disponiveis = sorted(df_panorama_financiamento['ano'].unique())
    ano_mais_recente = max(anos_disponiveis)

    ano = st.selectbox(
        "Selecione o ano:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="fundeb_ano"
    )

    # Gráfico do Fundeb total por ano
    grafico_fundeb_total_ano(df_panorama_financiamento, ano)
    
with col2:
    st.subheader("Fundeb Total por Ente")
    
    entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    
    entes = st.selectbox(
        "Selecione o ente:",
        options=entes_disponiveis,
        key="fundeb_ente"
    )
    
    grafico_fundeb_total_ente(df_panorama_financiamento, entes)
        
st.write(texto_pan_financiamento_fundeb_analise_1())

# Gráficos do Fundeb Estado e Municipios sob demanda
entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    
entes = st.selectbox(
    "Selecione o ente:",
    options=entes_disponiveis,
    key="fundeb_despesa_profissionais"
)

col1, col2 = st.columns(2)

with col1:
    grafico_indicador_despesa_profissionais(df_panorama_financiamento, entes)
    
with col2:
    grafico_percentual_recursos_nao_utilizados(df_panorama_financiamento, entes)

st.write(texto_pan_financiamento_fundeb_analise_2())

st.subheader("Complementações do Fundeb: VAAT, VAAF e VAAR")

st.write(texto_pan_financiamento_fundeb_complementacao_intro())

entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    
entes = st.selectbox(
    "Selecione o ente:",
    options=entes_disponiveis,
    key="complementacao_ente"
)

col1, col2 = st.columns(2)

with col1:
    grafico_valor_repasse_fundeb(df_panorama_financiamento, entes)

with col2:
    grafico_complementacoes_fundeb(df_panorama_financiamento, entes)
    
st.write(texto_pan_financiamento_fundeb_complementacao_analise())


#+++++++++
# Subseção Receita Impostos 5%
st.header("Receita mínima proveniente de impostos")

st.write(texto_pan_financiamento_receita_minima_impostos_intro())

entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    
entes = st.selectbox(
    "Selecione o ente:",
    options=entes_disponiveis,
    key="receita_impostos_ente"
)

col1, col2 = st.columns(2)

with col1:
    grafico_valor_receita_impostos(df_panorama_financiamento, entes)
    
with col2:
    grafico_valores_despesa_minima_impostos(df_panorama_financiamento, entes)

st.write(texto_pan_financiamento_receita_minima_impostos_analise())


#++++++++
# Subseção Mínimo Constitucional

st.header("Aplicação do Mínimo Constitucional de 25% da receita de impostos")

st.write(texto_pan_financiamento_minimo_constitucional_intro())

entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    
entes = st.selectbox(
    "Selecione o ente:",
    options=entes_disponiveis,
    key="minimo_constitucional_ente"
)

col1, col2 = st.columns(2)

with col1:
    grafico_valores_limite_constitucional(df_panorama_financiamento, entes)
    
with col2:
    grafico_indicador_limite_constitucional(df_panorama_financiamento, entes)

st.write(texto_pan_financiamento_minimo_constitucional_analise())


#++++++++
# Subseção Salário Educação
st.header("Salário-Educação")

st.write(texto_pan_financiamento_salario_educacao_intro())


col1, col2 = st.columns(2)

with col1:
    st.subheader("Salário-Educação por Ano")
    anos_disponiveis = sorted(df_panorama_financiamento['ano'].unique())
    ano_mais_recente = max(anos_disponiveis)

    ano = st.selectbox(
        "Selecione o ano:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="salario_educacao_ano"
    )

    grafico_receita_salario_educacao_ano(df_panorama_financiamento, ano)

with col2:
    st.subheader("Salário-Educação por Ente")
    entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    
    entes = st.selectbox(
        "Selecione o ente:",
        options=entes_disponiveis,
        key="salario_educacao_ente"
    )

    grafico_receita_salario_educacao_ente(df_panorama_financiamento, entes)
    
st.write(texto_pan_financiamento_salario_educacao_analise())


#++++++++
# Subseção Programas, Projetos e Ações do FNDE
st.header("Outras fontes de receita")

st.write(texto_pan_financiamento_receitas_adicionais_intro())

col1, col2 = st.columns(2)

with col1:
    entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    entes = st.selectbox(
        "Selecione o ente:",
        options=entes_disponiveis,
        key="outras_receitas_geral_ente"
    )

    anos_disponiveis = sorted(df_panorama_financiamento['ano'].unique())
    ano_mais_recente = max(anos_disponiveis)
    ano = st.selectbox(
        "Selecione o ano:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="outras_receitas_geral_ano"
    )

    grafico_receitas_adicionais_por_ente_ano(df_panorama_financiamento, entes, ano)
    
with col2:
    entes_disponiveis = sorted(df_panorama_financiamento['nome'].unique())
    entes = st.selectbox(
        "Selecione o ente:",
        options=entes_disponiveis,
        key="outras_receitas_evolucao_ente"
    )
    
    # Código do selectbox para categorias de receita adicional
    # Lista técnica das categorias de receita adicional
    colunas_receitas = [
        "valor_receita_pnae",
        "valor_receita_pnate",
        "valor_receita_pdde",
        "valor_receita_convenios",
        "valor_receita_outras_fnde",
        "valor_receita_royalties",
        "valor_receita_operacao_credito",
        "valor_receita_outras_outras"
    ]
    
    # Cria dicionário invertido para mapeamento reverso
    NOMES_RENOMEADOS_INV = {v: k for k, v in COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO.items() if k in colunas_receitas}
    
    # Opções legíveis
    opcoes_legiveis = list(NOMES_RENOMEADOS_INV.keys())
    
    # Seletor com nome amigável
    categoria_legivel = st.selectbox("Selecione a categoria de receita adicional:", opcoes_legiveis)
    
    # Converter de volta para nome técnico
    categoria_tecnica = NOMES_RENOMEADOS_INV[categoria_legivel]
    
    # Chamada do gráfico com nome técnico
    grafico_receitas_adicionais_evolucao(df_panorama_financiamento, entes, categoria_tecnica)
    
st.write(texto_pan_financiamento_receitas_adicionais_analise())

st.subheader("Exemplo de deficiência na execução dos recursos do PDDE")


#++++++++
# Subseção PDDE
st.write(texto_pan_financiamento_execucao_pdde_intro())

col1, col2 = st.columns(2)

with col1:
    entes_disponiveis = sorted(df_execucao_pdde['nome'].unique())
    entes = st.selectbox(
        "Selecione o ente:",
        options=entes_disponiveis,
        key="execucao_pdde_valores_ente"
    )

    anos_disponiveis = sorted(df_execucao_pdde['ano'].unique())
    ano_mais_recente = max(anos_disponiveis)
    ano = st.selectbox(
        "Selecione o ano:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="execucao_pdde_valores_ano"
    )
    
    grafico_execucao_pdde_valores(df_execucao_pdde, ano, entes)

with col2:
    anos_disponiveis = sorted(df_execucao_pdde['ano'].unique())
    ano_mais_recente = max(anos_disponiveis)
    ano = st.selectbox(
        "Selecione o ano:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key="execucao_pdde_porcentagem_ano"
    )
    
    grafico_execucao_pdde_porcentagem(df_execucao_pdde, ano)

st.write(texto_pan_financiamento_execucao_pdde_analise())


#++++++++
# Subseção Responsabilidade Criminal
st.header("Responsabilização dos gestores")
st.write(texto_pan_financiamento_responsabilidade_criminal())


#++++++++
# Subseção Considerações finais
st.header("Considerações finais")
st.write(texto_pan_fin_consideracoes_finais_intro())

col1, col2 = st.columns(2)
with col1:
    entes_disponiveis = sorted(df_execucao_pdde['nome'].unique())
    entes = st.selectbox(
        "Selecione o ente:",
        options=entes_disponiveis,
        key="consideracoes_ente"
    )
    
    grafico_receita_total_educacao(df_panorama_financiamento, entes)
    
st.write(texto_pan_fin_consideracoes_finais_analise())


#++++++++
# Subseção Relatórios
st.header("Geração de relatórios")
st.write(texto_pan_fin_relatorio_intro())

# Relatório "Descumprimento da despesa com profissionais da educação"
with st.form("pan_fin_form_remuneracao_profissionais"):

    st.subheader("Descumprimento da despesa mínima com profissionais da educação")
    st.write("Entes que descumpriram a despesa mínima de 70% com remuneração dos profissionais da educação. Dados disponíveis a partir do ano de 2021.")

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


# Relatório Máximo de 10% de superavit
with st.form("pan_fin_form_superavit"):

    st.subheader("Descumprimento do máximo de 10% de superávit no exercício")
    st.write("Entes que descumpriram o valor máximo permitido. Dados disponíveis a partir do ano de 2021.")

    submitted = st.form_submit_button("Gerar Dados")

    if submitted:
        # Copiar o DataFrame
        df = df_panorama_financiamento.copy()

        # Garantir que as colunas estejam numéricas
        colunas_max_superavit = ["valor_receita_total_fundeb", "valor_receita_nao_aplicada", "indicador_receita_nao_aplicada"]
        for col in colunas_max_superavit:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(",", "."),
                errors="coerce"
            )

        # Filtrar entes que não atingiram o mínimo
        df_filtrado = df[
            (df["ano"] >= 2021) &
            (df["indicador_receita_nao_aplicada"] > 10)
        ][["nome", "cod_ibge", "ano", "valor_receita_total_fundeb", "valor_receita_nao_aplicada", "indicador_receita_nao_aplicada"]].copy()

        if df_filtrado.empty:
            st.warning("Não houve descumprimento para os anos disponíveis.")
        else:
            # Renomear colunas com base no dicionário do projeto
            df_renomeado = df_filtrado.rename(columns=COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO)
            st.dataframe(df_renomeado)


# Relatório "Descumprimento do Mínimo Constitucional"
with st.form("pan_fin_form_minimo_constitucionas"):

    st.subheader("Descumprimento do Mínimo Constitucional (25%)")
    st.write("Entes que descumpriram a aplicação mínima de 25% exigida. Dados disponíveis a partir do ano de 2021.")

    submitted = st.form_submit_button("Gerar Dados")

    if submitted:
        # Copiar o DataFrame
        df = df_panorama_financiamento.copy()

        # Garantir que as colunas estejam numéricas
        colunas_min_const = ["valor_limite_const_exigido", "valor_limite_const_aplicado"]
        for col in colunas_min_const:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(",", "."),
                errors="coerce"
            )

        # Filtrar entes que não atingiram o mínimo
        df_filtrado = df[
            (df["ano"] >= 2021) &
            (df["indicador_limite_constitucional"] < 25)
        ][["nome", "cod_ibge", "ano", "valor_limite_const_exigido", "valor_limite_const_aplicado", "indicador_limite_constitucional"]].copy()

        if df_filtrado.empty:
            st.warning("Não houve descumprimento para os anos disponíveis.")
        else:
            # Renomear colunas com base no dicionário do projeto
            df_renomeado = df_filtrado.rename(columns=COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO)
            st.dataframe(df_renomeado)

            
# Relatório "Dados Financeiros"
with st.form("pan_fin_form_dados_financeiros"):

    st.subheader("Dados Financeiros")
    st.write("Aqui você gera uma tabela com todos os dados utilizados neste Panorama. Estão disponíveis os dados a partir do ano de 2021.")

    col1, col2 = st.columns(2)

    with col1:
        entes_disponiveis = sorted(df_panorama_financiamento["nome"].unique())
        ente_selecionado = st.multiselect(
            "Selecione o(s) ente(s):",
            options=entes_disponiveis,
            key="relatorio_financiamento_ente"
        )

    with col2:
        anos_disponiveis = sorted(df_panorama_financiamento["ano"].unique())
        anos_selecionados = st.multiselect(
            "Selecione o(s) ano(s):",
            options=anos_disponiveis,
            default=[max(anos_disponiveis)],
            key="relatorio_financiamento_anos"
        )

    # Botão de submissão
    submitted = st.form_submit_button("Gerar Dados")

    if submitted:
        # Filtrar o DataFrame corretamente
        df_filtrado = df_panorama_financiamento[
            (df_panorama_financiamento["nome"].isin(ente_selecionado)) &
            (df_panorama_financiamento["ano"].isin(anos_selecionados))
        ].copy()

        if df_filtrado.empty:
            st.warning("Não há dados disponíveis para o ente e ano selecionados.")
        else:
            df_renomeado = df_filtrado.rename(columns=COLUNAS_RENOMEADAS_DF_PANORAMA_FINANCIAMENTO)
            st.dataframe(df_renomeado)