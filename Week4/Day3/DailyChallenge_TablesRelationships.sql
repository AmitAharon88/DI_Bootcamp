-- ***** Part 1 *****

-- 1.
-- CREATE TABLE customer(
-- 	id serial NOT NULL primary key,
-- 	first_name VARCHAR(30),
-- 	last_name VARCHAR(30) NOT NULL
-- );

-- CREATE TABLE customer_profile(
-- 	id serial NOT NULL primary key,
-- 	isLoggedIn boolean DEFAULT FALSE,
-- 	customer_id INTEGER UNIQUE REFERENCES customer (id)
-- );

-- 2.
-- INSERT INTO customer(first_name, last_name)
-- VALUES('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive')

-- 3.
-- INSERT INTO customer_profile(isLoggedIn, customer_id)
-- VALUES(TRUE, 1), (FALSE, 2)

-- 4.1
-- SELECT first_name
-- FROM customer
-- INNER JOIN customer_profile
-- ON customer.id = customer_profile.customer_id
-- where customer_profile.isLoggedIn = TRUE

-- 4.2
-- SELECT customer.first_name, customer_profile.isLoggedIn
-- FROM customer
-- INNER JOIN customer_profile
-- ON customer.id = customer_profile.customer_id

-- 4.3
-- SELECT COUNT(*)
-- FROM customer
-- INNER JOIN customer_profile
-- ON customer.id = customer_profile.customer_id
-- where customer_profile.isLoggedIn = FALSE


-- ***** Part 2 *****

-- 1.
-- CREATE TABLE book(
-- 	book_id SERIAL PRIMARY KEY,
-- 	title VARCHAR(30) NOT NULL,
-- 	author VARCHAR(30) NOT NULL
-- )

-- 2.
-- INSERT INTO book(title, author)
-- VALUES ('Alice In Wonderland', 'Lewis Carroll'), ('Harry Potter', 'J.K Rowling'), ('To kill a mockingbird', 'Harper Lee')

-- 3.
-- CREATE TABLE student(
-- 	student_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(30) NOT NULL UNIQUE,
-- 	age INTEGER CHECK (age <= 15)
-- )

-- 4.
-- INSERT INTO student(name, age)
-- VALUES ('John', 12), ('Lera', 11), ('Patrick', 10), ('Bob', 14)

-- 5.
-- CREATE TABLE library(
-- 	book_fk_id INTEGER REFERENCES book (book_id),
-- 	student_id INTEGER REFERENCES student (student_id),
-- 	borrowed_date TIMESTAMP
-- )

-- 6.
-- INSERT INTO library(book_fk_id, student_id, borrowed_date)
-- VALUES ((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
-- 		(SELECT student_id FROM student WHERE name = 'John'),
--         '2022-02-15');

-- INSERT INTO library(book_fk_id, student_id, borrowed_date)
-- VALUES ((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
-- 		(SELECT student_id FROM student WHERE name = 'Bob'),
--         '2022-03-03');

-- INSERT INTO library(book_fk_id, student_id, borrowed_date)
-- VALUES ((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
-- 		(SELECT student_id FROM student WHERE name = 'Lera'),
--         '2021-05-23');
		
-- INSERT INTO library(book_fk_id, student_id, borrowed_date)
-- VALUES ((SELECT book_id FROM book WHERE title = 'Harry Potter'),
-- 		(SELECT student_id FROM student WHERE name = 'Bob'),
--         '2021-08-12');

-- 7.1
-- select * from library

-- 7.2
-- select student.name, book.title
-- From student
-- Inner Join library ON student.student_id = library.student_id
-- Inner Join book ON book.book_id = library.book_fk_id

-- 7.3
-- select avg(age) AS average_age
-- from student
-- inner join library on student.student_id = library.student_id
-- inner join book on book.book_id = library.book_fk_id
-- where book.title = 'Alice In Wonderland'

-- 7.4
-- DELETE FROM student WHERE name = 'Bob'
-- ** it wont delete because they still refernce from the library table and a ON DELETE CASCADE was not provided when making the library table.