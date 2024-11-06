from sqlalchemy import create_engine
import pandas as pd 

host = 'Localhost'
user = 'root'
password = 'root'
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')




# leirura de dados
df_estoque = pd.read_sql('tb_produtos', engine)
# somente os 5 valores
print(df_estoque.head())

# calcula o valor do estoque em linha
df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']

print(df_estoque[['NomeProduto', 'TotalEstoque']])

# calcula o valor do total do estoque
print(f'Total geral em estoque: R${df_estoque["TotalEstoque"].sum()}')
