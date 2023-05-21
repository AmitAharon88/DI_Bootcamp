-- Database: dvdrental

-- DROP DATABASE IF EXISTS dvdrental;

-- CREATE DATABASE dvdrental
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- ***** EXERCISE XP *****
-- *****  EXERCISE 2 *****

-- SELECT * FROM customer
-- SELECT first_name || ' ' || last_name AS full_name FROM customer
-- SELECT DISTINCT create_date FROM customer
-- SELECT * From customer ORDER BY first_name DESC
-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC
-- SELECT address, phone FROM address WHERE district = 'Texas'
-- SELECT * FROM film WHERE film_id IN (15,150)
-- SELECT film_id, title, description, rental_duration, rental_rate FROM film WHERE title ILIKE 'Harry Potter'
-- SELECT film_id, title, description, rental_duration, rental_rate FROM film WHERE title ILIKE 'Ha%'
-- Select * FROM film ORDER BY rental_rate ASC LIMIT 10
-- Select * FROM film ORDER BY rental_rate ASC LIMIT 10  OFFSET 10

-- SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
-- FROM customer
-- INNER JOIN payment
-- ON customer.customer_id = payment.customer_id ORDER BY customer.customer_id ASC

-- SELECT film_id, title
-- FROM film
-- WHERE film_id NOT IN (
--   SELECT film_id
--   FROM inventory
-- )

-- SELECT city.city, country.country
-- FROM city
-- INNER JOIN country
-- ON city.country_id = country.country_id

-- *** Bonus
-- SELECT customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date, staff.staff_id
-- FROM customer
-- Join payment on customer.customer_id = payment.customer_id
-- Join staff on payment.staff_id = staff.staff_id
-- ORDER BY staff.staff_id ASC