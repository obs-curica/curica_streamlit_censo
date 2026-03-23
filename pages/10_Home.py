import streamlit as st

from scripts.textos import texto_home_contextualizacao

# Configurações iniciais de layout
st.set_page_config(
    page_title="Observatório Curica",
    layout="wide",
    page_icon="🦜"
)

st.header("Observatório :orange[Cu]:green[ri]:orange[c]:red[a]")

st.markdown("""
O Observatório Curica é uma iniciativa desenvolvida pela Promotoria de Defesa da Criança e do Adolescente de Cruzeiro do Sul, que visa monitorar, diagnosticar e subsidiar intervenções em políticas públicas voltadas à educação escolar pública no Estado do Acre. 

A partir de bases de dados oficiais e abertas, como os microdados do Censo Escolar, PDDE/INEP e IBGE, o Observatório integra dados, analisa deficiências estruturais e **propõe caminhos de atuação para as Promotorias de Justiça**. 
Especial atenção é dada à realidade da Amazônia Ocidental Acreana, com foco nas escolas rurais que atendem populações tradicionais, indígenas e não indígenas.

Mais do que uma ferramenta de gestão e diagnóstico, o Observatório também se propõe a ser um instrumento de controle social e de promoção dos direitos fundamentais, reafirmando o papel institucional do Ministério Público na fiscalização das políticas públicas educacionais e na efetivação dos direitos da infância e juventude.

O nome “Curica” homenageia os saberes tradicionais e a biodiversidade da região, fazendo referência ao olhar atento dessa ave amazônica e aos *kene*, ensinados por *Yube* – o Mestre dos grafismos na cosmologia Huni Kuĩ.

Acesse os painéis laterais para explorar os dados e análises construídos nesta plataforma.
""")

st.subheader("Contextualização")
st.markdown(texto_home_contextualizacao())

#st.subheader("Objetivos e Metodologia")
#st.write("Em construção.")