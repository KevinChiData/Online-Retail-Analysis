SELECT Description, ROUND(SUM(Revenue), 2) AS Revenue
FROM online_retail_sql
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 15