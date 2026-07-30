import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("saas.db")

# ===== GRAFICO 1: MRR per piano =====
with open("sql/mrr_per_piano.sql") as f:
    query1 = f.read()
dati1 = pd.read_sql(query1, conn)

plt.figure(figsize=(8, 5))
plt.bar(dati1["plan_tier"], dati1["mrr_totale"], color="steelblue")
plt.title("MRR totale per piano")
plt.xlabel("Piano")
plt.ylabel("MRR totale (€)")
plt.tight_layout()
plt.savefig("mrr_per_piano.png")

# ===== GRAFICO 2: numero abbonamenti per piano =====
with open("sql/abbonamenti_per_piano.sql") as f:
    query2 = f.read()
dati2 = pd.read_sql(query2, conn)

plt.figure(figsize=(8, 5))
plt.bar(dati2["plan_tier"], dati2["numero_abbonamenti"], color="coral")
plt.title("Numero di abbonamenti per piano")
plt.xlabel("Piano")
plt.ylabel("Numero abbonamenti")
plt.tight_layout()
plt.savefig("abbonamenti_per_piano.png")

conn.close()
print("Fatti tutti e due i grafici!")