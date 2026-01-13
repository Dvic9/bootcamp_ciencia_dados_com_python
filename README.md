Dashboard de Assinaturas PlayStation Plus - Análise de Vendas e Retenção

1. Visão Geral do Projeto

Este projeto foi desenvolvido como parte de um bootcamp de análise de dados. Diferente da abordagem padrão sugerida (focada no ecossistema Xbox), este trabalho foi construído do zero utilizando como temática a PlayStation Plus.

A decisão de "sair da bolha" e não utilizar o modelo pronto fornecido teve como objetivo aplicar os conceitos de ETL (Extração, Transformação e Carga), modelagem de dados e criação de dashboards de forma autoral, garantindo que cada métrica e KPI fizesse sentido dentro de um cenário de mercado real e atualizado.

2. Diferenciais deste Projeto

Autoralidade Total: Toda a base de dados  foi gerada especificamente para este cenário, ignorando o "copia e cola" de modelos pré-existentes.

Fidelidade ao Mercado: Foram utilizados os planos reais da PlayStation (Essential, Extra e Deluxe) com seus respectivos valores de mercado brasileiro (mensal, trimestral e anual).

Inteligência de Add-ons: Implementação de uma lógica de venda cruzada (Cross-selling) com serviços complementares como Ubisoft+ Classics e Pacotes Exclusivos de Fortnite.

Análise de Cenários: Criação de colunas calculadas para identificar perfis de consumo (ex: usuários que assinam apenas serviços extras vs. usuários de planos base).

3. Estrutura do Arquivo

O projeto está dividido em quatro pilares fundamentais:

A - Assets: Identidade visual baseada na paleta de cores oficial da Sony (Azul Royal, Azul Neon e Dark Mode).

B - Bases: Base de dados bruta contendo ID do assinante, Plano, Período de Pagamento, Data de Início, Renovação Automática e indicadores de Add-ons.

C - Cálculos: Processamento dos dados através de Tabelas Dinâmicas para responder perguntas críticas de negócio, como faturamento por plano e taxa de retenção por auto-renovação.

D - Dashboard: Visualização final dos dados, consolidando os principais indicadores para tomada de decisão.

4. Perguntas de Negócio Respondidas

Faturamento por Plano/Período: Qual o plano que mais gera receita bruta para a plataforma?

Volumetria de Assinantes: Qual a distribuição de usuários entre os níveis de serviço?

Comportamento de Retenção: Qual a quantidade de assinantes que optam pela renovação automática e também consomem pacotes exclusivos de Fortnite?

Adesão a Serviços de Terceiros: Qual o impacto da parceria com a Ubisoft na base de assinantes com renovação ativa?

5. Tecnologias e Metodologia

Excel/Google Sheets: Utilizado para manipulação de strings, fórmulas condicionais (SES, CONT.SES, PROCV) e tabelas dinâmicas.

Metodologia Ágil: Desenvolvimento iterativo, desde a concepção da base fictícia até a validação das métricas.

Nota: Todos os dados contidos neste projeto são fictícios e foram gerados apenas para fins de estudo, prática e demonstração de competências técnicas em análise de dados.
