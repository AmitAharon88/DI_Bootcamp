-- Database: Public

-- DROP DATABASE IF EXISTS "Public";

-- CREATE DATABASE "Public"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- Week4 Day 1
-- Exercise XP
-- Exercise 1 : Items And Customers

-- CREATE TABLE items (
-- 	item_id SERIAL PRIMARY KEY,
-- 	item_name VARCHAR(100) NOT NULL,
-- 	price SMALLINT NOT NULL
-- )

-- CREATE TABLE customers (
-- 	customer_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(100) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL
-- )

-- INSERT INTO items (item_name, price)
-- VALUES
-- ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80)

-- INSERT INTO customers (first_name, last_name)
-- VALUES
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trever', 'Green'),
-- ('Melanie', 'Johnson')

-- SELECT * FROM items
-- SELECT * FROM items WHERE price>80
-- SELECT * FROM items WHERE price<=300
-- SELECT * FROM customers WHERE last_name = 'Smith'
-- (Outcome is nothing as there is no customers with the name Smith)
-- SELECT * FROM customers WHERE last_name = 'Jones'
-- SELECT * FROM customers WHERE first_name != 'Scott'

-- Week4 Day 2
-- Exercise XP
-- Exercise 1 : Items And Customers

-- SELECT * FROM ITEMS ORDER BY price ASC
-- SELECT * FROM ITEMS WHERE price >= 80 ORDER BY price DESC
-- SELECT first_name, last_name FROM customers ORDER BY first_name ASC LIMIT 3
-- SELECT last_name FROM customers ORDER BY last_name DESC
