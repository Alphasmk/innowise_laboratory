-- 1. Create tables
-- Create the students table to store student information
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each student
    full_name TEXT, -- Full name of the student
    birth_year INTEGER -- Year of birth
);

-- Create the grades table to store student grades
CREATE TABLE grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each grade record
    student_id INTEGER, -- Foreign key referencing students table
    subject TEXT, -- Subject name
    grade INTEGER CHECK (grade >= 1 AND grade <= 100), -- Grade value between 1 and 100
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Create an index on full_name to optimize queries filtering by student name
CREATE INDEX student_idx ON students(full_name);

-- 2. Insert data
-- Begin transaction to ensure data consistency
BEGIN TRANSACTION;

-- Insert student records
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henri Lopez', 2004),
('Isabella Martinez', 2006);

-- Insert grade records for each student
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);

-- Commit transaction to save changes
COMMIT;

-- 3. Find grades for a specific student
-- Create a view joining students and grades
CREATE VIEW students_grades AS
SELECT a.full_name, b.subject, b.grade
FROM students a
INNER JOIN grades b
ON a.id = b.student_id;

-- Query to retrieve Alice Johnson's grades
SELECT subject, grade FROM students_grades WHERE full_name = "Alice Johnson";

-- 4. Calculate the average grade per student
-- Create a view with average grades for each student
CREATE VIEW avg_grades AS
SELECT a.full_name, avg(b.grade) as avg_grade
FROM students a
INNER JOIN grades b
ON a.id = b.student_id
GROUP BY a.full_name;

-- Display all students with their average grades
SELECT * FROM avg_grades;

-- 5. List all students born after 2004
SELECT full_name, birth_year FROM students WHERE birth_year > 2004;

-- 6. Create a query that lists all subjects and their average grades
SELECT subject, avg(grade)
FROM grades
GROUP BY subject;

-- 7. Find the top 3 students with the highest average grades
SELECT * FROM avg_grades
ORDER BY avg_grade DESC
LIMIT 3;

-- 8. Show all students who have scored below 80 in any subject
SELECT full_name FROM students_grades
WHERE grade < 80
GROUP BY full_name;