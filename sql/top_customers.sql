SELECT CustomerID, ROUND(SUM(Revenue), 2) AS TotalSpendings
FROM online_retail_sql
GROUP BY CustomerID
ORDER BY TotalSpendings DESC
LIMIT 15