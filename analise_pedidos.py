import pandas as pd

clientes_df = pd.read_csv("clientes.csv")
pedidos_df = pd.read_csv("pedidos.csv")

merged_df = pd.merge(clientes_df, pedidos_df, left_on='id', right_on='cliente_id')

grouped_df_count = merged_df.groupby(['email'])['email', 'valor_total'].count()
grouped_df_sum = merged_df.groupby(['email'])['email', 'valor_total'].sum()
grouped_df_max = merged_df.groupby(['email'])['email', 'valor_total'].max()
grouped_df_min = merged_df.groupby(['email'])['email', 'valor_total'].min()
grouped_df_mean = merged_df.groupby(['email'])['email', 'valor_total'].mean()

print("-" * 30 + " QUANTIDADE DE PEDIDOS POR CLIENTES " + "-" * 30)
print(grouped_df_count)
print("-" * 30 + " SOMA DOS PEDIDOS POR CLIENTES " + "-" * 30)
print(grouped_df_sum)
print("-" * 30 + " PEDIDOS MÁXIMOS POR CLIENTES " + "-" * 30)
print(grouped_df_max)
print("-" * 30 + " PEDIDOS MÍNIMOS POR CLIENTES " + "-" * 30)
print(grouped_df_min)
print("-" * 30 + " MÉDIA DE PEDIDOS POR CLIENTES " + "-" * 30)
print(grouped_df_mean)