-- Average price
SELECT AVG(price) AS avg_price
FROM price_tracking;

-- Top rated products
SELECT p.product_name, pt.rating
FROM price_tracking pt
JOIN products p ON pt.product_id = p.product_id
ORDER BY pt.rating DESC
LIMIT 10;

-- Price distribution
SELECT 
    CASE 
        WHEN price < 30000 THEN 'Low'
        WHEN price BETWEEN 30000 AND 60000 THEN 'Mid'
        WHEN price BETWEEN 60000 AND 100000 THEN 'High'
        ELSE 'Premium'
    END AS price_category,
    COUNT(*) AS total_products
FROM price_tracking
GROUP BY price_category;