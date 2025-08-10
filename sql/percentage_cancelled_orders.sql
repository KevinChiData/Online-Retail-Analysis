WITH order_stats AS (
    SELECT
        COUNT(*) AS TotalOrders,
        COUNT(CASE WHEN InvoiceNo LIKE 'C%' THEN 1 END) AS CancelledOrders
    FROM dirty_data
)

SELECT
    TotalOrders,
    CancelledOrders,
    ROUND(100.0 * CancelledOrders / TotalOrders, 2) AS CancelledPercentage
FROM order_stats