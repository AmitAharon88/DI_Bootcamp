-- Database: Bootcamp

-- DROP DATABASE IF EXISTS "Bootcamp";

-- CREATE DATABASE "Bootcamp"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE students(
-- 	id SERIAL PRIMARY KEY,
-- 	last_name VARCHAR(100) NOT NULL,
-- 	first_name VARCHAR(100) NOT NULL,
-- 	birth_date DATE NOT NULL
-- )

-- Set datestyle to DMY

-- INSERT INTO students(last_name, first_name, birth_date)
-- Values
-- ('Benichou', 'Marc', '02/11/1998'),
-- ('Cohen', 'Yoan', '03/12/2010'),
-- ('Benichou', 'Lea', '27/07/1987'),
-- ('Dux', 'Amelia', '07/04/1996'),
-- ('Grez', 'David', '14/06/2003'),
-- ('Simpson', 'Omer', '03/10/1980')

-- SELECT * FROM students
-- SELECT first_name, last_name FROM students
-- SELECT * FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc'
-- SELECT * FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc'
-- SELECT * FROM students WHERE first_name ILIKE '%A%'
-- SELECT * FROM students WHERE first_name ILIKE 'A%'
-- SELECT * FROM students WHERE first_name ILIKE '%A'
-- SELECT * FROM students WHERE first_name LIKE '%a_'
-- SELECT * FROM students WHERE id IN (1, 3)
-- SELECT * FROM students Where birth_date >= '2000-01-01'

-- SELECT first_name, last_name, TO_CHAR(birth_date, 'DD/MM/YYYY') AS birth_date FROM students
-- (Changed the date but not perminatly)

-- ***** ExerciseXP Gold *****
-- SELECT * FROM students ORDER BY last_name ASC limit 4
-- SELECT * FROM students ORDER BY birth_date DESC LIMIT 1
-- SELECT * FROM students ORDER BY id OFFSET 2 LIMIT 3