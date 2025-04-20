#=============================
# Arquivo com funções para chamada de texto
#============================

#======================
# Funções para a página inicial
#======================
def texto_app():
    return """
    Bem-vindo ao Observatório Curica, uma iniciativa do grupo de pesquisa PoÉticas nas Amazônias,  
    Grupo de Pesquisa Interdisciplinar em Linguagem e Educação, do Instituto Federal do Acre,  
    em conjunto com a Promotoria Especializada de Defesa da Criança e do Adolescente de Cruzeiro do Sul-Acre.  
      
    O Observatório Curica é uma plataforma de visualização de dados para diagnóstico, monitoramento e intervenção  
    nas políticas públicas educacionais do Estado do Acre e seus Municípios.       
      
    Utilize o menu lateral para navegar entre os panoramas e metas do Plano Nacional de Educação.
"""

#==========================
# Funções para a página Home
#==========================

def texto_home_contextualizacao():
    return """
    O Estado do Acre possui uma área de 164.221 km², território maior que o da Inglaterra ou quase 7 vezes 
    a área de Israel. Localiza-se na Amazônia Sul-Ocidental, região das nascentes dos rios das bacias 
    hidrográficas do rio Purus e do rio Juruá, afluentes do rio Amazonas. É palco de uma das maiores 
    sociobiodiversidades do planeta. Esse espaço acolhe grandes centros urbanos, unidades de conservação, 
    reservas extrativistas, projetos de assentamento do INCRA, populações tradicionais indígenas 
    e não indígenas ([ZEE Acre, 2010](https://sema.ac.gov.br/zee-acre/#:~:text=O%20Zoneamento%20Ecol%C3%B3gico%2DEcon%C3%B4mico%20do,06%20de%20abril%20de%201999.)).  

    O deslocamento dessas populações se dá por via terrestre, fluvial ou aérea. Esses meios de transporte 
    são diretamente influenciados pelo clima: no período chuvoso, os rios estão cheios e o transporte fluvial 
    de pessoas e cargas é favorecido. Por outro lado, o transporte terrestre fica prejudicado em razão da 
    precariedade das estradas. Na estação seca, ao contrário, fica favorecido o transporte terrestre e a 
    avegação é afetada. O transporte aéreo é uma alternativa a esses outros, entre centros urbanos.  

    As políticas públicas educacionais enfrentam esses mesmos desafios logísticos e climáticos, pois devem 
    ser implementadas em toda essa vasta extensão territorial. Surgem, portanto, dificuldades para a construção 
    de infraestrutura, sanemento básico e disponibilização de água potável, lotação de recursos humanos, fornecimento 
    de alimentação escolar, materiais didáticos e materiais de expediente, transporte escolar de alunos e professores, 
    formações continuadas, acompanhamento pedagógico e gastos com combustível.
"""


#==========================
# Funções para a página Panorama Rede
#==========================
def texto_pan_rede_intro():
    return """
    Esta página busca oferecer uma visão geral sobre os sistemas de ensino da rede pública de **educação básica** 
    do estado do Acre, com base nos dados do Censo Escolar. Serão introduzidos gráficos e tabelas que
    possibilitam uma análise mais detalhada sobre a quantidade de alunos e escolas por Município, bem como 
    a dependência administrativa, localização e outros aspectos relevantes. Lembre-se que todos os gráficos 
    e tabelas estão disponíveis para download. Basta passar o mouse por cima da imagem ou tabela para que o 
    menu fique disponível no canto superior direito. Sugere-se que o menu lateral seja retraído, para 
    melhor visualização dos gráficos.  
    Para este panorama, utilizou-se exclusivamente os dados do Censo Escolar, excluídas as escolas inativas e privadas.
    """
    
