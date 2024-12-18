-- Create a database named Tech4Girls_DB
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;

-- Use the created database
USE Tech4Girls_DB;

-- Create a table Users with columns to store information about users
CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,         
    username VARCHAR(50) NOT NULL,                     
    email VARCHAR(100) NOT NULL,                        
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- Insert sample data into Users table
INSERT INTO Users (username, email, created_at)
VALUES
    ('Ama', 'ama@example.com', '2024-11-01 10:30:00'),
    ('Abena', 'abena@example.com', '2024-11-02 12:00:00'),
    ('Adjoa', 'adjoa@example.com', '2024-11-03 14:15:00');

-- Show the content of the table Users
SELECT * FROM Users;
