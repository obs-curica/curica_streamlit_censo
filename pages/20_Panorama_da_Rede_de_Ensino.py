import streamlit as st

from scripts.utils import carregar_dados

from scripts.textos import(
    texto_pan_rede_intro,
    texto_pan_rede_caracterizacao,
    texto_pan_rede_totais,
    texto_pan_rede_analise,
    texto_pan_rede_dependencia_intro,
    texto_pan_rede_dependencia_analise,
    texto_pan_rede_dependencia_analise_2,
    texto_pan_rede_rural_intro_1,
    texto_pan_rede_rural_analise_1,
    texto_pan_rede_rural_intro_2,
    texto_pan_rede_rural_analise_2,
    texto_pan_rede_dependencia_rural_intro_1,
    texto_pan_rede_dependencia_rural_analise_1,
    texto_pan_rede_dependencia_rural_intro_2,
    texto_pan_rede_dependencia_rural_analise_2,
    text_pan_rede_dependencia_rural_conclusao,
    texto_pan_rede_relatorio_intro
)

from scripts.graficos import(
    grafico_matriculas_por_municipio,
    grafico_escolas_por_municipio,
    grafico_escolas_por_dependencia,
    grafico_matriculas_por_dependencia,
    grafico_matriculas_por_dependencia_municipio,
    grafico_escolas_por_dependencia_municipio,
    grafico_matriculas_por_localizacao,
    grafico_escolas_por_localizacao,
    grafico_matriculas_por_localizacao_municipio,
    grafico_escolas_por_localizacao_municipio,
    grafico_escolas_por_dependencia_localizacao,
    grafico_matriculas_por_dependencia_localizacao,
    grafico_matriculas_por_dependencia_localizacao_municipio,
    grafico_escolas_por_dependencia_localizacao_municipio
)

from scripts.relatorios import relatorio_rede_dados_escolas

# Configuração da página
st.set_page_config(page_title="Panorama Rede de Ensino", layout="wide", page_icon="🦜")

# Carrega dataframes
url_panorama = "https://raw.githubusercontent.com/obs-curica/curica_streamlit_censo/refs/heads/main/data/panorama_geral/df_panorama_geral.csv"
df_panorama_geral = carregar_dados(url_panorama)


st.title("🏫 Panorama da Rede Pública de Ensino do Estado do Acre")
st.write(texto_pan_rede_intro())


st.header("Caracterização da Rede de Ensino")
st.write(texto_pan_rede_caracterizacao())


st.subheader("Total de matrículas e Escolas por Município")
st.write(texto_pan_rede_totais())

anos_disponiveis = sorted(df_panorama_geral['NU_ANO_CENSO'].unique())
ano_mais_recente = max(anos_disponiveis)

ano_censo = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente)
)

col1, col2 = st.columns(2)
with col1:
    grafico_matriculas_por_municipio(df_panorama_geral, ano_censo)
with col2:
    grafico_escolas_por_municipio(df_panorama_geral, ano_censo)

st.write(texto_pan_rede_analise())


st.subheader("Total de matrículas e Escolas por Dependência Administrativa")
st.write(texto_pan_rede_dependencia_intro())

st.write("Ano Selecionado: ", ano_censo)

col1, col2 = st.columns(2)
with col1:
    grafico_matriculas_por_dependencia(df_panorama_geral, ano_censo)
with col2:
    grafico_escolas_por_dependencia(df_panorama_geral, ano_censo)

st.write(texto_pan_rede_dependencia_analise())

with st.form("form_dependencia"):
    ano_censo_dependencia = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key ="ano_censo_dependencia"
    )
    municipio_dependencia = st.selectbox(
        "Selecione o município:",
        sorted(df_panorama_geral['NO_MUNICIPIO'].unique()),
        key="municipio_dependencia")

    submitted = st.form_submit_button("Gerar Gráfico")
    if submitted:
        col1, col2 = st.columns(2)
        with col1:
            grafico_matriculas_por_dependencia_municipio(df_panorama_geral, ano_censo_dependencia, municipio_dependencia)
        with col2:
            grafico_escolas_por_dependencia_municipio(df_panorama_geral, ano_censo_dependencia, municipio_dependencia)

        st.write(texto_pan_rede_dependencia_analise_2())


