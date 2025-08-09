SELECT STRFTIME('%Y-%M', InvoiceDate) AS YearMonth,
    ROUND(SUM(Quantity), 2) AS TotalQuantity,
    ROUND(SUM(Revenue), 2) AS TotalRevenue
FROM online_retail_sql
GROUP BY YearMonth
ORDER BY YearMonth