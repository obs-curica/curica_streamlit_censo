#=============================
# Arquivo com funções para chamada de texto
#============================

#======================
# PÁGINA APP.PY
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
# PÁGINA HOME
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
    
    Avesso da blusa para  
    encontrar o caminho de volta...
    criar uma picada segura nesse cipoal, tabocal espinhoso...
"""


#==========================
# PÁGINA PANORAMA REDE
#==========================

def texto_pan_rede_intro():
    return """
    Esta página busca oferecer uma visão geral sobre os sistemas de ensino da rede pública de **educação básica** 
    do estado do Acre, com base nos dados do Censo Escolar. Serão introduzidos gráficos e tabelas que
    possibilitam uma análise mais detalhada sobre a quantidade de matrículas e escolas por Município, bem como 
    a dependência administrativa, localização e outros aspectos relevantes. Lembre-se que todos os gráficos 
    e tabelas estão disponíveis para download. Basta passar o mouse por cima da imagem ou tabela para que o 
    menu fique disponível no canto superior direito. Sugere-se que o menu lateral seja retraído, para 
    melhor visualização dos gráficos.  
    Para este panorama, utilizou-se exclusivamente os dados do Censo Escolar, excluídas as escolas inativas e privadas.
    """
    
def texto_pan_rede_caracterizacao():
    return """
    A caracterização da rede de ensino é fundamental para compreender a estrutura educacional do estado do 
    Acre em seu contexto amazônico ímpar. Nesta seção, apresentam-se dados sobre o total de matrículas e escolas 
    por Município, além de informações sobre a dependência administrativa das instituições de ensino. 
    A caracterização da rede é essencial para identificar as necessidades e desafios enfrentados pelos 
    Municípios, permitindo uma análise mais aprofundada das políticas públicas educacionais e suas 
    implicações na formação dos alunos.  
    
    Ainda, as características da rede de ensino são fundamentais para o planejamento e a implementação de políticas públicas
    educacionais eficazes, dado que elas **:orange-background[determinam] as possibilidades de :orange-background[captação de recursos] 
    federais**.  
    
    Ressalta-se que o estudo adota como nomenclatura o número de matrículas e não o número de alunos, porque há a 
    possibilidade dupla matrícula de alunos que recebem atendimento educacional especializado e daqueles matriculados
    em itinerários de formação técnica e profissional do ensino médio.
    """

def texto_pan_rede_totais():
    return """
    Inicia-se o estudo com a apresentação geral do quantitativo de matrículas e escolas, por Município. É possível 
    selecionar o ano do Censo Escolar desejado, para que os gráficos sejam atualizados. Os gráficos podem ser 
    visualizados em tela cheia, clicando no ícone de tela cheia no canto superior direito da imagem.
    
    Sobre os dados, intuitivamente, espera-se que os Municípios com maior população tenham maior número 
    de matrículas e escolas, certo?
    """
    
def texto_pan_rede_analise():
    return """
    Embora a soma total dos quatitativos apresentados pareça um dado singelo, a análise dos gráficos já permite uma 
    compreensão mais aprofundada da estrutura educacional do estado do Acre e das escolhas administrativas dos sistemas de ensino.
    
    Compare os Municípios de Taraucá e Jordão, localizados na mesma bacia hidrográfica. Taraucá abriga a terceira maior população 
    do Estado. Jordão, por sua vez, é um dos menos populosos do Acre. O número de matrículas em seus sistemas de ensino 
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

