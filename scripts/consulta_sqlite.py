import sqlite3
import pandas as pd

# Conecta ao banco de dados SQLite que você criou
conn = sqlite3.connect("vendas.db")

# --- Consulta 1: Top Produtos ---
query_1 = """
SELECT
    Produto,
    Categoria,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM
    vendas  -- O nome da sua tabela no SQLite é 'vendas'
GROUP BY
    Produto,
    Categoria
ORDER BY
    Total_Vendas DESC;
"""

resultado_1 = pd.read_sql(query_1, conn)

print("======================================================")
print("Resultado da Consulta 1 (Vendas Totais por Produto):")
print("======================================================")
print(resultado_1)


# --- Consulta 2: Produto Menos Vendido (Jun/2024) ---
query_2 = """
SELECT
    Produto,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM
    vendas
WHERE
    Data BETWEEN '2024-06-01' AND '2024-06-30'
GROUP BY
    Produto
ORDER BY
    Total_Vendas ASC
LIMIT 1;
"""

resultado_2 = pd.read_sql(query_2, conn)

print("\n======================================================")
print("Resultado da Consulta 2 (Produto que Menos Vendeu em Jun/2024):")
print("======================================================")
print(resultado_2)

# Fechar a conexão
conn.close()