import pandas as pd

df = pd.read_csv('tabela.csv')
df = df.fillna(0)

df['Faturamento'] = df['Preco'] * df['Quantidade']

filtro_sul_alto = df[(df['Regiao'] == 'Sul') & (df['Faturamento'] > 500)]
print("--- Vendas no Sul e Com Faturamento Alto ---")
print(filtro_sul_alto[['Data', 'Vendedor', 'Produto', 'Faturamento', 'Regiao']])

filtro_telas = df[(df['Produto'] == 'Notebook') | (df['Produto']== 'Monitor')]
print("--- Vendas de Notebook ou Monitor ---")
print(filtro_telas[['Vendedor', 'Produto', 'Faturamento']])