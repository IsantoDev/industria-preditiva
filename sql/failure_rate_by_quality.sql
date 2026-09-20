-- Taxa de falha por nível de qualidade da máquina 
SELECT
    m.quality_level,
    COUNT(*)                                              AS total_leituras,
    SUM(r."Machine failure")                              AS falhas,
    ROUND(100.0 * SUM(r."Machine failure") / COUNT(*), 2) AS taxa_falha_pct
FROM readings AS r
JOIN machines AS m ON r.Type = m.Type
GROUP BY m.quality_level
ORDER BY taxa_falha_pct DESC;