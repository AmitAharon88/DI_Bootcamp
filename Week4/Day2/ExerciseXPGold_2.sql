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

-- ***** Exercise XP Gold *****

-- ** UPDATE

-- UPDATE students
-- SET birth_date = '02/11/1998'
-- WHERE last_name = 'Benichou'

-- select * from students

-- UPDATE students
-- SET last_name = 'Guez'
-- WHERE last_name = 'Grez'

-- select * from students


-- ** DELETE
-- delete from students where first_name = 'Lea'

-- select * from students


-- ** COUNT
-- select count(*) from students

-- select count (*) from students where birth_date > '2000-01-01'


-- ** INSERT/ALTER
-- alter table students add column math_grade smallint
-- update students set math_grade = 80 WHERE id = 1
-- update students set math_grade = 90 WHERE id = 2 OR id = 4
-- update students set math_grade = 40 WHERE id = 6
-- select count(*) from students where math_grade > 83
-- insert into students(last_name, first_name,birth_date, math_grade) values('Simpson', 'Omer', '2003-06-14', 70)
-- select * from students
-- CAN't FIGURE OUT
-- select first_name, last_name, math_grade count(*)
-- from students
-- group by math_grade

-- ** SUM
-- select sum(math_grade) from students
