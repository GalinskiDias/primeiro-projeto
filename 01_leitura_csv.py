import pandas as pd

df = pd.read_csv('exercicio_vendas.csv')
print("--- Primeiras linhas (head)---")
print(df.head())

df['Faturamento'] = df['Preco'] * df['Quantidade']

vendas_altas = df[df['Faturamento']> 500]
print("\n--- Vendas Acima de R$ 500,00 ---")
print(vendas_altas[['Vendedor','Produto', 'Faturamento']])

resumo_regiao = df.groupby('Regiao')['Faturamento'].sum()
print("\n--- Faturamento Total por Regiao ---")
print(resumo_regiao)