# Panorama Rede - Dependência Administrativa

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
    
    Os gráficos a seguir apresentam o total de matrículas e escolas por dependência administrativa, para todo o Estado.
    """
    
def texto_pan_rede_dependencia_analise():
    return """
    Como será aprofundado na avaliação do cumprimento das metas do Plano Nacional de Educação, as matrículas do ensino 
    infantil e fundamental somadas superam o número de matrículas do ensino médio. Pensando que esses níveis de ensino 
    devem ser ofertados prioritariamente pelos Municípios, era de se esperar que a maior quantidade de matrículas e escolas 
    estivesse vinculada à rede pública municipal.  
    
    No entanto, os dados revelam que, somados, a maior parte das matrículas está vinculada à rede pública estadual e, por
    outro lado, a maior parte das escolas está vinculada à rede pública Municipal. Essa informação é importante para entender as estratégias adotadas por cada ente federativo, bem como a distribuição 
    de responsabilidades entre os diferentes níveis de governo na oferta de educação básica.  
    
    Nesse ponto, é importante lembrar que grande parte dos recursos federais para a educação básica são transferidos
    ao Estado e Municípios levando em conta o quantitativo de alunos matriculados e contabilizados no Censo Escolar.
    
    Agora dê corda à sua inquietação e verifique se este panorama geral se repete localmente, em seu Município. Melhor ainda,
    escolha alguns Municípios, compare os dados e reflita sobre as diferenças e suas motivações.
    """
    
def texto_pan_rede_dependencia_analise_2():
    return """
    Sem pretensão de exaurir o tema, é possível afirmar que, ao se comparar os dados entre os Municípios, nota-se que
    quanto maior a população do Município, maior o número de matrículas e escolas vinculados à rede pública estadual. 
    É o caso nos Municípios de Rio Branco, Cruzeiro do Sul, Tarauacá, Feijó e Sena Madureira.  
    
    Ainda, é possível notar uma acentuada diminuição da presença do sistema de ensino estadual nos Municípios que não possuem 
    acesso terrestre: Santa Rosa do Purus, Jordão, Marechal Thaumaturgo e Porto Walter.
    
   Esta análise segue sendo aprofundada abaixo, categorizando-se a rede de ensino pela localização das escolas.
    """

# Panorama Rede - Urbano vs. Rural

def texto_pan_rede_rural_intro_1():
    return """
    Abaixo são apresentados os dados sobre a localização das escolas, que são classificadas no Censo Escolar como aquelas
    localizadas em área urbana ou rural, tento como critério os limites geográficos definidos no Plano Diretor do Município 
    ou instrumento equivalente. Essa classificação é importante para entender a distribuição das escolas no território e o
    acesso dos alunos à educação básica.  
        
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
    O primeiro gráfico apresenta o total de matrículas por localização, indicando a maior concentração de matrículas em escolas
    localizadas em áreas urbanas. Esse dado reflete os dados populacionais de que a maioria da população do Acre reside 
    em áreas urbanas. Entretanto, quase um terço do total de alunos estão matriculados em escolas rurais.
    
    Por sua vez, o segundo gráfico revela que a quantidade de escolas em áreas rurais é quase dois terços maior do que a
    quantidade de escolas em áreas urbanas. Esse é o dado que começa a diferenciar a **educação amazônica** daquela executada
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
    Selecione abaixo o ano do Censo Escolar e o Município desejado. Os gráficos apresentam o total de matrículas e escolas por localização.
    """

def texto_pan_rede_rural_analise_2():
    return """
    E então, como está a localização das escolas em seu Município? A maior parte delas está localizada em áreas urbanas ou rurais?
    E as matrículas, estão de fato concentrados na área urbana? Existem Municípios com maior número de matrículas em escolas rurais?
    Há uma relação entre a quantidade de matrículas em áreas rurais e a região onde o Município está inserido?
    
    O grande número de matrículas e escolas rurais nos Municípios do interior do Acre apenas reflete a realidade geográfica e 
    demográfica do Estado. O que é preciso enfatizar é que existem Municípios com grande quantidade de alunos e escolas rurais,
    que enfrentam os desafios logísticos e climáticos da região amazônica. Como fica o transporte escolar em ramais, durante
    o período chuvoso, ou em igarapés, no período da seca? E o fornecimento de alimentação escolar e material de expediente?
    
    Existem soluções para esses desafios já previstas pela legislação e ainda pouco exploradas pela administração escolar 
    estadual e municipais, como a :orange-background[adequação do calendário escolar] ao ciclo agrícola e às condições climáticas ou a 
    aquisição da alimentação escolar diretamente da :orange-background[agricultura familiar local], ou mesmo a :orange-background[pedagogia da alternância]. 
    Há muito trabalho a ser feito.
    
    De quem é a responsabilidade?
    
    O início da resposta a essa pergunta pode ser obtido combinando-se os dados da análise anterior, que trata da dependência
    administrativa, com os dados sobre a localização das escolas. Essa combinação de dados é importante porque
    identifica a presença dos diferentes sistemas de ensino em áreas urbanas e rurais. 
    """
    
# Panorama Rede - Dependencia Administrativa e Localização

def texto_pan_rede_dependencia_rural_intro_1():
    return """
    A combinação dos dados sobre a dependência administrativa e a localização das escolas é fundamental para entender 
    como os diferentes sistemas de ensino atuam em áreas urbanas e rurais. Essa análise permite identificar as 
    escolhas administrativas do Governo do Estado e dos Municípios, bem como suas responsabilidades por possíveis
    omissões.
        
    A seguir, são apresentados gráficos que mostram o total de matrículas e escolas por dependência administrativa, 
    considerando a localização das escolas, se urbanas ou rurais. Selecione o ano do Censo Escolar desejado.
    """    

def texto_pan_rede_dependencia_rural_analise_1():
    return """
    Agora fica evidente o modo como os sistemas de ensino estão concentrados em cada uma das dependências administrativas. 
    No geral, nota-se que o sistema de ensino estadual possui um número significativamente maior de alunos matriculados em sua rede,
    quando comparado com o sistema de ensino municipal. Entretanto, possui um número de escolas urbanas e rurais menor que
    o dos Muncípios, especialmente na zona rural.

    Novamente, há que se refletir sobre as causas e os impactos dessas decisões admninistrativas. Pensando no sistema estadual 
    de ensino, há redução ou aumento de custos? Menos escolas significam menos salas de aula e maior lotação? Há ausência de 
    cobertura na zona rural? Esses mesmos questionamentos se aplicam ao sistema municipal. 
    
    De plano, é possível concluir que o sistema de ensino estadual possui um índice de concentração maior que os sistemas 
    de ensino municipais. Ou seja, possui menos escolas para um maior número de matrículas. Ainda, é claramente menos presente 
    na zona rural. Os questionamentos sobre os custos serão endereçados na página trata do financiamento da educação pública e 
    sua relação com os dados analisados até aqui. O leitor vai perceber que este é um tema recorrente que também será abordado 
    especificamente em cada uma das páginas deste site.
    
    Por hora, vale comparar a distribuição específica por Município e verificar se o quadro geral se repete localmente.
    """
    
def texto_pan_rede_dependencia_rural_intro_2():
    return """
    O formulário abaixo permite a visualização dos dados por Município.  
    Relembra-se que os gráficos abaixo podem ser visualizados em tela cheia, clicando no ícone de tela cheia no canto superior 
    direito da imagem.
    """
    
def texto_pan_rede_dependencia_rural_analise_2():
    return """
    Como ficou a distribuição de matrículas e escolas por dependência administrativa e localização em seu Município, quando comparado 
    com o quadro geral? Há Municípios com maior número de alunos matriculados no sistema de ensino municipal? As escolas estatudais 
    continuam concentradas na zona urbana? E as escolas municipais? Há Municípios com maior número de alunos matriculados em escolas rurais?
    Há uma relação entre a presença do sistema de ensino estadual e a região onde o Município está inserido?
    """
    
def text_pan_rede_dependencia_rural_conclusao():
    return """
    A análise dos dados sobre a dependência administrativa e a localização das escolas revela a complexidade da
    realidade educacional do estado do Acre. A vasta extensão territorial, a diversidade cultural e as
    características geográficas da região exigem uma abordagem diferenciada para a oferta de educação básica.
    A presença significativa de escolas rurais e a concentração de matrículas em áreas urbanas indicam a necessidade
    de políticas públicas que considerem as especificidades locais e promovam a equidade no acesso à educação.
    A combinação desses dados com informações sobre o financiamento da educação pública permitirá uma análise
    mais aprofundada das responsabilidades dos diferentes sistemas de ensino e suas implicações na formação dos alunos.
    """
    
# Geração de relatórios

def texto_pan_rede_relatorio_intro():
    return """
    Nesta subseção, você pode gerar relatórios com a relação das escolas de cada Município, contendo o seu número
    identificador no cadastro do MEC, o número de matrículas, a dependência administrativa, localização e endereço.  
    São dados úteis para diminuir a abstração dos gráficos a iniciar a materialização do trabalho.
    
    Eles podem ser baixados pelo usuario. Basta selecionar os filtros desejados e clicar no botão de download.
    """

#==========================
# PÁGINA FINANCIAMENTO REDE
#==========================


def texto_pan_financiamento_intro():
    return """
    Quando se pensa em recursos para financiamento de políticas públicas, logo vem à mente a ideia de escassez e o argumento da 
    [reserva do possível](https://www.stf.jus.br/arquivo/informativo/documento/informativo345.htm#ADPF%20-%20Pol%C3%ADticas%20P%C3%BAblicas%20-%20Interven%C3%A7%C3%A3o%20Judicial%20-%20%22Reserva%20do%20Poss%C3%ADvel%22%20(Transcri%C3%A7%C3%B5es):~:text=T%20R%20A%20N%20S%20C%20R%20I%20%C3%87%20%C3%95%20E%20S%).  
    **Será mesmo que os recursos são escassos ao ponto de inviabilizar a oferta da educação básica com qualidade?**
    
    O modelo de federalismo brasileiro prevê que a União, os Estados e os Municípios mantenham seus respectivos sistemas de ensino, 
    em regime de colaboração ([art. 211 CF](https://www.planalto.gov.br/ccivil_03/Constituicao/Constituicao.htm#art212:~:text=Art.%20211.%20A%20Uni%C3%A3o%2C%20os%20Estados%2C%20o%20Distrito%20Federal%20e%20os%20Munic%C3%ADpios%20organizar%C3%A3o%20em%20regime%20de%20colabora%C3%A7%C3%A3o%20seus%20sistemas%20de%20ensino.)). 
    Pensando na educação básica, cada ente possui responsabilidades prioritárias: os Municípios, com a educação infantil e fundamental; 
    os Estados, com o ensino fundamental e médio; e a União, responsabilidade em caráter supletivo e redistributivo, para garantir 
    padrão mínimo de qualidade em todo o país. Essa organização reflete tanto a autonomia dos entes quanto a necessidade de 
    cooperação federativa para assegurar o direito à educação. 
    
    O [art. 212](https://www.planalto.gov.br/ccivil_03/constituicao/ConstituicaoCompilado.htm#:~:text=Art.%20212.-,A%20Uni%C3%A3o%20aplicar%C3%A1,-%2C%20anualmente%2C%20nunca%20menos)
     da CF define três diferentes fontes de financiamento da educação básica:
    
    * o Fundeb - Fundo  de Manutenção e Desenvolvimento da Educação Básica e de Valorização dos Profissionais da Educação.
    * a aplicação mínima da arrecadação em impostos, na proporção de 18% para a União e **25%** para Estados e Municípios, 
    na Manutenção e Desenvolvimento do Ensino (MDE);
    * o Salário Educação;
    
    Além dessas fontes, há também outros programas e ações executadas dentro da estrutura do **Fundo Nacional de Desenvolvimento 
    da Educação (FNDE)**, autarquia vinculada ao Ministério da Educação, criada no ano de 1968 [(Lei 5.537/68)](https://www.planalto.gov.br/ccivil_03/leis/l5537.htm). 
    Repasses de recursos por meio de programas como o PNLD, PNAE, PNATE, PDDE e o próprio Fundeb consolidam sua atuação.
    
    Na sequência, apresenta-se uma visão geral desses recursos para cada esfera administrativa.
    """

# Fundeb
def texto_pan_financiamento_fundeb_intro():
    return """
    O financiamento da educação básica pública no Brasil passou por importantes transformações ao longo do tempo.
    Em 1996, foi criado o Fundef (Fundo de Manutenção e Desenvolvimento do Ensino Fundamental e de Valorização do 
    Magistério), voltado exclusivamente para o ensino fundamental. Sua estrutura visava garantir o acesso e a 
    qualidade deste nível de ensino, mas deixava de fora a educação infantil e o ensino médio.  

    Com a ampliação do conceito de educação como direito social em todas as etapas, o Fundeb (Fundo de Manutenção 
    e Desenvolvimento da Educação Básica e de Valorização dos Profissionais da Educação) foi instituído em 2007. 
    Diferente do Fundef, o Fundeb abrange toda a educação básica — da creche ao ensino médio — e contempla todos 
    os profissionais da educação, fortalecendo o compromisso com a equidade e a qualidade do ensino público.  

    Aprovado de forma permanente em 2020, o novo Fundeb trouxe melhorias, como o aumento da participação da União 
    e a adoção de mecanismos de correção de desigualdades educacionais. Agora o Fundeb tem caráter permanente e 
    constitucional e está regulamentado pela Lei [13.113/2020](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm). 
        
    Ele é formado pelo repasse de 20% de uma [cesta de tributos](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=Receita%20dos%20Fundos-,Art.%203%C2%BA,-Os%20Fundos%2C%20no) 
    provenientes da arrecadação estadual e federal. 
    Logo, é importante esclarecer que o Fundeb não possui uma natureza estadual ou federal, mas híbrida. Assim, o 
    que define a competência na tomada de contas ou da fiscalização do repasse é a origem do recurso utilizado, 
    segundo as declarações contábeis ([ADI 5791](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=493795&ori=1), 
    [art. 30 da Lei do Fundeb](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=e%20do%20Controle-,Art.%2030,-.%C2%A0%20A%20fiscaliza%C3%A7%C3%A3o%20e)).

    A distribuição dos recursos que compõem os Fundos ocorre de forma automática e o montante varia de acordo com a
    arrecadação dos impostos que compõe a cesta. Por sua vez, o rateio dos valores se dá em função do número de alunos 
    matriculados nas respectivas redes de educação básica pública presencial, no âmbito da atuação prioritária de 
    cada ente Federativo. Ainda, a distribuição do recurso é feita de forma ponderada por [etapas e modalidades](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/Decreto/D10656.htm#:~:text=A%20da%20Constitui%C3%A7%C3%A3o.-,Art.%202%C2%BA,-Para%20fins%20do) 
    de ensino na qual o aluno está matriculado, duração da jornada e tipo de estabelecimento, com índices definidos anualmente [(art. 7)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=e%20das%20Pondera%C3%A7%C3%B5es-,Art.%207%C2%BA,-A%20distribui%C3%A7%C3%A3o%20de).
    O número de matrículas em cada etapa e modalidade é obtido a partir do :orange-background[Censo Escolar], que também é realizado 
    anualmente pelo INEP.
    
    A atribuição do Ministério Público está explicitamente definida no [artigo 32](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=Art.%2032.%C2%A0%20A-,defesa,-da%20ordem%20jur%C3%ADdica) 
    da Lei do Fundeb, que estabelece que:
    
    "*A defesa da ordem jurídica, do regime democrático, dos interesses sociais e individuais indisponíveis, 
    relacionada ao pleno cumprimento desta Lei, :orange-background[compete ao Ministério Público dos Estados] e 
    do Distrito Federal e Territórios e ao Ministério Público Federal, especialmente quanto às transferências 
    de recursos federais.*"
    
    Se existia, este dispositivo retira qualquer dúvida a respeito da atribuição do Ministério Público Estadual 
    na fiscalização dos repasses do Fundeb.
    
    Acompanhe abaixo a evolução dos repasses do Fundeb, com gráficos que mostram a distribuição dos recursos 
    por ente Federativo, no tempo. Os valores foram extraídos da plataforma SIOPE, do FNDE e foram contabilizados
    os recursos totais do Fundeb disponíveis para o exercício respectivo. Além do principal, 
    estão incluídas as complementações VAAF, VAAT e VAAR, explicadas e discriminadas mais abaixo.
      
    Estão disponíveis os dados a partir do ano de 2021. O nome Acre refere-se à Secretaria Estadual de Educação 
    e foi mantido assim por ser o padrão adotado nos documentos oficiais do FNDE e do Tesouro Nacional.
    Se não forem encontrados dados para o ano selecionado na consulta, significa que o Ente atrasou sua prestação 
    de contas e é um indicativo para a atuação do Ministério Público. 
    """
    
def texto_pan_financiamento_fundeb_analise_1():
    return """
    Como explicado acima, o repasse do Fundeb é feito de forma automática e é diretamente proporcional ao número 
    de matrículas do respectivo sistema de ensino público em sua área de atuação prioritária, definida pela LDB. 
    Portanto, quanto maior o número de matrículas, maior o repasse. Desse modo, não são contabilizadas as matrículas 
    de alunos em área de atuação não prioritária, declaradas no Censo Escolar. Por exemplo, as matrículas de alunos 
    da educação infantil matriculados na rede estadual de ensino não são contabilizados para o repasse ao Estado, 
    pois suas etapas de atuação prioritárias são os ensinos fundamental e médio.
    
    Importante enfatizar que o :orange-background[Censo Escolar] é o ponto de partida para o cálculo do repasse
    do Fundeb e de outros programas do FNDE.
    
    Os recursos do Fundo possuem vinculação constitucional e devem ser utilizados exclusivamente na
    :orange-background[manutenção e desenvolvimento do ensino (MDE)].
    
    É a LDB quem define o que é MDE, no seu [artigo 70](https://www.planalto.gov.br/ccivil_03/leis/L9394compilado.htm#:~:text=das%20autoridades%20competentes.-,Art.%2070.,-Considerar%2Dse%2D%C3%A3o). 
    Sob o aspecto da fiscalização, este artigo é fundamental, pois delimita o que pode ser considerado como despesa 
    lícita ou ilícita, de acordo com o regramento do Fundeb.
    
    De largada, duas condicionantes podem ser analisadas neste momento, a fim de se aferir a conformidade do uso dos 
    recursos do Fundeb: (1) a aplicação mínima de 70% dos recursos na remuneração dos profissionais da educação e (2) a execução
    mínima de 90% dos recursos do fundo no mesmo exercício financeiro (anual), com a possibilidade de utilização de até 10% 
    do total do repasse no primeiro quadrimestre do ano seguinte.
    
    Consulte abaixo o desempenho dessas despesas. Basta selecionar o Ente desejado para a geração dos gráficos. Os dados 
    são extraídos da plataforma [SIOPE](https://www.fnde.gov.br/siope/o_que_e.jsp) - Sistema de Informações sobre 
    Orçamentos Públicos em Educação, do FNDE.
    """

def texto_pan_financiamento_fundeb_analise_2():
    return """
    De plano, basta consultar os dados da esfera administrativa desejada e conferir se o percentual mínimo de 70% de 
    gastos com a remuneração dos profissionais da educação foi atingido. Na sequência, verica-se se o percentual
    máximo de 10% de reprogramação de recursos de um exercício para o próximo foi respeitado. O descumprimento de quaisquer
    desses percentuais implica em responsabilidade criminal dos gestores, tema elaborado mais adiante. Fácil, não é?
    
    Entretanto, é muito importante inferir os fatos que estão por trás desses números. A primeira análise interessante é
    verificar se há algum valor que destoa dos demais. Aí, as perguntas vêm naturalmente: O que aconteceu neste ano? 
    Era ano eleitoral? Houve uma mudança de gestão? Houve impugnação de algum certame licitatório? Houve evento 
    climático extremo? Dentre os repasses do Fundeb, existem receitas vinculadas ao cumprimento de metas de qualidade 
    não atingidas? Ou, ainda, houve mudança de legislativa? 
    
    A nova Lei do Fundeb entrou em vigor em dezembro de 2020 e estabeleceu um escalonamento progressivo de 6 anos para sua 
    completa implementação, em especial os percentuais de transferência de recursos da União para Estados e Municípios [(art. 41)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=Disposi%C3%A7%C3%B5es%20Transit%C3%B3rias-,Art.%2041.,-A%20complementa%C3%A7%C3%A3o%20da).
    Logo, se tudo correr bem, é de se esperar um aumento progressivo nos valores dos gráficos, certo? Isso aconteceu no 
    Município de interesse? Se a legislação prevê esse aumento progressivo, o que explica a queda dos valores recebidos 
    de um ano para outro? Se há queda no valor do repasse e o número de profissionais permanecer o mesmo de um ano para 
    o outro, o percentual gasto com sua remuneração deve aumentar, correto?
    
    Outra análise possível é a comparação entre os próprios percentuais analisados. Há correlação entre eles? Ou seja, 
    quanto maior um, menor o outro?
    
    Uma última sugestão de análise muito interessante é a comparação entre Municípios de mesmo porte populacional e características
    geográficas semelhantes. Há semelhanças na comparação ou algum deles destoa dos demais? Se um Município consegue 
    bons resultados, porque o outro não atingiu percentuais semelhantes? Experimente iniciar comparando os Municípios de 
    Santa Rosa do Purus e Jordão. Que te parece?
    
    Em qualquer caso, é plausível estabelecer duas conclusões: quanto maior o gasto com a remuneração dos profissionais,
    menor a chance de reprogramação de recursos do Fundeb para o exercício seguinte. Entretanto, quanto maior este gasto, 
    menor o valor disponível para a execução de outras despesas de MDE, como a construção e reforma de escolas.
    
    As respostas às demais perguntas sugeridas exigem a coleção de mais peças do quebra-cabeças e cada Panorama dará sua 
    contribuição, a seu tempo. De qualquer maneira, de posse dos dados aqui analisados, insta-se que o usuário retorne 
    à página do Panorama da Rede de Ensino e à página do Panorama de Recursos Humanos e prossiga com as comparações. 
    Esse exercício é fundamental para a compreensão da estrutura da rede analisada e consequente exorcismo das assombrações 
    da "reserva do possível" e da "discrionariedade administrativa". O debate é sobre legalidade.
    Adiante.
    """


# VAAT, VAAF, VAAR
def texto_pan_financiamento_fundeb_complementacao_intro():
    return"""
    O Fundeb é composto por recursos provenientes de tranferência e arrecadação de impostos federais, estaduais e municipais, mas a 
    União também participa do financiamento da educação básica pública por meio de complementações. A partir da Lei 14.113/2020, 
    essas complementações pela União devem atingir gradativamente o total de 23% do total dos repasses de Estados e Municípios 
    ao Fundo até o ano de 2026. A novidade é que, além de uma maior contribuição da União, a complementação do Fundeb possui 
    um caracter **redistributivo**, beneficiando os Entes Federativos que possuem uma arrecadação tributária menor.
        
    Agora, há [três modalidades](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=Complementa%C3%A7%C3%A3o%20da%20Uni%C3%A3o-,Art.%204%C2%BA,-A%20Uni%C3%A3o%20complementar%C3%A1) 
    diferentes de complementação, que contribuem com diferentes requisitos e proporções, para se atingir o repasse mínimo de 23% 
    pela União. São elas:
    
    * Complementação **VAAF** (Valor Aluno Ano Fundeb), proporção de **10%**, 
    * Complementação **VAAT** (Valor Aluno Ano Total), proporção de **10,5%**,
    * Complementação **VAAR** (Valor Aluno Ano Resultado), proporção de **2,5%**.
    
    [**VAAF**](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=da%20autoridade%20competente.-,Art.%205%C2%BA,-A%20complementa%C3%A7%C3%A3o%20da)  
    A atual complementação VAAF segue os mesmos critérios de sua versão anterior. Para o seu cálculo, o FNDE define anualmente 
    o "Valor Anual Mínimo por Aluno" (VAAF-MIN), igual para toda a rede de ensino pública brasileira. Então, os Estados que não 
    atingirem esse valor mínimo com os repasses do Fundeb são beneficados com a complementação VAAF. Em razão da maior vocação 
    redistributiva do Fundo, poucos Estados recebem esta complementação, pois já atingem o valor mínimo.
    
    [**VAAT**](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=da%20autoridade%20competente.-,Art.%205%C2%BA,-A%20complementa%C3%A7%C3%A3o%20da)  
    A complementação VAAT é novidade instituída pelo novo Fundeb e possui natureza essencialmente redistributiva, pois contempla
    as redes de ensino com baixa arrecadação tributária. Diferente do VAAF, o cálculo do VAAT é feito por ente federativo. Cada Estado e 
    Município terá o seu VAAT calculado e, se não atingir o valor mínimo do VAAT definido nacionalmente (VAAT-MIN), recebe a complementação.  
    Entretanto, para que o ente federativo faça jus ao repasse, deve ter prestado contas e executado as despesas de acordo com 
    a legislação [(art. 13,  §4º, da Lei 14.113/2020)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=Minist%C3%A9rio%20da%20Educa%C3%A7%C3%A3o.-,%C2%A7%204%C2%BA,-Somente%20s%C3%A3o%20habilitados).
    
    
    
    [**VAAR**](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=da%20autoridade%20competente.-,Art.%205%C2%BA,-A%20complementa%C3%A7%C3%A3o%20da)
    Somente a partir do ano de 2023.
    
    
    A seguir, são apresentados gráficos que mostram a evolução dos repasses do Fundeb, incluindo as complementações VAAF, VAAT e VAAR.
    
    
    
    """
def texto_pan_financiamento_fundeb_complementacao_analise():
    return """
    
    """


# MDE
def texto_pan_financiamento_intro_mde():
    return """
    Receita Orçamentária decorrente de tributos. Vinculação da receita de tributos com despesas em MDE.
    
    Exercício financeiro.
    
    Definicao de MDE. Lembrar que pode ser considerada como MDE a despesa em áreas de atuação não prioritária.
    """

def texto_pan_financiamento_analise_mde():
    return """ """

# Salário Educação
def texto_pan_financiamento_intro_se():
    return """ """

def texto_pan_financiamento_analise_se():
    return """ """

# Programas FNDE
def texto_pan_financiamento_fnde_intro():
    return """ 
    Os repasses de recursos realizados pelo FNDE podem ser classificados em três categorias: constitucionais, automáticos e voluntários.
    Os repasses constitucionais, como o Fundeb, são obrigatórios e definidos pela Constituição Federal. Os repasses automáticos são 
    transferidos diretamente para os entes federativos ou escolas, mediante adesão e cumprimento de critérios legais, sem necessidade 
    de convênio(ex: PNATE, PNAE). Já os repasses voluntários dependem da celebração de convênios ou termos de compromisso, sendo utilizados para 
    apoiar projetos específicos aprovados tecnicamente (ex: Proinfância).
    """

def texto_pan_financiamento_fnde_programas():
    return """ """