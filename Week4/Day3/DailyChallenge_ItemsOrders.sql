-- CREATE TABLE product_orders(
-- 	order_id SERIAL PRIMARY KEY,
-- 	order_date TIMESTAMP,
-- 	customer_id INTEGER REFERENCES users(customer_id)
-- )

-- CREATE TABLE items(
-- 	item_name VARCHAR(30),
-- 	order_id integer REFERENCES product_orders(order_id),
-- 	price integer NOT NULL
-- )

-- INSERT INTO product_orders(order_date, customer_id)
-- VALUES ('2023-01-01', 1), ('2023-02-02', 2), ('2023-03-03', 3)

-- INSERT INTO items(item_name, order_id, price)
-- VALUES ('chair', 1, 15), ('table', 3, 40), ('desk',1, 3)

-- SELECT product_orders.order_id,  SUM(items.price) AS total_price
-- FROM product_orders
-- INNER JOIN items
-- ON product_orders.order_id = items.order_id
-- GROUP BY product_orders.order_id HAVING product_orders.order_id = 1


-- ***** BONUS *****

-- CREATE TABLE users(
-- 	customer_id SERIAL PRIMARY KEY NOT NULL,
-- 	customer_name VARCHAR(30)
-- );

-- INSERT INTO users(customer_name)
-- VALUES ('Sara'), ('Michal'), ('Zohar'), ('Eva')

-- SELECT users.customer_name,  SUM(items.price) AS total_price
-- FROM product_orders
-- INNER JOIN items
-- ON product_orders.order_id = items.order_id
-- INNER JOIN users
-- ON product_orders.customer_id = users.customer_id
-- GROUP BY product_orders.order_id, users.customer_id