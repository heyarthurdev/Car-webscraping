🚗 Web Scraping de Carros

Projeto de web scraping em Python desenvolvido para praticar a extração de informações de páginas HTML utilizando Requests e BeautifulSoup.

O programa permite escolher uma página do site de testes do Web Scraper, extrair os dados dos carros disponíveis e armazená-los em um arquivo .csv.

🛠️ Tecnologias utilizadas
Python
Requests
BeautifulSoup4
CSV
Matplotlib

📋 Dados coletados
Para cada carro, o programa coleta:

Nome
Descrição
Ano
Disponibilidade

🚀 Como executar
1. Clone o repositório
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
2. Instale as dependências
pip install requests beautifulsoup4
3. Execute o programa
python main.py

O programa solicitará o número da página que você deseja consultar.

Qual página você quer ler?: 5

Os dados encontrados serão exibidos no terminal e salvos em um arquivo CSV correspondente à página escolhida.

📁 Estrutura do projeto
.
├── main.py
├── scraper.py
├── carros_pagina*.csv
├── .gitignore
└── README.md
🎯 Objetivo

Este projeto foi desenvolvido como prática de:

Requisições HTTP com Python
Parsing de HTML
Localização de elementos com BeautifulSoup
Extração de dados
Manipulação de arquivos CSV
Organização de código em módulos
Uso do Git e GitHub
📌 Observação

Este projeto utiliza o site de testes Web Scraper como fonte dos dados e possui finalidade educacional.