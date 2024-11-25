-- Use the existing database
USE Tech4Girls_DB;

-- Create the Courses table that stores information about available courses.
CREATE TABLE IF NOT EXISTS Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,         
    course_name VARCHAR(100) NOT NULL           
);

-- Create the User_Courses intermediate table that links users and courses to establish a many-to-many relationship.
CREATE TABLE IF NOT EXISTS User_Courses (
    user_id INT NOT NULL,                       
    course_id INT NOT NULL,                     
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,  
    FOREIGN KEY (course_id) REFERENCES Courses(id) ON DELETE CASCADE,  
    PRIMARY KEY (user_id, course_id)            
);

-- Insert sample courses into the Courses table
INSERT INTO Courses (course_name)
VALUES
    ('Backend Development Basics'),
    ('Bash,Bash Scripting and OOP'),
    ('DataBases with SQL');

-- Enroll users in courses using the User_Courses table
-- Each user can be enrolled in multiple courses and each course can have multiple users. Establishing many-to-many relationship
INSERT INTO User_Courses (user_id, course_id)
VALUES
    (1, 1),  -- Ama enrolls in Backend Development Basics
    (1, 2),  -- Ama enrolls in Bash,Bash Scripting and OOP
    (2, 2),  -- Abena enrolls in Bash,Bash Scripting and OOP
    (2, 3),  -- Abena enrolls in DataBases with SQL
    (3, 1),  -- Adjoa enrolls in Backend Development Basics
    (3, 3);  -- Adjoa enrolls in DataBases with SQL

-- This displays all the records from the User_Courses table to see and check enrollments.
SELECT * FROM User_Courses;
