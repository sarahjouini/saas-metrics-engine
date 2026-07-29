SELECT
    plan_tier,
    COUNT(*) AS numero_abbonamenti,
    SUM(mrr_amount) AS mrr_totale
FROM abbonamenti
GROUP BY plan_tier
ORDER BY mrr_totale DESC;