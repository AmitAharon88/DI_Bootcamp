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

-- ***** Exercise 1 *****
-- 1.
-- SELECT rating, COUNT(*) FROM film GROUP BY rating

-- 2. 
-- SELECT title, rating From film WHERE rating = 'G' OR rating = 'PG-13'
-- SELECT * From film WHERE (rating = 'G' OR rating = 'PG-13') AND length < 120 AND rental_rate < 3 ORDER BY title ASC

-- 3.
-- UPDATE customer SET first_name = 'Amit', last_name = 'Aharon' Where customer_id = 1
-- SELECT * FROM customer WHERE first_name = 'Amit'

-- 4. 
-- UPDATE address SET address = '123 Season st. NY, NY 13456' Where address_id = 5
-- SELECT * FROM address WHERE address_id = 5