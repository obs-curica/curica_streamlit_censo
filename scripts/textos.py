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

# Funções para a página Panorama Rede - Dependência Administrativa

def texto_pan_rede_dependencia_intro():
    return """
    Nesta subseção é detalhada a dependência administrativa das escolas, que pode ser Municipal, Estadual ou Federal. Ou seja,
    ela indica a qual sistema de ensino alunos e escolas estão vinculados. Ela segue a Lei de Diretrizes e Bases da Educação (LDB),
    que detalha a responsabilidade de cada ente federativo na oferta de educação básica. Embora a colaboração entre os entes 
    seja destaque, a LDB detalha que os Municípios devem oferecer a educação infantil e, com prioridade, o ensino fundamental. 
    Já os Estados devem assegurar o ensino fundamental e ofertar, com prioriodade, o ensino médio.
    
    A oferta da educação básica por entes que integram o sistema de ensino federal se dá, no Estado do Acre, por meio do 
    Colégio de Aplicação, da UFAC, com sede em Rio Branco, e por meio dos Institutos Federais do Acre (IFAC), com maior capilaridade.
    
    Do ponto de vista de uma Promotoria de Justiça, a dependência administrativa indica o polo passivo de eventual ação civil pública.
    
    Os gráficos a seguir apresentam o total de alunos e escolas por dependência administrativa, para todo o Estado.
    """
    
def texto_pan_rede_dependencia_analise():
    return """
    Como será aprofundado na avaliação do cumprimento das metas do Plano Nacional de Educação, as matrículas do ensino 
    infantil e fundamental somadas superam o número de matrículas do ensino médio. Pensando que esses níveis de ensino 
    devem ser ofertados prioritariamente pelos Municípios, era de se esperar que a maior quantidade de alunos e escolas 
    estivesse vinculada à rede pública municipal.  
    
    No entanto, os dados revelam que, somados, a maior parte dos alunos está vinculada à rede pública estadual e, por
    outro lado, a maior parte das escolas está vinculada à rede pública Municipal.  
    Essa informação é importante para entender as estratégias adotadas por cada ente federativo, bem como a distribuição 
    de responsabilidades entre os diferentes níveis de governo na oferta de educação básica.  
    
    Nesse ponto, é importante lembrar que grande parte dos recursos federais para a educação básica são transferidos
    ao Estado e Municípios levando em conta o quantitativo de alunos matriculados e contabilizados no Censo Escolar.
    
    Agora dê corda à sua inquietação e verifique se este panorama geral se repete localmente, em seu Município. Melhor ainda,
    escolha alguns Municípios, compare os dados e reflita sobre as diferenças e suas motivações.
    """
    
def texto_pan_rede_dependencia_analise_2():
    return """
    Sem pretensão de exaurir o tema, é possível afirmar que, ao se comparar os dados entre os Municípios, nota-se que
    quanto maior a população do Município, maior o número de alunos e escolas vinculados à rede pública estadual. 
    É o caso nos Municípios de Rio Branco, Cruzeiro do Sul, Tarauacá, Feijó e Sena Madureira.  
    
    Ainda, é possível notar uma acentuada diminuição da presença do sistema de ensino estadual nos Municípios que não possuem 
    acesso terrestre: Santa Rosa do Purus, Jordão, Marechal Thaumaturgo e Porto Walter.
    
   Esta análise segue sendo aprofundada abaixo, categorizando-se a rede de ensino pela localização das escolas.
    """

# Funções para a página Panorama Rede - Urbano vs. Rural

def texto_pan_rede_rural_intro_1():
    return """
    Abaixo são apresentados os dados sobre a localização das escolas, que são classificadas no Censo Escolar como aquelas
    localizadas em área urbana ou rural, tento como critério os limites geográficos definidos no Plano Diretor do Município 
    ou instrumento equivalente. Essa classificação é importante para entender a distribuição das escolas no território e a 
    acessibilidade dos alunos à educação básica.  
    
    Muito já foi dito a respeito da dualidade entre os adjetivos "rural" e "urbano", bem como sobre os concepções pejorativas
    ou supremacistas que permeiam essa classificação. Nunca é demais relembrar que o termo rural deve ser empregado com a cautela
    de se levar em conta o contexto que o abriga. Nesse caso, o contexto amazônico marcado por sua rica sociobiodiversidade. 
    Desse modo, é importante ter em mente que o termo "rural" abriga tanto escolas indígenas, como escolas em reservas extrativistas, 
    projetos de assentamento do INCRA e ribeirinhas. É quase um conceito negativo do urbano. Críticas à parte, o Censo Escolar busca 
    afinar essa categorização com outros campos que tratam da "Localização Diferenciada", abordada em panorama próprio.
    
    O ensino rural é explicitamente previsto na LDB, que estabelece a necessidade de sua adaptação às peculiaridades locais e 
    suas as manifestações culturais, a adequação do currículo às necessidades dos alunos, calendário escolar adaptado ao 
    ciclo agrícola e às condições climáticas e adequação da escola à natureza do trabalho rural 
    ([LDB, 1996](https://www.planalto.gov.br/ccivil_03/leis/L9394compilado.htm#:~:text=desportivas%20n%C3%A3o%2Dformais.-,Art.%2028,-.%20Na%20oferta%20de)).    
    
    Segue o panorama geral da localização das escolas, para todo o Estado do Acre, conforme os dados do Censo Escolar.
    """
    
