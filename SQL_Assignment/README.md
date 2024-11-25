# SQL_Assignment

This directory contains SQL scripts that demonstrates key database concepts like creating databases, defining relationships between tables, and inserting sample data. The scripts are organized as follows:

## 1. question1.sql - Setting Up and Populating a Database

### Concepts Covered:
- **Creating a Database**: The script demonstrates how to create a new database Tech4Girls_DB.
- **Table Creation**: The Users table is created with columns for id, username, email, and   created_at. The id column uses the primary key and auto-increment.
- **Inserting Data**: Inserts sample users into the Users table.

### Key SQL Commands:
 - CREATE DATABASE
 - CREATE TABLE
 - INSERT INTO
 - VALUES
 - SELECT 

## 2. question2.sql - Building Relationships

### Concepts Covered:
 - **Foreign Keys and Relationships**: This script demonstrates how to create a Posts table with a foreign key that references the Users table, establishing a one-to-many relationship.
 - **Cascading Deletes**: Uses ON DELETE CASCADE to ensure posts are deleted if the associated user is deleted.
 - **Inserting Data**: Sample posts are inserted for each user.

### Key SQL Commands:
-  CREATE TABLE with FOREIGN KEY
-  INSERT INTO
- VALUES
- SELECT

## 3. question3.sql - Creating Many-to-Many Relationships

### Concepts Covered:
- **Many-to-Many Relationship**: This script demonstrates how to create a many-to-many relationship between Users and Courses using an intermediate table User_Courses.
- **Intermediate Table**: The User_Courses table stores mappings of user enrollments in courses. It uses a composite primary key to ensure uniqueness.
- **Foreign Keys**: Foreign key constraints are applied to both user_id and course_id for references.
- **Inserting Data**: Sample courses are inserted into the Courses table, and sample enrollments are inserted into the User_Courses table.

### Key SQL Commands:
- CREATE TABLE with FOREIGN KEY
- PRIMARY KEY 
- INSERT INTO
- VALUES
- SELECT 

### Conclusion:
These scripts showcase how create databases, tables and how to handle one-to-many and many-to-many relationships in SQL. The examples demonstrate fundamental database concepts such as creating tables, defining foreign key constraints, and using intermediate tables to link data across tables.
