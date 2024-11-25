-- Use the existing database
USE Tech4Girls_DB;

-- Create the Posts table to store information about user posts
CREATE TABLE IF NOT EXISTS Posts (
    id INT AUTO_INCREMENT PRIMARY KEY,        
    user_id INT NOT NULL,                      
    title VARCHAR(255) NOT NULL,                
    content TEXT NOT NULL,                     
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE 
);

-- Insert sample posts into the Posts table to establish the one-to-many relationship 
INSERT INTO Posts (user_id, title, content, created_at)
VALUES
    (1, 'Ama’s First Post', 'This is Ama’s first post content.', '2024-11-24 11:00:00'),
    (1, 'Ama’s Second Post', 'This is Ama’s second post content.', '2024-11-25 12:30:00'),
    (2, 'Abena’s First Post', 'This is Abena’s first post content.', '2024-11-25 13:00:00'),
    (3, 'Adjoa’s First Post', 'This is Adjoa’s first post content.', '2024-11-25 15:00:00');

-- Displaying the records in the Posts table to ensure the posts were added
SELECT * FROM Posts;
