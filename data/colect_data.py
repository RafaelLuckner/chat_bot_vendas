import pandas as pd 
import numpy as np
import psycopg2
from dotenv import load_dotenv 
import os 

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Conectar ao banco
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port="5432"

)

# Criar um cursor e executar uma consulta
cursor = conn.cursor()
cursor.execute("SELECT * FROM vendas")
dados = cursor.fetchall()

# Fechar conexão
cursor.close()
conn.close()

print(dados[1])
dados = pd.DataFrame(dados, columns=['id_venda','email_vendedor', 'momento_venda', 'valor_venda', 'qtd_produtos', 'produto'])
dados.to_csv('vendas.csv', index=False)