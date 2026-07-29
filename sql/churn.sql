SELECT
    churn_flag,
    COUNT(*) AS numero_abbonamenti
FROM abbonamenti
GROUP BY churn_flag;