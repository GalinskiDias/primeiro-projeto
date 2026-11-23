import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tabela.csv')
df = df.fillna(0)

df['Faturamento'] = df['Preco'] * df['Quantidade']
df.to_excel('relatorio_vendas.xlsx', index=False)
print("-> Planilha'relatorio_venda.xlsx' gerada com sucesso!")

faturamento_vendedor = df.groupby('Vendedor')['Faturamento'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
faturamento_vendedor.plot(kind='bar', color='royalblue')

plt.title('Faturamento Total por vendedor', fontsize=14)
plt.xlabel('Vendedor', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig('Grafico_faturamento.png', dpi=150)
print("Imagem 'grafico_faturamento.png' salva com sucesso")