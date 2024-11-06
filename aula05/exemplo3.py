from sqlalchemy import create_engine
import pandas as pd 


host = 'Localhost'
user = 'root'
password = 'root'
database = 'bd_vendas'


engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')



# carregar dados dantabela do banco exemplo3
query_clientes = "SELECT id_cliente, nome, email, FROM tb_clientes"
df_clientes = pd.read_sql(query_clientes, engine)

# carregar dados da tabela 'pedidos' do arquivos excel
df_pedidos = pd.read_excel('tb_pedidos.xlsx')

# ralcionar os dados usando merge
df_relacionado = pd.merge(df_pedidos, df_clientes, on='id_clientes', how='inner')

# ordenar o dataframe relacionado pela coluna 'id_clientes'
df_relacionado = df_relacionado.sort_values(by='nome')

# exibir o resultado
print(df_relacionado)