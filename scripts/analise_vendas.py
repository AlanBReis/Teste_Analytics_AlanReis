import pandas as pd

# Ler dataset limpo
df = pd.read_csv("../data/data_clean.csv")

# Criar coluna de total de vendas
df["Total_Vendas"] = df["Quantidade"] * df["Preço"]

# Total de vendas por produto
total_vendas_produto = df.groupby("Produto")["Total_Vendas"].sum().reset_index()
print("Total de vendas por produto:\n", total_vendas_produto)

# Produto mais vendido
produto_mais_vendido = total_vendas_produto.sort_values(by="Total_Vendas", ascending=False).iloc[0]
print("\nProduto mais vendido:", produto_mais_vendido["Produto"])
print("Total de vendas:", produto_mais_vendido["Total_Vendas"])

# Opcional: salvar em CSV na pasta data/
total_vendas_produto.to_csv("../data/total_vendas_produto.csv", index=False)
