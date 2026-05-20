-- Write your SQL query here
SELECT name, city, COALESCE(SUM(amount), 0) AS total_spent
    FROM customers LEFT JOIN orders 
    ON customers.id = orders.customer_id
    GROUP BY customers.id, name, city
    ORDER BY total_spent DESC, name ASC;