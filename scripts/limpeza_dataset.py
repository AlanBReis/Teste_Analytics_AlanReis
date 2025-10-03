import pandas as pd
import os

os.makedirs("data", exist_ok=True)

df = pd.read_csv("data/data_raw.csv")

print("Valores faltantes antes:\n", df.isnull().sum())
df = df.dropna() 

print("Duplicatas antes:", df.duplicated().sum())
df = df.drop_duplicates()

df["Data"] = pd.to_datetime(df["Data"], format="%Y-%m-%d")
df["Quantidade"] = df["Quantidade"].astype(int)
df["Preço"] = df["Preço"].astype(float)

df.to_csv("data/data_clean.csv", index=False, encoding="utf-8")

print("Dataset limpo salvo como data/data_clean.csv")
