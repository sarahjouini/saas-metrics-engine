import pandas as pd
import sqlite3

conn = sqlite3.connect("saas.db")

nomi_tabelle = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
print("Tabelle nel database:")
print(nomi_tabelle)
print()

anteprima = pd.read_sql("SELECT * FROM abbonamenti LIMIT 5", conn)
print("Prime 5 righe della tabella abbonamenti:")
print(anteprima)

conn.close()