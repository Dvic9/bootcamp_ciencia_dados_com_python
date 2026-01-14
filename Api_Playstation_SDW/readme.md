🎮 PSN Stats & Marketing API - ETL Challenge

Este projeto implementa um pipeline de ETL (Extract, Transform, Load) focado no ecossistema PlayStation. Ele utiliza uma API customizada para gerenciar dados de jogadores e o poder da Inteligência Artificial (Google Gemini) para gerar recomendações de marketing personalizadas.

📋 Descrição do Projeto

O sistema simula uma operação de marketing da PlayStation onde:

Dados de Jogadores (PSN ID, gênero favorito, plano de assinatura) são armazenados e servidos por uma API.

Um Pipeline Automatizado consome esses dados.

Uma IA (Gemini) atua como especialista de marketing para sugerir novos jogos.

O sistema Carrega essas sugestões de volta para o perfil do usuário via notificações.

🏗️ Estrutura de Arquivos

main.py: Servidor Backend construído com FastAPI. Utiliza um arquivo CSV (playstation_db.csv) como banco de dados persistente (Ao menos enquanto não há deploy novo), empregando ast.literal_eval para garantir a integridade de objetos complexos (JSON) dentro do CSV.

pipeline_psn_etl.ipynb: Notebook Jupyter contendo o fluxo completo de ETL e scripts de população inicial de dados.

jogadores_id.csv: Arquivo de entrada para o Pipeline, contendo os IDs dos jogadores que devem ser processados.

requirements.txt: Lista de dependências necessárias para rodar o ambiente.

🛠️ Tecnologias Utilizadas

FastAPI & Uvicorn: Para a criação e execução da API REST.

Pandas: Para manipulação de dados e interface com o banco de dados CSV.

Pydantic: Para validação de esquemas de dados.

Google Generative AI SDK: Para integração com o Gemini (Moisés).

Requests: Para comunicação entre o Pipeline e a API.

🚀 Como Executar

1. Preparação do Ambiente

Instale as bibliotecas necessárias:

pip install -r requirements.txt


2. Execução da API

Inicie o servidor localmente:

uvicorn main:app --reload


Nota: Se estiver usando a versão em nuvem, a URL configurada no projeto é: https://bootcamp-ciencia-dados-com-python.onrender.com. O objetivo foi gerar uma api para funcionar de acordo com o exemplo do desafio. [Clique aqui para consultar a documentação](https://bootcamp-ciencia-dados-com-python.onrender.com/docs).

3. Execução do Pipeline (ETL)

Abra o arquivo pipeline_psn_etl.ipynb.

Configuração da Chave: Na célula de configuração, localize a variável GEMINI_API_KEY e substitua pelo seu token válido do Google AI Studio.

GEMINI_API_KEY = "SUA_CHAVE_AQUI"

Execute as células em ordem:

Célula 1: Popula a API com jogadores de teste.

Célula 2: Define as funções de ETL e executa o processo de recomendação via IA.

🧪 Fluxo ETL Detalhado

EXTRACT: O script lê o arquivo jogadores_id.csv, extrai os IDs e faz uma requisição GET para a API para obter o perfil completo de cada jogador.

TRANSFORM: O modelo Gemini analisa o favorite_genre e o plan de assinatura. Ele gera uma mensagem de até 140 caracteres recomendando um jogo específico que combine com o perfil.

LOAD: O script anexa a nova mensagem à lista de notifications do objeto jogador e realiza um PUT na API para atualizar o banco de dados.

Desenvolvido por: [Dvic](https://github.com/Dvic9)
