import pandas as pd
import sqlite3

with open("sql/churn.sql") as f:
    query = f.read()

conn = sqlite3.connect("saas.db")
risultato = pd.read_sql(query, conn)
conn.close()

print(risultato)