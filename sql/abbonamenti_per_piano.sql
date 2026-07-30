SELECT
    plan_tier,
    COUNT(*) AS numero_abbonamenti
FROM abbonamenti
GROUP BY plan_tier;