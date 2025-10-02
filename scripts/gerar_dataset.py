import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Criar pasta data/ se não existir (no mesmo nível do script ou projeto)
os.makedirs("data", exist_ok=True)

# Lista de produtos (igual antes)
produtos = [
    ("Notebook Dell", "Eletrônicos"),
    ("Smartphone Samsung", "Eletrônicos"),
    ("Fone de Ouvido JBL", "Acessórios"),
    ("Cadeira Gamer", "Móveis"),
    ("Teclado Mecânico", "Acessórios"),
    ("Mouse Logitech", "Acessórios"),
    ("Monitor LG", "Eletrônicos"),
    ("Copo Térmico", "Utilidades"),
    ("Livro Python", "Livros"),
    ("Tênis Nike", "Vestuário"),
]

# Função para gerar datas aleatórias
def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

# Período definido
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Criando registros
dados = []
for i in range(1, 101):
    produto, categoria = random.choice(produtos)
    quantidade = random.randint(1, 5)
    preco_unitario = round(random.uniform(30, 5000), 2)
    data = random_date(start_date, end_date)
    
    dados.append({
        "ID": i,
        "Data": data.strftime("%Y-%m-%d"),
        "Produto": produto,
        "Categoria": categoria,
        "Quantidade": quantidade,
        "Preço": preco_unitario
    })

# Criando DataFrame
df = pd.DataFrame(dados)

# Salvar CSV na pasta data/ no mesmo nível do script
df.to_csv("data/data_raw.csv", index=False, encoding="utf-8")

print("Dataset gerado e salvo como data/data_raw.csv")