st.header("Urbano vs. Rural vs. Florestal")

st.write(texto_pan_rede_rural_intro_1())

ano_censo_rural = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente),
    key ="ano_censo_rural"
)

col1, col2 = st.columns(2)
with col1:
    grafico_matriculas_por_localizacao(df_panorama_geral, ano_censo_rural)
with col2:
    grafico_escolas_por_localizacao(df_panorama_geral, ano_censo_rural)
st.write(texto_pan_rede_rural_analise_1())


st.subheader("Total de matrículas e Escolas por Localização, por Município")

st.write(texto_pan_rede_rural_intro_2())

with st.form("form_localizacao"):
    
    ano_censo_localizacao = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key ="ano_censo_localizacao")
    
    municipio_localizacao = st.selectbox(
        "Selecione o município:",
        sorted(df_panorama_geral['NO_MUNICIPIO'].unique()),
        key="municipio_localizacao"
    )
    
    submitted = st.form_submit_button("Gerar Gráfico")
    if submitted:
        col1, col2 = st.columns(2)
        with col1:
            grafico_matriculas_por_localizacao_municipio(df_panorama_geral, ano_censo_localizacao, municipio_localizacao)
        with col2:
            grafico_escolas_por_localizacao_municipio(df_panorama_geral, ano_censo_localizacao, municipio_localizacao)
    
        st.write(texto_pan_rede_rural_analise_2())
        

st.header("Dependência Administrativa de matrículas e escolas, por Localização")

st.write(texto_pan_rede_dependencia_rural_intro_1())

ano_censo_dependencia_rural = st.selectbox(
    "Selecione o ano do Censo Escolar:",
    options=anos_disponiveis,
    index=anos_disponiveis.index(ano_mais_recente),
    key ="ano_censo_dependencia_rural"
)

col1, col2 = st.columns(2)
with col1:
    grafico_matriculas_por_dependencia_localizacao(df_panorama_geral, ano_censo_dependencia_rural)
with col2:
    grafico_escolas_por_dependencia_localizacao(df_panorama_geral, ano_censo_dependencia_rural)

st.write(texto_pan_rede_dependencia_rural_analise_1())

st.subheader("Total de matrículas e Escolas por Dependência Administrativa, por Localização, por Município")

st.write(texto_pan_rede_dependencia_rural_intro_2())

with st.form("form_dependencia_localizacao_municipio"):
    
    ano_censo_dependencia_rural = st.selectbox(
        "Selecione o ano do Censo Escolar:",
        options=anos_disponiveis,
        index=anos_disponiveis.index(ano_mais_recente),
        key ="ano_censo_dependencia_localizacao_municipio"
    )

    municipio_dependencia_rural = st.selectbox(
        "Selecione o Município:",
        sorted(df_panorama_geral['NO_MUNICIPIO'].unique()),
        key="municipio_dependencia_localizacao_municipio"
    )

    submitted = st.form_submit_button("Gerar Gráfico")
    if submitted:
        col1, col2 = st.columns(2)
        with col1:
            grafico_matriculas_por_dependencia_localizacao_municipio(df_panorama_geral, ano_censo_dependencia_rural, municipio_dependencia_rural)
        with col2:
            grafico_escolas_por_dependencia_localizacao_municipio(df_panorama_geral, ano_censo_dependencia_rural, municipio_dependencia_rural)

        st.write(texto_pan_rede_dependencia_rural_analise_2())

st.write(text_pan_rede_dependencia_rural_conclusao())


st.header("Relatórios")

st.write(texto_pan_rede_relatorio_intro())

relatorio_rede_dados_escolas(df_panorama_geral)
