import sqlite3
import pandas as pd
import os


df = pd.read_csv(os.path.join("..", "data", "data_clean.csv"))

conn = sqlite3.connect("vendas.db")

df.to_sql("vendas", conn, if_exists="replace", index=False)

print("Banco criado e dados inseridos com sucesso!")
