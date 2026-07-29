import pandas as pd
import sqlite3
import glob

file_csv = glob.glob("data/*.csv")[0]
df = pd.read_csv(file_csv)

conn = sqlite3.connect("saas.db")
df.to_sql("abbonamenti", conn, if_exists="replace", index=False)
conn.close()

print("Database creato! Tabella 'abbonamenti' pronta.")