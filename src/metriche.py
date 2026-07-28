import pandas as pd

df = pd.read_csv("data/ravenstack_subscriptions.csv")

# Quanti abbonamenti hanno abbandonato (churn)
churn_totali = df["churn_flag"].sum()
print("Abbonamenti in churn:", churn_totali)

# Su quanti abbonamenti in totale
totali = len(df)
print("Abbonamenti totali:", totali)

# Il tasso di churn in percentuale
churn_rate = churn_totali / totali * 100
print("Churn rate:", churn_rate, "%")
# Churn rate per piano
churn_per_piano = df.groupby("plan_tier")["churn_flag"].mean() * 100
print(churn_per_piano)
# Churn rate per auto-renew (rinnovo automatico sì/no)
churn_per_autorenew = df.groupby("auto_renew_flag")["churn_flag"].mean() * 100
print(churn_per_autorenew)
# MRR medio: chi abbandona vs chi resta
mrr_per_churn = df.groupby("churn_flag")["mrr_amount"].mean()
print(mrr_per_churn)
# MRR totale (tutti gli abbonamenti)
mrr_totale = df["mrr_amount"].sum()
print("MRR totale (tutti):", mrr_totale)

# MRR degli abbonamenti ATTIVI (churn_flag = False)
attivi = df[df["churn_flag"] == False]
mrr_attivo = attivi["mrr_amount"].sum()
print("MRR attivo (solo attivi):", mrr_attivo)
# ARR totale degli abbonamenti attivi
arr_attivo = attivi["arr_amount"].sum()
print("ARR attivo:", arr_attivo)

# Verifica: ARR dovrebbe essere circa MRR x 12
print("MRR attivo x 12:", mrr_attivo * 12)
# MRR totale per piano (solo attivi)
mrr_per_piano = attivi.groupby("plan_tier")["mrr_amount"].sum()
print("MRR per piano:")
print(mrr_per_piano)

# Quanti clienti attivi per piano
clienti_per_piano = attivi.groupby("plan_tier")["subscription_id"].count()
print("Clienti attivi per piano:")
print(clienti_per_piano)
# Quanti abbonamenti vengono da trial
print("Distribuzione trial:")
print(df["is_trial"].value_counts())

# Churn rate: trial vs non-trial
churn_trial = df.groupby("is_trial")["churn_flag"].mean() * 100
print("Churn per trial:")
print(churn_trial)