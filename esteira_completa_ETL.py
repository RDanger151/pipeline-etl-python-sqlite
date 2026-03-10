import requests
import pandas as pd
import sqlite3


# 1. EXTRACT (Extrair da API)
url = "https://fakestoreapi.com/products"

# Requests.get na url
resposta = requests.get(url)

# Transformando a resposta em JSON
dados_json = resposta.json()

# Transformando o JSON em um DataFrame do Pandas chamado 'df'
df = pd.DataFrame(dados_json)


# 2. TRANSFORM (Transformar com Pandas)
# Criando uma nova coluna chamada 'preco_real' que seja o 'price' multiplicado por 5.0

df['preco_real'] = df['price'] * 5.0
print(df.head())
# Criando um novo DataFrame chamado 'df_eletronicos' filtrando o df apenas onde a 'category' seja igual a "electronics"
df_eletronicos =  df[df['category'] == 'electronics']
print(df_eletronicos)


# 3. LOAD (Carregar no Banco de Dados)

# Conectando ao banco
conexao = sqlite3.connect('loja_produtos.db')

# Deletando coluna 'rating' pois veio como dicionádio
df_eletronicos = df_eletronicos.drop(columns=['rating'])

# Salvando a tabela inteira direto no SQL
df_eletronicos.to_sql('tabela_eletronicos', conexao, if_exists='replace', index=False)


# 4. Consultar com SQL

# Criando query Selecionando tudo da 'tabela_eletronicos' ONDE o 'preco_real' seja maior que 500.
query1 = "SELECT * FROM tabela_eletronicos WHERE preco_real > 500"

# lendo o resultado e guardando numa variável chamada 'resultado_sql'.
resultado_sql = pd.read_sql_query(query1,conexao)
# Imprimindo o resultado final
print(resultado_sql)

conexao.close()