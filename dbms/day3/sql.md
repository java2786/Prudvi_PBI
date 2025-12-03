# MySQL Students Table Guide  
  
## 1. Create Database  
```sql  
CREATE DATABASE school;  
USE school;  
```  
  
---  
  
## 2. Create Table - Students  
```sql  
CREATE TABLE Students(  
	name VARCHAR(30),  
	email VARCHAR(30) UNIQUE NOT NULL,  
	marks INT DEFAULT 50,  
	dob DATE,  
	class VARCHAR(4),  
	subject VARCHAR(10)  
);  
```  
  
---  
  
## 3. Insert Data - Valid and Invalid Cases  
```sql  
-- Invalid: Missing required field 'email'  
INSERT INTO Students VALUES('Ramesh', '8A', 78, '2017-07-15', 'Physics');  
  
-- Valid  
INSERT INTO Students VALUES('Ramesh', 'ramesh@gmail.com', 78, '2017-07-15', '8A', 'Physics');  
  
-- Partial column insert  
INSERT INTO Students(name, class, marks, dob, subject)   
VALUES('Ramesh', '8A', 78, '2017-07-15', 'Physics');  
  
INSERT INTO Students(name, marks, subject)   
VALUES('Mahesh', 71, 'Math');  
```  
  
---  
  
## 4. Alter Table - Add Column  
```sql  
ALTER TABLE Students ADD COLUMN email VARCHAR(30);  
```  
  
---  
  
## 5. Insert More Data  
```sql  
INSERT INTO Students(name, marks, email)   
VALUES('Mukesh Kumar', 93, 'mukesh@gmail.com');  
  
-- Violates UNIQUE constraint (same email)  
INSERT INTO Students(name, marks, email)   
VALUES('Mukesh Mittal', 82, 'mukesh@gmail.com');  
```  
  
---  
  
## 6. Re-create Table with More Constraints (14 Jun 2025)  
```sql  
CREATE TABLE Students(  
	name VARCHAR(30),  
	phone VARCHAR(20) UNIQUE NOT NULL,   
	email VARCHAR(30) UNIQUE NOT NULL,  
	marks INT DEFAULT 50,  
	dob DATE,  
	class VARCHAR(4),  
	subject VARCHAR(10),  
	roll INT PRIMARY KEY AUTO_INCREMENT  
);  
```  
  
---  
  
## 7. Drop Table  
```sql  
DROP TABLE Students;  
```  
  
---  
  
## 8. Describe Table  
```sql  
DESC Students;  
```  
  
---  
  
## 9. Insert with Specific Roll Numbers  
```sql  
INSERT INTO Students(roll, email, phone)   
VALUES(101, 'ramesh@gmail.com', '9879879876');  
  
INSERT INTO Students(roll, email, phone)   
VALUES(102, 'mukesh@gmail.com', '2879879876');  
  
INSERT INTO Students(roll, email, phone)   
VALUES(1001, 'dinesh@gmail.com', '9839879876');  
  
-- Bulk Insert  
INSERT INTO Students(roll, email, phone) VALUES  
(1003,'rajesh@gmail.com', '1839879876'),  
(1004,'ramesh@gmail.com', '9239879876'),  
(1005,'kamlesh@gmail.com', '9833879876'),  
(1006,'ganesh@gmail.com', '9839849876'),  
(1007,'gukesh@gmail.com', '9839879576');  
  
-- Auto Increment behavior test  
INSERT INTO Students(roll, email, phone)   
VALUES(100, 'ram@gmail.com', '983987987');  
  
INSERT INTO Students(roll, email, phone)   
VALUES(101, 'shyam@gmail.com', '9983987987');  
```  
  
---  
  
## 10. Auto-increment Behavior Test  
```sql  
-- Insert without roll, check what auto ID it picks  
INSERT INTO Students(email, phone)   
VALUES('ramesh@gmail.com', '2839879876');  
```  
  
---  
  
## 11. Create Table - With Subject Breakdown  
```sql  
CREATE TABLE Students(  
	roll INT PRIMARY KEY AUTO_INCREMENT,  
	name VARCHAR(30),  
	marks INT,  
	subject1 VARCHAR(10),  
	subject2 VARCHAR(10),  
	subject3 VARCHAR(10)  
);  
```  
  
---  
  
## 12. Insert Multi-subject Data  
```sql  
INSERT INTO Students(name, subject1, subject2)   
VALUES('Ramesh', 'Math', 'English');  
  
INSERT INTO Students(name, subject1, subject2, subject3)   
VALUES('Rajesh', 'Physics', 'Math', 'English');  
```  
  
---  
  
## 🔍 Query Categories Summary  
  
**DDL (Data Definition Language):**  
```sql  
CREATE TABLE, ALTER TABLE, DROP TABLE, DESC  
```  
  
**DML (Data Manipulation Language):**  
```sql  
INSERT INTO, UPDATE, DELETE  
```  
  
**DQL (Data Query Language):**  
```sql  
SELECT * FROM Students;  
SELECT name, marks FROM Students;  
```  
  