def texto_pan_rede_caracterizacao():
    return """
    A caracterização da rede de ensino é fundamental para compreender a estrutura educacional do estado do 
    Acre em seu contexto amazônico ímpar. Nesta seção, apresentam-se dados sobre o total de alunos e escolas 
    por Município, além de informações sobre a dependência administrativa das instituições de ensino. 
    A caracterização da rede é essencial para identificar as necessidades e desafios enfrentados pelos 
    Municípios, permitindo uma análise mais aprofundada das políticas públicas educacionais e suas 
    implicações na formação dos alunos.  
    
    Ainda, as características da rede de ensino são fundamentais para o planejamento e a implementação de políticas públicas
    educacionais eficazes, dado que elas **:orange-background[determinam] as possibilidades de :orange-background[captação de recursos] 
    federais**.
    """

def texto_pan_rede_totais():
    return """
    Inicia-se o estudo com a apresentação geral do quantitativo de alunos e escolas, por Município. É possível 
    selecionar o ano do Censo Escolar desejado, para que os gráficos sejam atualizados. Os gráficos podem ser 
    visualizados em tela cheia, clicando no ícone de tela cheia no canto superior direito da imagem.
    
    Sobre os dados, intuitivamente, espera-se que os Municípios com maior população tenham maior número 
    de alunos e escolas, certo?
    """
    
def texto_pan_rede_analise():
    return """
    Embora a soma total dos quatitativos apresentados pareça um dado singelo, a análise dos gráficos já permite uma 
    compreensão mais aprofundada da estrutura educacional do estado do Acre e das escolhas administrativas dos sistemas de ensino.
    
    Compare os Municípios de Taraucá e Jordão, localizados na mesma bacia hidrográfica. Taraucá abriga a terceira maior população 
    do Estado. Jordão, por sua vez, é um dos menos populosos do Acre. O número de alunos matriculados em seus sistemas de ensino 
    aderem a essa lógica. No entanto, **o número de escolas de Taraucá é próximo do número de escolas de Jordão**.  
    
    Esse dado evidencia uma prática muito comum adotada pelas Secretarias de Educação dos Municípios do Acre: a criação 
    de :orange-background[escolas anexas], que são escolas que não possuem autonomia administrativa, pedagógica e financeira. 
    Elas estão vinculadas a uma "escola sede" ou "escola polo", que é a responsável pela gestão administrativa, pedagógica e financeira. 
    
    Ao visitar as escolas anexas, é comum ouvir reclamações a respeito da desigualdade na distribuição de material de expediente ou,
    até mesmo, de alimentação escolar, que acabam privilegiando somente a escola polo. Entretanto, o cenário é pior do que parece, pois
    as escolas anexas não são cadastradas no Ministério da Educação,  e seus alunos constam como matriculados nas escolas polo. 
    Embora o respectivo sistema educacional, estaudal ou municipal, ainda receba os repasses do FNDE que levam em conta o número 
    de matrículas, esta situação impede a captação de recursos federais para a melhoria e manutenção da infraestrutura das escolas anexas.  
    
    Esta situação será detalhada em diversos momentos nesta plataforma, evidenciando os reflexos negativos dessa escolha 
    administrativa e apontando caminhos para intervenção. 
    """
    
def texto_pan_rede_dependencia_intro():
    return """
    Nesta subseção é detalhada a dependência administrativa das escolas, que pode ser Municipal, Estadual ou Federal. Ou seja,
    ela indica a qual sistema de ensino alunos e escolas estão vinculados. Ela segue a Lei de Diretrizes e Bases da Educação (LDB),
    que detalha a responsabilidade de cada ente federativo na oferta de educação básica. Embora a colaboração entre os entes 
    seja destaque, a LDB detalha que os Municípios devem oferecer a educação infantil e, com prioridade, o ensino fundamental. Já os Estados 
    devem assegurar o ensino fundamental e ofertar, com prioriodade, o ensino médio.
    
    A oferta da educação básica por entes que integram o sistema de ensino federal se dá, no Estado do Acre, por meio do Colégio de Aplicação,
    da UFAC, com sede em Rio Branco, e por meio dos Institutos Federais do Acre (IFAC), com maior capilaridade.
    
    Do ponto de vista de uma Promotoria de Justiça, a dependência administrativa indica o polo passivo de eventual ação civil pública.
    
    Os gráficos a seguir apresentam o total de alunos e escolas por dependência administrativa, para todo o Estado.
    """