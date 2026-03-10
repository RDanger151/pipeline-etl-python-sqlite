# pipeline-etl-python-sqlite

Pipeline de ETL com Python e Pandas
Este projeto é uma esteira de dados completa (ETL) construída para extrair informações de uma API, transformar os dados e carregá-los em um Banco de Dados Relacional.

Ferramentas Utilizadas:

Python & Requests: Extração de dados da API FakeStore (JSON).

Pandas: Limpeza de dados nulos, conversão de moedas e regras de negócio.

SQLite3 & SQL: Criação de banco de dados e consultas (SELECT, WHERE) para gerar relatórios finais.

Como funciona: O script baixa os produtos, remove colunas incompatíveis (dicionários aninhados), calcula o preço em reais e salva apenas a categoria de Eletrônicos no banco de dados, retornando os itens mais caros.
