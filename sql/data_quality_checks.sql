-- ============================================================
-- Checagens de qualidade dos dados (tabela readings)
-- ============================================================

-- 1) Valores faltantes (nulos): COUNT(*) - COUNT(coluna) = nº de nulos
SELECT
    COUNT(*)                                AS total_linhas,
    COUNT(*) - COUNT("Air temperature [K]") AS nulos_air_temp,
    COUNT(*) - COUNT("Torque [Nm]")         AS nulos_torque,
    COUNT(*) - COUNT("Tool wear [min]")     AS nulos_tool_wear,
    COUNT(*) - COUNT("Machine failure")     AS nulos_alvo
FROM readings;

-- 2) Faixas plausíveis - Identificar valores exorbitantes
SELECT
    MIN("Air temperature [K]")    AS min_air,    MAX("Air temperature [K]")    AS max_air,
    MIN("Rotational speed [rpm]") AS min_rpm,    MAX("Rotational speed [rpm]") AS max_rpm,
    MIN("Torque [Nm]")            AS min_torque, MAX("Torque [Nm]")            AS max_torque,
    MIN("Tool wear [min]")        AS min_wear,   MAX("Tool wear [min]")        AS max_wear
FROM readings;

-- 3) Duplicatas de Product ID 

SELECT "Product ID", COUNT(*) AS vezes
FROM readings
GROUP BY "Product ID"
HAVING COUNT(*) > 1;