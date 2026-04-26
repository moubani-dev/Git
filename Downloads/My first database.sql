CREATE DATABASE my_first_db;

USE my_first_db;

CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
);

INSERT INTO students (id, name, age, course)
VALUES 
(101, 'Sahil', 24, 'MSC'),
(102, 'Moubani', 21, 'Diploma'),
(103, 'Ankita', 20, 'Diploma'),
(104, 'ribani', 22, 'BSC');

SELECT * FROM students;

UPDATE students
SET age = '21'
WHERE id = 101;

DELETE FROM students
WHERE id = 104;