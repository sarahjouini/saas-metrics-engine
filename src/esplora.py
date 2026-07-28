import pandas as pd

df = pd.read_csv("data/ravenstack_subscriptions.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())

df["start_date"] = pd.to_datetime(df["start_date"])
df["end_date"] = pd.to_datetime(df["end_date"])
print(df.dtypes)