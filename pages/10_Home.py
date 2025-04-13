import streamlit as st

# Configurações iniciais de layout
st.set_page_config(
    page_title="Observatório Curica",
    layout="wide",
    page_icon="🦜"
)

# Paleta e estilos
st.markdown("""
    <style>
        body {
            background-color: #121212;
        }
        .title {
            color: #FFA07A;
            font-size: 2.8em;
            font-weight: bold;
        }
        .subtitle {
            color: #FFA07A;
            font-size: 1.5em;
            margin-top: 10px;
        }
        .text {
            color: #B0E0E6;
            font-size: 1.1em;
            text-align: justify;
        }
    </style>
""", unsafe_allow_html=True)

# Conteúdo da página inicial
st.markdown('<div class="title">Observatório Curica</div>', unsafe_allow_html=True)

st.markdown("""
<div class="text">
<p>
O Observatório Curica é uma iniciativa desenvolvida pela Promotoria de Defesa da Criança e do Adolescente de Cruzeiro do Sul (MPAC), que visa monitorar, diagnosticar e subsidiar intervenções em políticas públicas voltadas à educação escolar pública no Estado do Acre. 
</p>

<p>
A partir de bases de dados oficiais e abertas, como os microdados do Censo Escolar, PDDE/INEP e IBGE, o Observatório integra dados, analisa deficiências estruturais e propõe caminhos de atuação para as Promotorias de Justiça. 
Especial atenção é dada à realidade da Amazônia Ocidental Acreana, com foco nas escolas rurais que atendem populações tradicionais, indígenas e não indígenas.
</p>

<p>
Mais do que uma ferramenta de gestão e diagnóstico, o Observatório também se propõe a ser um instrumento de controle social e de promoção dos direitos fundamentais, reafirmando o papel institucional do Ministério Público na fiscalização das políticas públicas educacionais e na efetivação dos direitos da infância e juventude.
</p>

<p>
O nome “Curica” homenageia os saberes tradicionais e a biodiversidade da região, fazendo referência ao olhar atento dessa ave amazônica e aos <i>kene</i>, ensinados por <i>Yube</i> – o Mestre dos grafismos na cosmologia Huni Kuĩ.
</p>

<p>
Acesse os painéis laterais para explorar os dados e análises construídos nesta plataforma.
</p>
</div>
""", unsafe_allow_html=True)