def texto_pan_rede_rural_analise_1():
    return """
    O primeiro gráfico apresenta o total de alunos por localização, indicando a maior concentração de alunos em escolas
    localizadas em áreas urbanas. Esse dado reflete os dados populacionais de que a maioria da população do Acre reside 
    em áreas urbanas. Entretanto, quase um terço do total de alunos está matriculado em escolas rurais.
    
    Por sua vez, o segundo gráfico revela que a quantidade de escolas em áreas rurais é quase dois terços maior do que a
    quantidade de escolas em áreas urbanas. Esse é o dado que começa a diferenciar a educação amazônica daquela executada
    em outras regiões do Brasil. Para se ter uma perspectiva, o Estado do Acre abrange uma área territorial próxima da Inglaterra.
    Os Municípios do Vale do Alto Rio Juruá, por sua vez, possuem uma área territorial maior que a do Estado de Israel.
    A noção dessas dimensões espaciais são fundamentais para se compreender os desafios da realidade educacional do Acre 
    e não se surpreender com a quantidade de escolas rurais/florestais.
    
    Portanto, a quantidade de escolas rurais é um reflexo da dispersão espacial da população no território, que é uma característica
    marcante da região amazônica. E serve de alerta àqueles que pensam que a floresta é um "[deserto verde](https://search.worldcat.org/title/3189649)"
    a ser conquistado.
    
    Assim como na análise anterior, é possível comparar os dados entre os Municípios e refletir sobre as diferenças
    e suas motivações.
    """
    
def texto_pan_rede_rural_intro_2():
    return """
    Selecione abaixo o ano do Censo Escolar e o Município desejado. Os gráficos apresentam o total de alunos e escolas por localização.
    """

def texto_pan_rede_rural_analise_2():
    return """
    E então, como está a localização das escolas em seu Município? A maior parte delas está localizada em áreas urbanas ou rurais?
    E os alunos, estão de fato concentrados na área urbana? Existem Municípios com maior número de alunos em escolas rurais?
    Há uma relação entre a quantidade de alunos em áreas rurais e a região onde o Município está inserido?
    
    O grande número de alunos e escolas rurais nos Municípios do interior do Acre apenas reflete a realidade geográfica e 
    demográfica do Estado. O que é preciso enfatizar é que existem Municípios com grande quantidade de alunos e escolas rurais,
    que enfrentam os desafios logísticos e climáticos da região amazônica. Como fica o transporte escolar em ramais, durante
    o período chuvoso, ou em igarapés, no período da seca? E o fornecimento de alimentação escolar e material de expediente?
    
    Existem soluções para esses desafios já previstas pela legislação e ainda pouco exploradas pela administração escolar 
    estadual e municipais, como a :orange-background[adequação do calendário escolar] ao ciclo agrícola e às condições climáticas ou a 
    aquisição da alimentação escolar diretamente da :orange-background[agricultura familiar local], ou mesmo a :orange-background[pedagogia da alternância]. 
    Há muito trabalho a ser feito.
    
    De quem é a responsabilidade?
    
    O início da resposta a essa pergunta pode ser obtido combinando-se os dados da análise anterior que trata da dependência
    administrativa, com os dados sobre a localização das escolas. Essa combinação de dados é importante porque
    identifica a presença dos diferentes sistemas de ensino em áreas urbanas e rurais. 
    """
    
# Funções para a página Panorama Rede - Dependencia Administrativa e Localização

def texto_pan_rede_dependencia_rural_intro_1():
    return """
    A combinação dos dados sobre a dependência administrativa e a localização das escolas é fundamental para entender 
    como os diferentes sistemas de ensino atuam em áreas urbanas e rurais. Essa análise permite identificar as 
    escolhas administrativas do Governo do Estado e dos Municípios, bem como suas responsabilidades por possíveis
    omissões.
        
    A seguir, são apresentados gráficos que mostram o total de alunos e escolas por dependência administrativa, 
    considerando a localização das escolas, se urbanas ou rurais. Selecione o ano do Censo Escolar desejado.
    """    

def texto_pan_rede_dependencia_rural_analise_1():
    return """
    Agora fica evidente o modo como os sistemas de ensino estão concentrados em cada uma das dependências administrativas. 
    Nota-se que o sistema de ensino estadual possui um número significativamente maior de alunos matriculados em sua rede,
    quando comparado com o sistema de ensino municipal. Entretanto, possui um número de escolas urbanas e rurais menor que
    o dos Muncípios, especialmente na zona rural.

    Novamente, há que se refletir sobre as causas e os impactos dessas decisões admninistrativas. Pensando no sistema estadual 
    de ensino, há redução ou aumento de custos? Menos escolas significam menos salas de aula e maior lotação? Há ausência de 
    cobertura na zona rural? Esses mesmos questionamentos se aplicam ao sistema municipal. 
    
    De plano, é possível concluir que o sistema de ensino estadual possui um índice de concentração maior que os sistemas 
    de ensino municipais. Ou seja, possui menos escolas para um maior número de alunos. Ainda, é claramente menos presente 
    na zona rural. Os demais questionamentos serão endereçados logo mais abaixo, na seção que tratará do financiamento da 
    educação pública e sua relação com os dados analisados até aqui.  
    
    Por hora, vale comparar a distribuição específica por Município:
    """
    
def texto_pan_rede_dependencia_rural_intro_2():
    return """
    intro 2
    Relembra-se que os gráficos abaixo podem ser visualizados em tela cheia, clicando no ícone de tela cheia no 
    anto superior direito da imagem.
    """
    
def texto_pan_rede_dependencia_rural_analise_2():
    return """
    analise 2
    """