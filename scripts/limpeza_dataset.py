import pandas as pd
import os

# Criar pasta data/ se não existir (mesmo nível do script)
os.makedirs("data", exist_ok=True)

# 1. Carregar dataset cru
df = pd.read_csv("data/data_raw.csv")

# 2. Tratamento de valores faltantes
print("Valores faltantes antes:\n", df.isnull().sum())
df = df.dropna()  # ou df.fillna(...)

# 3. Remoção de duplicatas
print("Duplicatas antes:", df.duplicated().sum())
df = df.drop_duplicates()

# 4. Conversão de tipos de dados
df["Data"] = pd.to_datetime(df["Data"], format="%Y-%m-%d")
df["Quantidade"] = df["Quantidade"].astype(int)
df["Preço"] = df["Preço"].astype(float)

# 5. Salvar dataset limpo
df.to_csv("data/data_clean.csv", index=False, encoding="utf-8")

print("Dataset limpo salvo como data/data_clean.csv")
