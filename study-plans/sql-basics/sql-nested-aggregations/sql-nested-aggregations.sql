-- Write your SQL query here
WITH daily_totals AS (
    SELECT
    order_date, 
    COUNT(*) AS daily_count,
    SUM(amount) AS daily_revenue
    FROM orders
    GROUP BY order_date
)

SELECT 
    AVG(daily_count) AS avg_daily_orders,
    AVG(daily_revenue) AS avg_daily_revenue,
    MAX(daily_count) AS busiest_day_orders
FROM daily_totals;
    