CREATE DATABASE ecommerce_tracker;
USE ecommerce_tracker;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(500)
);

CREATE TABLE platforms (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,
    platform_name VARCHAR(100)
);

CREATE TABLE price_tracking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    platform_id INT,
    price DECIMAL(10,2),
    rating DECIMAL(3,2),
    review_count INT,
    date_scraped DATETIME,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (platform_id) REFERENCES platforms(platform_id)
);