import pandas as pd

df = pd.read_csv('exercicio_vendas.csv')

print("--- Quantidade de Nulos por Coluna ---")
print(df.isna().sum())

df_preenchido = df.fillna(0)
print("\n--- Linhas Preenchidas com Zero ---")
print(df_preenchido.tail(3))