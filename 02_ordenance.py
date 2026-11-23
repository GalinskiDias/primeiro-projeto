import pandas as pd

df = pd.read_csv('exercicio_vendas.csv')

df['Faturamento'] = df['Preco'] * df['Quantidade']

df_ordenado = df.sort_values(by='Faturamento', ascending=False)

print("--- Vendas Ordenadas pelo Faturamento (maior --> Menor) ---")
print(df_ordenado[['Vendedor', 'Produto', 'Faturamento']])

total_vendedor = df.groupby('Vendedor')['Faturamento'].sum().sort_values(ascending=False)

print("\n--- Faturamento Total por Vendedor (classificado) ---")
print(total_vendedor)