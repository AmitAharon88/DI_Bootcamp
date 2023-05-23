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

-- ***** Exercise XP Gold *****

-- ** Part 1
-- Create a table named purchases. It should have 3 columns :
-- id : the primary key of the table
-- customer_id : this column references the table customers
-- item_id : this column references the table items
-- quantity_purchased : this column is the quantity of items purchased by a certain customer

-- CREATE TABLE purchases (
-- 	id serial primary key,
-- 	customer_id INTEGER REFERENCES customers (customer_id),
-- 	item_id INTEGER REFERENCES items (item_id),
-- 	quantity_purchased integer
-- )
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES ((SELECT customer_id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'), (SELECT item_id FROM items WHERE item_name = 'fan'), 1)
-- select * from purchases

-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES ((SELECT customer_id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'), (SELECT item_id FROM items WHERE item_name = 'large desk'), 1)

-- select * from purchases

-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES ((SELECT customer_id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'), (SELECT item_id FROM items WHERE item_name = 'small desk'), 1)

-- select * from purchases


-- ** Part 2
-- select * from items

-- SELECT * FROM items where item_id = 5
-- select * from items
-- select * from items where item_name = 'Large Desk'  OR item_name = 'Small Desk'

-- select customers.first_name, customers.last_name, items.item_name
-- from customers
-- inner join items
-- on customer.customer_id = items.customer_id

-- select * from purchases

-- update purchases set item_id = 3 WHERE customer_id = 3
-- update purchases set item_id = 2 WHERE customer_id = 5
-- update purchases set item_id = 1 WHERE customer_id = 1

-- select * from purchases

-- select customers.first_name, customers.last_name, items.item_name
-- from purchases
-- join customers on customers.customer_id = purchases.customer_id
-- join items on items.item_id = purchases.item_id

-- No becuase item id is maditory

                 
