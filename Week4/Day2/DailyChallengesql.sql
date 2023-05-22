-- Database: W4D2_DC

-- DROP DATABASE IF EXISTS "W4D2_DC";

-- CREATE DATABASE "W4D2_DC"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;


-- ***** DAILY CHALLENGE *****
--   *** Queries ***

-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- );

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- );

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL);

-- SELECT * FROM SecondTab


-- Q1. What will be the OUTPUT of the following statement?

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft
-- WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- ** Assumption- 3 (Output- 0)
-- It will count the number of rows in the "FirstTab" table where the corresponding "id" values are not NULL in the "SecondTab" table.



-- Q2. What will be the OUTPUT of the following statement?

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft
-- WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- ** Assumption- 3 (Output- 2)
-- It will count the number of rows in the "FirstTab" table where the corresponding "id" values are not equal to 5 in the "SecondTab" table.



-- Q3. What will be the OUTPUT of the following statement?

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft
-- WHERE ft.id NOT IN (SELECT id FROM SecondTab)

-- ** Assumption- 2 (Output- 0)
-- It will count the number of rows in the "FirstTab" table where the corresponding "id" values are not found in the "SecondTab" table.



-- Q4. What will be the OUTPUT of the following statement?

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft
-- WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NOT NULL)

-- ** Assumption- 2 (Output- 2)
-- It will the number of rows in the "FirstTab" table where the corresponding "id" values are not found or are NULL in the "SecondTab" table.