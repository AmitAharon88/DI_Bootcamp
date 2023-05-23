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
-- 	review_id SERIAL NOT NULL,
-- 	film_id integer NOT NULL,
-- 	language_id integer NOT NULL,
-- 	title VARCHAR(30),
-- 	score integer,
-- 	review_text TEXT,
-- 	last_update TIMESTAMP,
-- 	primary key (review_id),
-- 	foreign KEY (film_id) references new_film(film_id) ON DELETE CASCADE,
-- 	foreign KEY (language_id) references language(language_id) ON DELETE CASCADE
-- )


-- 5.
-- insert into customer_review(title, score, review_text)
-- values('Loved it', 10, 'This movie had everything. Exciting, drama, comedy'), ('I was on the edge of my seat', 9, 'Everything I was waiting for but a bit long')

-- select * from customer_review



