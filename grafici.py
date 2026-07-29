import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

with open("sql/mrr_per_piano.sql") as f:
    query = f.read()

conn = sqlite3.connect("saas.db")
dati = pd.read_sql(query, conn)
conn.close()

print(dati)
plt.figure(figsize=(8, 5))
plt.bar(dati["plan_tier"], dati["mrr_totale"], color="steelblue")
plt.title("MRR totale per piano")
plt.xlabel("Piano")
plt.ylabel("MRR totale (€)")
plt.tight_layout()
plt.savefig("mrr_per_piano.png")
print("Grafico salvato come mrr_per_piano.png")