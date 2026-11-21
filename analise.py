import pandas as pd

dados = {
  'Vendedor': ['Ana', 'Bruno', 'Carlos', 'Ana', 'Bruno'],
  'Vendas': [100, 250, 150, 300, 200],
  'Regiao': ['Sul', 'Norte', 'Sul', 'Sul', 'Norte']
}

df = pd.DataFrame(dados)

print("--- Tabela Completa ---")
print(df)

print("\n--- Total de Vendas por Vendedor ---")
total_vendedor = df.groupby('Vendedor')['Vendas'].sum()
print(total_vendedor)