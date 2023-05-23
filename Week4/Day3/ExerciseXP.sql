-- ***** Exercise 1 *****

-- 1.
-- SELECT film.title, language.name
-- FROM film
-- INNER JOIN language
-- ON film.language_id = language.language_id

-- 2.1 
-- SELECT film.title, film.description, language.name
-- FROM film
-- LEFT JOIN language
-- ON film.language_id = language.language_id

-- 2.2
-- SELECT film.title, film.description, language.name
-- FROM film
-- RIGHT JOIN language
-- ON film.language_id = language.language_id

-- 3.
-- CREATE TABLE new_film(
-- 	film_id serial PRIMARY KEY,
-- 	name VARCHAR(50)
-- )

-- INSERT INTO new_film(name)
-- VALUES ('Harry Potter and the Sorcerers Stone'), ('Harry Potter and the Chamber of Secrets'), ('Harry Potter and the Prisoner of Azkaban')

-- drop table if exists customer_review
-- 4.
-- CREATE TABLE customer_review(
-- 	review_id SERIAL primary key NOT NULL,
-- 	film_id integer references new_film(film_id) ON DELETE CASCADE NOT NULL,
-- 	language_id integer references language(language_id) ON DELETE CASCADE NOT NULL,
-- 	title VARCHAR(30),
-- 	score integer,
-- 	review_text TEXT,
-- 	last_update TIMESTAMP
-- )


-- 5.
-- insert into customer_review(film_id, language_id, title, score, review_text)
-- values(1, 1, 'Loved it', 10, 'This movie had everything. Exciting, drama, comedy'), (2, 1, 'I was on the edge of my seat', 9, 'Everything I was waiting for but a bit long')

-- 6.
-- DELETE FROM new_film WHERE film_id = 1
-- select * from customer_review

-- ** The whole entry gets deleted



-- ***** Exercise 2 *****

-- 1.
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
-- UPDATE film
-- SET language_id = 3
-- WHERE film_id = 1;

-- UPDATE film
-- SET language_id = 2
-- WHERE film_id = 2;

-- UPDATE film
-- SET language_id = 5
-- WHERE film_id = 3

-- select * from film where film_id in (1, 2, 3)

-- 2.
-- The foreign key in the customer table are address_id
-- The primary key is customer_id which is refernced in the rental and payment tables.

-- 3.
-- DROP TABLE IF EXISTS customer_review
-- ** Was easy to drop

-- 4.
-- SELECT count(*) AS outstanding_rentals
-- FROM rental
-- WHERE return_date is NULL

-- 5.
-- SELECT title, amount
-- FROM film
-- INNER JOIN inventory
-- ON film.film_id = inventory.film_id
-- INNER JOIN rental
-- ON inventory.inventory_id = rental.inventory_id
-- INNER JOIN payment
-- ON rental.rental_id = payment.rental_id
-- WHERE return_date is NULL
-- ORDER BY payment.amount DESC
-- limit 30

-- 6.1
-- SELECT film.title
-- FROM film
-- INNER JOIN film_actor
-- ON film.film_id = film_actor.film_id
-- INNER JOIN actor
-- ON actor.actor_id = film_actor.actor_id
-- WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe' AND film.description ILIKE '%sumo wrestler%'

-- 6.2
-- SELECT film.title
-- FROM film
-- INNER JOIN film_category
-- ON film.film_id = film_category.film_id
-- INNER JOIN category
-- ON film_category.category_id = category.category_id
-- WHERE film.length < 60 AND film.rating = 'R' AND category.name = 'Documentary'

-- 6.3
-- SELECT film.title
-- from film
-- INNER JOIN inventory
-- ON film.film_id = inventory.film_id
-- INNER JOIN rental
-- ON inventory.inventory_id = rental.inventory_id
-- INNER JOIN payment
-- ON payment.rental_id = rental.rental_id
-- INNER JOIN customer
-- ON payment.customer_id = customer.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND payment.amount > 4 AND (rental.return_date BETWEEN '2005-07-28' And '2005-08-01')

-- 6.4
-- SELECT film.title
-- from film
-- INNER JOIN inventory
-- ON film.film_id = inventory.film_id
-- INNER JOIN rental
-- ON inventory.inventory_id = rental.inventory_id
-- INNER JOIN payment
-- ON payment.rental_id = rental.rental_id
-- INNER JOIN customer
-- ON payment.customer_id = customer.customer_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
-- ORDER BY payment.amount DESC LIMIT 1


