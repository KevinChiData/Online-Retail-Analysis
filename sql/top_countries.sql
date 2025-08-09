SELECT Country, ROUND(SUM(Revenue), 2) AS TotalRevenue
FROM online_retail_sql
GROUP BY Country
ORDER BY TotalRevenue DESC