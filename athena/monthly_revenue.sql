-- Update database/table names to match your Glue Catalog.
SELECT date_trunc('month', order_date) AS order_month,
       COUNT(*) AS order_count,
       SUM(amount) AS revenue
FROM curated_orders
WHERE amount >= 0
GROUP BY 1
ORDER BY 1;
