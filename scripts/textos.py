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
    
    Além dessas fontes, há também outros programas e ações destinados a promoção da educação básica, como o PNLD, PNAE, PNATE, PDDE. Essas 
    siglas serão detalhadas mais adiante, mas é importante destacar que todas essas fontes de financiamento são geridas pelo Fundo Nacional 
    de Desenvolvimento da Educação ([FNDE](https://www.gov.br/fnde/pt-br)), autarquia vinculada ao Ministério da Educação.
        
    O estudo desse Panorama apresentará uma visão geral do orçamento do FNDE, para que se possa compreender a dimensão dos recursos
    destinados à educação básica pública no Brasil. Em seguida, procura-se descer para a realidade local, inciando o detalhamento
    dessas principais fontes para cada ente federativo, sem pretensão alguma de exaurimento do tema. Determinados programas e ações 
    serão minuciosamente abordados em Panoramas específicos.
    """

# FNDE
def texto_pan_financiamento_fnde_intro():
    return """ 
    O Fundo Nacional de Desenvolvimento da Educação (FNDE) foi criado pelo Decreto-Lei nº 872/69, que alterou a [Lei 5.537/68](https://www.planalto.gov.br/ccivil_03/leis/l5537.htm). 
    Eles conferem ao FNDE a personalidade jurídica de autarquia vinculada ao Ministério da Educação, com o objetivo de captar recursos para o 
    financiamento do ensino e bolsas de estudo. A legislação de regência foi recepcionada pela Constituição Federal de 1988 e permanece
    em vigor, com atualizações legislativas. É ele quem executa a maior parte dos recursos do orçamento federal destinados à educação básica, 
    além de realizar a gestão dos repasses das receitas constitucionais.
    
    Os repasses de recursos realizados pelo FNDE podem ser classificados em três categorias: constitucionais, automáticos e voluntários.
    Os repasses constitucionais, como o Fundeb e o Salário-Educação, são obrigatórios e definidos pela Constituição Federal. Os repasses 
    automáticos são transferidos diretamente para os entes federativos ou escolas, mediante adesão e cumprimento de critérios legais, sem 
    necessidade de convênio (ex: PNAE, PNATE). Já os repasses voluntários dependem de adesão expressa dos entes federativos ou 
    [unidades executoras](https://portal.mec.gov.br/ultimas-noticias/214-296700251/13118-escola-deve-criar-unidade-executora-para-receber-recursos), 
    a celebração de convênios ou de termos de compromisso. O Programa Dinheiro Direto na Escola (PDDE) é um exemplo de repasse 
    voluntário, que necessita de adesão expressa.
    
    Portanto, além da gestão dos repasses do Fundeb e do Salário-Educação, o FNDE também é responsável por gerir 
    outros programas e ações que visam o apoio à educação e possuem regulações próprias para adesão.
    
    Veja abaixo a evolução do orçamento do FNDE, bem como a distribuição dos recursos por categoria de repasse feito pela Autarquia.
    """
    
def texto_pan_financiamento_fnde_analise():
    return """
    O gráfico da evolução do orçamento do FNDE revela o crescimento significativo dos recursos destinados à educação básica pública no 
    Brasil, que se deve em grande medida à nova configuração do Fundeb, que passou a ser permanente e constitucional. A contribuição da 
    União mais que dobrou nos primeiros anos de vigência do novo Fundeb. É importante lembrar que a arrecadação também reflete escolhas
    pol[iticas e momentos econômicos. Note a evidente queda do orçamento durante a pandemia de Covid-19, no ano de 2020.
    
    Por sua vez, o gráfico de distribuição dos recursos por categoria permite uma visão geral da missão do FNDE, que envolve a  transferência 
    de recursos para Estados e Municípios, bem como a gestão de programas voltados ao suporte da educação básica pública. O gráfico mostra 
    ainda que a maior parte dos recursos é destinada ao Fundeb e ao Salário-Educação, que são obrigatórios e definidos pela Constituição 
    Federal. FIES, PNAE, PDDE e PNATE também são programas de destaque.
    
    Feita a devida introdução, passa-se a análise dessas receitas na educação básica pública do Estado do Acre. Serão destacadas as fontes
    de receita mais relevantes para o financiamento do serviço público na ponta, ou seja, aquelas que impactam diretamente as condições
    materiais e humanas de oferta da educação básica pública local. A perscpectiva prática para subsidiar as políticas atuação das Promotorias 
    de Justiça do interior do Estado também estará presente. Os dados apresentados abaixo foram extraídos dos **Relatórios Resumidos de 
    Execução Orçamentária**, ([RREO - art. 165, § 3º CF](https://www.planalto.gov.br/ccivil_03/constituicao/ConstituicaoCompilado.htm#:~:text=DOS%20OR%C3%87AMENTOS-,Art.%20165,-.%20Leis%20de%20iniciativa)),
    disponíveis para consulta na platoforma [SIOPE](https://www.fnde.gov.br/siope/o_que_e.jsp). 
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
    os recursos totais do Fundeb disponíveis para o [exercício financeiro](https://www.congressonacional.leg.br/legislacao-e-publicacoes/glossario-orcamentario/-/orcamentario/termo/exercicio_financeiro) 
    respectivo. Além do principal, estão incluídas as complementações VAAF, VAAT e VAAR, explicadas e discriminadas mais abaixo.
      
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
    :orange-background[manutenção e desenvolvimento do ensino (MDE)], classificação particular de [natureza de despesa](https://www.congressonacional.leg.br/legislacao-e-publicacoes/glossario-orcamentario/-/orcamentario/termo/classificacao_de_natureza_de_despesa)
    que terá reflexos contábeis.
    
    É a LDB quem define o que é MDE, no seu [artigo 70](https://www.planalto.gov.br/ccivil_03/leis/L9394compilado.htm#:~:text=das%20autoridades%20competentes.-,Art.%2070.,-Considerar%2Dse%2D%C3%A3o). 
    Sob o aspecto da fiscalização, este artigo é fundamental, pois delimita o que pode ser considerado como despesa 
    lícita ou ilícita, de acordo com o regramento do Fundeb.
    
    De largada, duas condicionantes podem ser analisadas neste momento, a fim de se aferir a conformidade do uso dos 
    recursos do Fundeb: (1) a aplicação mínima de 70% dos recursos na remuneração dos profissionais da educação e (2) a execução
    mínima de 90% dos recursos do fundo no mesmo [exercício financeiro](https://www.congressonacional.leg.br/legislacao-e-publicacoes/glossario-orcamentario/-/orcamentario/termo/exercicio_financeiro) 
    (anual), com a possibilidade de utilização de até 10% do total do repasse no primeiro quadrimestre do ano seguinte. Ressalva-se que 
    os valores recebidos pela complementação VAAR não integram a base de cálculo para a contabilização do percentual mínimo da remuneração 
    profissional. Além disso, tomou-se por base os valores [empenhados](https://www.congressonacional.leg.br/legislacao-e-publicacoes/glossario-orcamentario/-/orcamentario/termo/empenho)
    e não os valores [liquidados ou efetivamente pagos](https://www.congressonacional.leg.br/legislacao-e-publicacoes/glossario-orcamentario/-/orcamentario/termo/estagio_da_despesa), 
    pois o empenho é o ato que vincula a receita à despesa e será sempre o maior valor possível.
    
    Consulte abaixo o desempenho dessas despesas. Basta selecionar o Ente desejado para a geração dos gráficos. Os dados 
    são extraídos da plataforma [SIOPE](https://www.fnde.gov.br/siope/o_que_e.jsp) - Sistema de Informações sobre 
    Orçamentos Públicos em Educação, do FNDE.
    """

def texto_pan_financiamento_fundeb_analise_2():
    return """
    De plano, basta consultar os dados da esfera administrativa desejada e conferir se o percentual mínimo de 70% de 
    gastos com a remuneração dos profissionais da educação foi atingido. Na sequência, verifica-se se o percentual
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
    menor o valor disponível para a execução de outras despesas em MDE, como a construção e reforma de escolas.
    
    As respostas às demais perguntas sugeridas exigem a coleção de mais peças do quebra-cabeças e cada Panorama dará sua 
    contribuição, a seu tempo. De qualquer maneira, de posse dos dados aqui analisados, insta-se que o usuário retorne 
    à página do Panorama da Rede de Ensino e à página do Panorama de Recursos Humanos e prossiga com as comparações. 
    Esse exercício é fundamental para a compreensão da estrutura da rede analisada e consequente exorcismo das assombrações 
    da "reserva do possível" e da "discrionariedade administrativa". O debate é sobre legalidade.
    Adiante.
    """

# VAAT, VAAF, VAAR
def texto_pan_financiamento_fundeb_complementacao_intro():
    return """
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
    redistributiva do Fundo, poucos Estados recebem esta complementação, pois já atingem o valor mínimo ([art. 12 da Lei 14.113/20](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=Complementa%C3%A7%C3%A3o%20da%20Uni%C3%A3o-,Art.%2012,-.%C2%A0%20A%20complementa%C3%A7%C3%A3o%2DVAAF)).
    Em qualquer caso, os valores recebidos nesta modalidade de complementação devem ser destinados exclusivamente a despesas com 
    manutenção e desenvolvimento do ensino (MDE).
    
    [**VAAT**](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=da%20autoridade%20competente.-,Art.%205%C2%BA,-A%20complementa%C3%A7%C3%A3o%20da)  
    A complementação VAAT é novidade instituída pelo novo Fundeb e possui natureza essencialmente redistributiva, pois contempla
    as redes de ensino com baixa arrecadação tributária. Diferente do VAAF, o cálculo do VAAT é feito por ente federativo. Cada Estado e 
    Município terá o seu VAAT calculado e, se não atingir o valor mínimo do VAAT definido nacionalmente (VAAT-MIN), recebe a complementação.  
    Entretanto, para que o ente federativo faça jus ao repasse, deve ter cumprido a condicionalidade de prestação de contas e 
    execução das despesas de acordo com a legislação [(art. 13,  §4º, da Lei 14.113/2020)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=Minist%C3%A9rio%20da%20Educa%C3%A7%C3%A3o.-,%C2%A7%204%C2%BA,-Somente%20s%C3%A3o%20habilitados).
    Esta modalidade de complementação exige que os valores recebidos sejam destinados para despesas de capital, na proporção de 15%, e 
    com despesas com educação infantil, para os Municípios, na proporção de 50%. O restante deve ser destinado para despesas em MDE [(arts. 27 e 28)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=despesas%20de%20capital.-,Art.%2028,-.%C2%A0%20Realizada%20a%20distribui%C3%A7%C3%A3o).
    
    [**VAAR**](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=da%20autoridade%20competente.-,Art.%205%C2%BA,-A%20complementa%C3%A7%C3%A3o%20da)  
    Por fim, a complementação VAAR também é outra inovação legislativa e garante o repasse ao ente federativo que cumpriu as 
    condicionalidades de melhoria de gestão, de atendimento, aprendizagem e redução das desigualdades ([art. 14 da Lei do Fundeb](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm#:~:text=da%20autoridade%20competente.-,Art.%205%C2%BA,-A%20complementa%C3%A7%C3%A3o%20da)).  
    Os repasses dessa complementação se iniciaram a partir do ano de 2023, para atender a implementação progressiva da nova política de 
    financiamento educacional.  
    O art. 14 apresenta as cinco condicionalidades que devem ser atingidas pela rede educacional. Salienta-se as condicionalidades
    II e III, que dizem respeito à participação de no mínimo 80% dos alunos da rede na prova do Sistema de Avaliação da Educação Básica
    (SAEB) e a redução das desigualdades educacionais e socioeconômicas. Ambas são calculadas pelo INEP, com base nos dados fornecidos 
    ao **Censo Escolar** e nas avaliações do SAEB.
        
    A seguir, são apresentados gráficos que discriminam a evolução dos repasses do Fundeb e as respectivas complementações VAAF, VAAT e VAAR, 
    a partir do ano de 2021.
    """
    
def texto_pan_financiamento_fundeb_complementacao_analise():
    return """
    Note que os valores dos repasses do Fundeb crescem com consistência, refletindo a implementação gradual da nova política de
    financiamento da educação. Em especial, refletem também o momento econômico.  
    
    Entretanto, o quadro muda quando se olha para as complementações. Nenhum ente federativo recebeu repasse da complementação VAAF pois,
    como dito antes, são poucos os Estados que não atingem o valor mínimo do VAAF. Entretanto, as complementações VAAT e VAAR são interessantes
    de serem observadas, **em especial por causa de suas condicionalidades**. 
    
    No que diz respeito à complementação VAAT, o seu não recebimento pelo ente é **indicativo de ausência de prestação de contas** e aponta
    para o cometimento de crime de responsabilidade do Prefeito. Como exemplo, pode-se verificar o Município de Bujari, que foi inabilitado
    pelo FNDE para receber a complementação nos anos de 2021 a 2023, pela não prestação das contas. A informação atualizada a respeito
    das prestações de contas dos entes é encontrada na plataforma [SIOPE](https://www.fnde.gov.br/siope/recibosTransmissao.do).
    
    Por sua vez, o não recebimento da complementação VAAR é indicativo de descumprimento de normas de organização administrativa escolar, má 
    cobertura da rede, falta de participação de alunos nas avaliações do SAEB, preenchimento incorreto do Censo Escolar, ou baixo rendimento
    dos alunos, segundo os critérios da avaliação nacional.
    
    Portanto, mais do que recursos, as complementações auxiliam no diagnóstico da rede escolar que deve ser fiscalizada e aponta possíveis
    falhas de gestão que podem ser endereçadas com base na legalidade, ou na falta dela, dos atos praticados pela administração escolar. 
    """

# MDE
def texto_pan_financiamento_receita_minima_impostos_intro():
    return """
    Este tópico trata da vinculação da receita proveniente de impostos a despesas com MDE, assim definidas no [art. 70](https://www.planalto.gov.br/ccivil_03/leis/L9394compilado.htm#:~:text=das%20autoridades%20competentes.-,Art.%2070,-.%20Considerar%2Dse%2D%C3%A3o) 
    da LDB.
    
    Como explicado anteriormente, o [art. 212](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm#:~:text=Art.%20212.-,A%20Uni%C3%A3o%20aplicar%C3%A1,-%2C%20anualmente%2C%20nunca%20menos)
    da Constituição Federal determina a Estados e Municípios a aplicação **mínima** de 25% da receita proveniente de impostos em despesas 
    com MDE.  
    Desse total, 20% são destinados à composição do Fundeb. Os **5% restantes** são contabilizados a partir dos **elementos de despesa 
    atribuídos a MDE**, discriminados nas respectivas prestações de contas.  
    Portanto, o seu cálculo leva em conta o total da arrecadação proveniente de impostos e o total das despesas em MDE, que deve atingir 
    o mínimo de 5% naquele exercício financeiro. Como explicado anteriormente, este valor irá variar de acordo com a arrecadação 
    tributária do ente federativo.  
    
    Consulte abaixo o total de arrecadação proveniente de impostos e o total de despesas em MDE para o cálculo da receita mínima de 5% em 
    impostos. 
    Para a criação do gráfico, foi considerado o valor [empenhado](https://www.congressonacional.leg.br/legislacao-e-publicacoes/glossario-orcamentario/-/orcamentario/termo/empenho) 
    como despesa em MDE para o exercício, pois é o maior parâmetro possível.  
    Os dados foram extraídos da plataforma SIOPE, do FNDE, e estão disponíveis a partir do ano de 2021.    
    """

def texto_pan_financiamento_receita_minima_impostos_analise():
    return """
    Agora ficou fácil verificar se o ente federativo atingiu o mínimo de 5% de receitas provenientes de impostos para a educação, em despesas 
    com MDE.  
    
    É importante lembrar que há uma diferença entre a vinculação da receita destinada ao Fundeb e a receita mínima de impostos para MDE.
    Se no Fundeb são permitidas despesas em MDE **somente nas áreas de atuação prioritária**, a receita mínima de 5% proveninente de impostos 
    pode ser executada em áreas não prioritárias, mas sempre em MDE.  
    O que deve ficar claro é que o não cumprimento do mínimo legal, para além de aspectos formais ou criminais, impacta diretamente a 
    qualidade da educação, pois reflete a disponibilidade de recursos materiais e humanos para prestação do seviço público.  
    
    Outro ponto de atenção é que os entes federativos devem apresentar seus Relatórios Resumidos de Execução Orçamentária (RREO) 
    **bimestralmente**, durante o exercício. Assim, invés de aguardar o julgamento das contas pelo Tribunal de Contas Estadual, é
    possível consultar esses relatórios parciais e verificar se o ente está cumprindo com a vinculação mínima de 5% da receita de impostos
    em despesas com MDE durante o exercício. O RREO bimestral serve de guia para uma atuação preventiva. Basta acessar a plataforma do 
    [SIOPE](https://www.fnde.gov.br/siope/relatorioRREOMunicipal2006.do), e procurar pelo RREO do ente em questão. Por fim, o 
    descumprimento da determinação será endereçada adiante.
    """
    
# Salário-Educação
def texto_pan_financiamento_salario_educacao_intro():
    return """
    O Salário-Educação também possui uma longa história no financiamento da educação pública brasileira. Foi criado no ano de 1964 e, 
    atualmente, possui previsão constitucional ([art. 212, §5°](https://www.planalto.gov.br/ccivil_03/constituicao/ConstituicaoCompilado.htm#:~:text=outros%20recursos%20or%C3%A7ament%C3%A1rios.-,%C2%A7%205%C2%BA,-A%20educa%C3%A7%C3%A3o%20b%C3%A1sica)),
    com regulamentação pelas Leis [9.424/96](https://www.planalto.gov.br/ccivil_03/LEIS/L9424compilado.htm) e [9.766/98](https://www.planalto.gov.br/ccivil_03/LEIS/L9766.htm).
    Diferente do Fundeb, que é financiado por meio de impostos, o Salário-Educação é financiado por meio de contribuições sociais, com 
    alíquota de 2,5% sobre a folha de salários das empresas. Do total da arrecadação líquida, 10% são destinados ao FNDE para financiamento
    projetos, programas e ações da educação básica. Os outros 90% são rateados entre a União, Estados e Municípios, na proporção de 1/3 
    para a União e 2/3 para os Estados e Municípios. O rateio é proporcional  ao número de alunos matriculados no respectivo sistema de 
    ensino ([art. 9° do Decreto 6003/2006](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/decreto/D6003.htm#:~:text=ao%20da%20arrecada%C3%A7%C3%A3o.-,Art.%C2%A09,-o%C2%A0%C2%A0O%20montante)),
    assim declarado no :orange-background[Censo Escolar]. A quota da União também é destinada para financiamento de programas, projetos e 
    ações educacionais voltados à redução das desigualdades regionais. **Estados e Municípios**, por sua vez, devem utilizar a receita 
    proveniente do **Salário-Educação exclusivamente com MDE**, vedado o seu uso para pagamento de pessoal.
    """

def texto_pan_financiamento_salario_educacao_analise():
    return """
    A comparação das receitas entre os exercícios financeiros permite identificar um incremento significativo no repasse no ano de 2024. 
    O motivo para este salto é que, até o ano de 2023, o FNDE utilizava como critério não somente o número de alunos matriculados no respectivo
    sistema de ensino, mas a origem da arrecadação. O montante arrecadado a partir da contribuição social em cada Estado da Federação lá 
    permanecia para o rateio sobre o número de matrículas de seus respectivos sistemas de ensino. Essa metodologia fomenta as desigualdades 
    regionais, pois Estados com maior arrecadação recebem valores maiores, mesmo que o número de matrículas seja menor. 
    
    No ano de 2009 foi interposta a [ADPF 188](https://portal.stf.jus.br/processos/detalhe.asp?incidente=3698566) 
    para que os repasses da Salário-Educação obedecessem somente o critério do número de matrículas, independentemente da origem da 
    arrecadação. Ela foi julgada procedente pelo STF no ano de 2022, fixando a tese de que “À luz da Emenda Constitucional 53/2006, é 
    incompatível com a ordem constitucional vigente a adoção, para fins de repartição das quotas estaduais e municipais referentes ao 
    salário-educação, do critério legal de unidade federada em que realizada a arrecadação desse tributo, devendo-se observar unicamente 
    o parâmetro quantitativo de alunos matriculados no sistema de educação básica”.
    
    Esse julgamento eleva a importância do Salário-Educação como fonte de financiamento da educação, em especial para os Estados com menor 
    arrecadação, pois permite à contribuição atingir a sua finalidade de atender a educação básica dos alunos brasileiros, independentemente 
    do lugar onde vivem.
    
    Com relação à fiscalização, o Salário-Educação é um recurso vinculado constitucionalmente e deve ser utilizado exclusivamente em MDE.
    Os repasses são depositados em conta específica de cada ente federativo para movimentação dessa receita, embora haja menos transparência
    e controle social, quando comparado com a legislação do Fundeb. A prestação de contas é feita perante os Tribunais de Contas Estaduais. 
    Como consequência, fica firmada a atribuição do Ministério Público Estadual para a fiscalização dessa fonte de receita.
    """

# Outras receitas do FNDE
def texto_pan_financiamento_receitas_adicionais_intro():
    return """
    Além das transferências constitucionais obrigatórias, Estados e Municípios também recebem recursos provenientes de [operações de 
    crédito](https://www.congressonacional.leg.br/legislacao-e-publicacoes/glossario-orcamentario/-/orcamentario/termo/operacao_de_credito) 
    e [royalties do petróleo](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12858.htm). 
    
    Ainda, recebem repasses suplementares do FNDE a partir de [ações e programas](https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas) 
    de apoio à educação. Cada programa procura endereçar uma necessidade específica, com  regulamentação própria. Guardando o viés prático 
    deste trabalho, esses programas serão escrutinados nos respectivos Panoramas temáticos. Entretanto, uma breve introdução é necessária 
    para que se compreenda a importância desses recursos e o seu potencial de impacto para o quadro local. 
    
    O Programa Nacional de Alimentação Escolar ([PNAE](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/lei/l11947.htm)) e o
    Programa de Apoio ao Transporte Escolar ([PNATE](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.880.htm)) são
    recursos de transferência automática e levam em conta o número de alunos matriculados no respectivo sistema de ensino, declarados 
    no :orange-background[Censo Escolar]. 
    
    Outro programa de destaque é o Plano de Ações Articuladas (PAR - [Decreto 6094/2007](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6094.htm) e
    [Lei 12.695/12](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12695.htm)), que se propõe a oferecer apoio técnico e
    financeiro aos Estados e Municípios, com o objetivo de promover a melhoria da qualidade da educação. Para acessar os recursos do PAR, 
    os entes federativos devem elaborar um diagnóstico e respectivo plano de ação, para celebração de **convênios** com o FNDE. Os recursos 
    do PAR contemplam quatro eixos de atuação: gestão educacional, formação de profissionais de educação, práticas pedagógicas e avaliação e
    infraestrutura física e recursos pedagógicos.
    
    Por fim, é necessário destacar o Programa Dinheiro Direto na Escola ([PDDE](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/lei/l11947.htm)), 
    que tem como objetivo prestar assistência financeira suplementar às escolas públicas, mediante adesão. As escolas contempladas são 
    definidas anualmente pelo FNDE a partir dos dados do :orange-background[Censo Escolar].
    
    Visualize abaixo o gráfico que mostra os valores recebidos por categoria de receitas ainda não discriminadas nos tópicos anteriores.
    """
    
def texto_pan_financiamento_receitas_adicionais_analise():
    return """
    Esse gráfico possui muitas informações relevantes, e deve ser analisado com paciência e atenção. A primeira análise é a comparação 
    individual de cada ente, no tempo. Note que o valor de cada uma das receitas varia de ano para ano. O natural então é se perguntar os
    motivos para essa variação. Respostas possíveis são a mudança na arrecadação de tributos, momento econômico, mudança na metodologia de
    cálculo. 
    
    Como foi visto no início, as receitas do FNDE estão aumentando ano a ano. Logo,  a expectativa é de que as receitas adicionais repassadas 
    a Estados e Municípios também aumentem, concorda?
    
    Nesse caso, a diminuição da receita no tempo pode ser um indicativo de **falha grave na gestão**. Tome a receita do PNAE, por exemplo. 
    Ele é um repasse automático que leva em conta o número de alunos. Entretanto, existem condicionalidades que devem ser observadas pelos 
    entes na execução do programa. O descumprimento dessas condicionalidades pode levar à diminuição ou mesmo a suspensão do repasse no ano 
    seguinte. Esse foi o caso da Secretaria Estadual de Educação, por exemplo.
    
    Outra receita interessante de se analisar é aquela proveniente de convênios celebrados com o FNDE. Se não existem receitas dessa fonte, é
    sinal de que o ente não está participando do PAR, pois esse programa é executado mediante celebração de convênio. O mesmo vale para os 
    recursos do PDDE. Eles são captados mediante adesão do ente ao programa específico. Se não existem recursos dessa fonte, é sinal de que 
    há omissão grave na gestão educacional em acessa-los. Insiste-se que cada um dos programas citados serão minuciosamente analisados nos 
    Panoramas temáticos. Por hora, o foco é apenas uma introdução às possibilidades de análise.
    
    Nessa picada, vamos analisar o impacto da gestão na captação do PDDE pelos entes?
    
    """
    

