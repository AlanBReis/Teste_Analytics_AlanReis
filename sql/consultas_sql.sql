-- Soma total de vendas por produto e categoria
SELECT Produto, Categoria, SUM(Quantidade * Preço) AS Total_Vendas
FROM data_clean
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;

-- Produto que menos vendeu em junho de 2024
SELECT Produto, SUM(Quantidade * Preço) AS Total_Vendas
FROM data_clean
WHERE Data BETWEEN '2024-06-01' AND '2024-06-30'
GROUP BY Produto
ORDER BY Total_Vendas ASC
LIMIT 1;
