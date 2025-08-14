# Linhagem dos dados utilizados no Observatório Curica

## Página Panorama Rede de Ensino

* Microdados do Censo Escolar

        Dados abertos do Inep.
        Link: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar
        -> dataframes processados: df_panorama_geral.csv, df_panorama_agua.csv



## Página Panorama Financiamento

* Receitas FNDE
  Painel do Orçamento Federal.
  -> dataframe raw extraído: 
    df_receita_fnde.csv
    Processado no notebook df_receita_fnde.ipynb

* Despesas FNDE
  Relatórios de Gestão do FNDE.
  Link: https://www.gov.br/fnde/pt-br/acesso-a-informacao/transparencia-e-prestacao-de-contas/relatorio-de-gestao-1
  Parser "despesas_fnde"
  -> dataframe raw extraído: 
    df_despesas_fnde.csv
    Processado no notebook df_despesas_fnde.ipynb

* Repasses Fundeb
  Tesouro Nacional.
  Link: https://sisweb.tesouro.gov.br/apex/f?p=2600:1
  -> dataframes processados: df_fundeb_estado.csv, df_fundeb_municipios.csv, df_fundeb_ac_completo.csv

* Relatórios Resumidos de Execução Orçamentária, RREO's:
  SIOPE
  Link: https://www.fnde.gov.br/siope/o_que_e.jsp

  -> dataframe raw extraídos:
    df_rreo_parser.csv
  
  -> dataframes processados: df_panorama_financiamento.csv
    Primeiro foi utilizado o pipeline do parser e então o notebook df_financiamento.ipynb para processar os dados.

* Receitas provenientes do FNDE:
  Painel do Orçamento Federal.
  Link: https://www1.siop.planejamento.gov.br/QvAJAXZfc/opendoc.htm?document=IAS%2FExecucao_Orcamentaria.qvw&host=QVS%40pqlk04&anonymous=true?lang=en-US&opendocqs=

  -> dataframes raw extraídos: 
      df_receitas_mec_2019_2024.csv, df_receita_fnde_total_2019_2024.csv, df_receita_fnde_fonte_2019_2024.csv


* Emendas parlamentares:
  Painel do Orçamento Federal.
  Link: https://www1.siop.planejamento.gov.br/QvAJAXZfc/opendoc.htm?document=IAS%2FExecucao_Orcamentaria.qvw&host=QVS%40pqlk04&anonymous=true?lang=en-US&opendocqs=
  
  -> dataframes raw extraídos: 
      df_emendas_geral_2019_2024.csv, df_emendas_mec_2019_2024.csv
  
  -> dataframes processados: 


## Página Panorama Infraestrutura

* PAR
  SIMEC - Transparência Pública - Obras FNDE
  Link: https://simec.mec.gov.br/painelObras/index.php
  
  -> dataframe raw extraído: 
    df_simec_obras_par.csv




# Referências bibliográficas

## Orçamento

Glossário de termos orçamentários
https://www.congressonacional.leg.br/legislacao-e-publicacoes/glossario-orcamentario

Fonte ou destinação de recursos
https://www.gov.br/tesouronacional/pt-br/contabilidade-e-custos/federacao/fonte-ou-destinacao-de-recursos

FNDE 50 anos.
https://www.gov.br/fnde/pt-br/acesso-a-informacao/institucional/biografia/55anosdeFNDEversaovirtual.pdf

Correlação entre repasses e Ideb - Tese Doutorado
https://teses.usp.br/teses/disponiveis/12/12136/tde-26072012-113928/pt-br.php

### Fundeb

Manual Novo FUNDEB
https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/financiamento/fundeb/ManualNovoFundeb2021.pdf

Cartilha Novo FUNDEB
https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/financiamento/fundeb/CartilhaNovoFundeb2021.pdf

Novo Fundeb - TCE-SP
https://www.tce.sp.gov.br/publicacoes/novo-fundeb-perguntas-e-respostas

Fundeb Perguntas e Respostas
https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/financiamento/fundeb/manuais-a-cartilhas-1/perguntas-e-respostas_atualizacao_11_10_22.pdf

Fundeb e CACs TCE-AC
https://tceac.tc.br/site/wp-content/uploads/2024/10/CARTILHA-FUNDEB-final.pdf

Fundeb e Mínimo Constitucional
https://apet.org.br/artigos/o-fundeb-e-os-minimos-constitucionais-da-educacao/#:~:text=Em%20tal%20contexto%2C%20somente%20a,se%20automaticamente%20nos%2025%25%20constitucionais.

Metodologia cálculo Fundeb segmentos
https://cadernosdeestudos.inep.gov.br/ojs3/index.php/cadernos/article/view/6511

PNE
https://pne.mec.gov.br/images/pdf/pne_conhecendo_20_metas.pdf

Indicadores da Meta 01 do PNE
https://cadernosdeestudos.inep.gov.br/ojs3/index.php/cadernos/article/view/1007

Escolas em localização diferenciada
https://cadernosdeestudos.inep.gov.br/ojs3/index.php/cadernos/article/view/6503

Evasão escolar em terras indígenas
https://cadernosdeestudos.inep.gov.br/ojs3/index.php/cadernos/article/view/6504

# Legislação

LDB
https://www.planalto.gov.br/ccivil_03/leis/L9394compilado.htm

FUNDEB
https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14113.htm

PNE
https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13005.htm

Movimentação do Fundeb
https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/financiamento/fundeb/legislacao/2022/portaria-conjunta-no-3-de-29-de-dezembro-de-2022

Resolução FNDE prestação de contas quadrienal PNAE
https://www.in.gov.br/web/dou/-/resolucao-cd/fnde-n-7-de-2-de-maio-de-2024-557685634

Salário Educação
https://www.planalto.gov.br/ccivil_03/LEIS/L9766.htm

# Jurisprudência

ADI 5791 - Competência dos TCEs e TCU
https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=493795&ori=1