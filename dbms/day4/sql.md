# MySQL Practice Guide - Students & Customers  
  
---  
  
## 🟢 DATABASE SETUP  
```sql  
CREATE DATABASE practice_db;  
USE practice_db;  
```  
  
---  
  
## 🟩 TABLE: Students (Initial Version)  
### Data Dictionary (DD)  
- name: VARCHAR(30)  
- email: VARCHAR(30) UNIQUE NOT NULL  
- marks: INT DEFAULT 50  
- dob: DATE  
- class: VARCHAR(4)  
- subject: VARCHAR(10)  
  
### DDL - Table Structure  
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
  
## 🟨 DML - Insert Data  
```sql  
-- ❌ Invalid (missing email)  
INSERT INTO Students VALUES('Ramesh', '8A', 78, '2017-07-15', 'Physics');  
  
-- ✅ Valid  
INSERT INTO Students VALUES('Ramesh', 'ramesh@gmail.com', 78, '2017-07-15', '8A', 'Physics');  
  
-- ✅ Partial column insert  
INSERT INTO Students(name, class, marks, dob, subject)   
VALUES('Ramesh', '8A', 78, '2017-07-15', 'Physics');  
  
INSERT INTO Students(name, marks, subject)   
VALUES('Mahesh', 71, 'Math');  
```  
  
---  
  
## 🛠 ALTER TABLE  
```sql  
ALTER TABLE Students ADD COLUMN email VARCHAR(30);  
```  
  
```sql  
INSERT INTO Students(name, marks, email)   
VALUES('Mukesh Kumar', 93, 'mukesh@gmail.com');  
  
-- ❌ Duplicate email  
INSERT INTO Students(name, marks, email)   
VALUES('Mukesh Mittal', 82, 'mukesh@gmail.com');  
```  
  
---  
  
## 🔁 TABLE: Students (14 Jun 2025) — Recreated with Constraints  
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
  
## 🧨 Drop / Describe  
```sql  
DROP TABLE Students;  
DESC Students;  
```  
  
---  
  
## 📝 Insert with Manual Roll  
```sql  
INSERT INTO Students(roll, email, phone)   
VALUES(101, 'ramesh@gmail.com', '9879879876');  
  
INSERT INTO Students(roll, email, phone)   
VALUES(102, 'mukesh@gmail.com', '2879879876');  
  
INSERT INTO Students(roll, email, phone)   
VALUES(1001, 'dinesh@gmail.com', '9839879876');  
  
-- Bulk  
INSERT INTO Students(roll, email, phone) VALUES  
(1003,'rajesh@gmail.com', '1839879876'),  
(1004,'ramesh@gmail.com', '9239879876'),  
(1005,'kamlesh@gmail.com', '9833879876'),  
(1006,'ganesh@gmail.com', '9839849876'),  
(1007,'gukesh@gmail.com', '9839879576');  
```  
  
---  
  
## ❓ Auto-Increment ID Test  
```sql  
-- Manually assign lower roll number (allowed)  
INSERT INTO Students(roll, email, phone)   
VALUES(100, 'ram@gmail.com', '983987987');  
  
-- Try duplicate roll  
INSERT INTO Students(roll, email, phone)   
VALUES(101, 'shyam@gmail.com', '9983987987');  
  
-- Auto ID test  
INSERT INTO Students(email, phone)   
VALUES('ramesh@gmail.com', '2839879876');  
```  
  
---  
  
## 🆕 Create Subject-Wise Table  
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
  
```sql  
INSERT INTO Students(name, subject1, subject2)   
VALUES('Ramesh', 'Math', 'English');  
  
INSERT INTO Students(name, subject1, subject2, subject3)   
VALUES('Rajesh', 'Physics', 'Math', 'English');  
```  
  
---  
  
## 🔷 TABLE: Customers & Orders (16 Jun 2025)  
```sql  
DROP TABLE IF EXISTS Customers;  
DROP TABLE IF EXISTS Orders;  
  
CREATE TABLE Customers(  
	id INT PRIMARY KEY AUTO_INCREMENT,  
	name VARCHAR(20),  
	city VARCHAR(20)  
);  
  
CREATE TABLE Orders(  
	customerId INT,  
	product_name VARCHAR(20),  
	quantity INT,  
	FOREIGN KEY(customerId) REFERENCES Customers(id)  
);  
```  
  
---  
  
## 🟨 Insert Customer & Orders  
```sql  
INSERT INTO Customers(name, city)   
VALUES('Ramesh', 'pune');  
  
INSERT INTO Orders(customerId, product_name, quantity)   
VALUES(123, 'mobile', 2);  
```  
  
---  
  
## 🔍 DQL Queries - Search  
```sql  
-- Customers from Pune  
SELECT * FROM Customers WHERE city = 'pune';  
SELECT name FROM Customers WHERE city = 'pune';  
  
-- Nested Query: Customer who purchased shirt  
SELECT name FROM Customers   
WHERE id IN (  
    SELECT customerId FROM Orders   
    WHERE product_name = 'shirt'  
);  
```  
  
---  
  
## 🔁 CRUD Examples  
```sql  
-- Read  
SELECT * FROM Customers;  
  
-- Update  
UPDATE Customers   
SET city = 'delhi'   
WHERE name = 'Mukesh';  
```  
  
---  
  
## 🔑 CATEGORY: SQL COMMANDS SUMMARY  
  
**DDL (Data Definition Language):**  
- CREATE, ALTER, DROP, DESC  
  
**DML (Data Manipulation Language):**  
- INSERT, UPDATE, DELETE  
  
**DQL (Data Query Language):**  
- SELECT  
  
**KEY REAL-WORLD ACTIONS:**  
- Create table for students  
- Enforce unique/primary constraints  
- Insert valid/invalid records  
- Use auto_increment for ID generation  
- Perform nested queries and subqueries  
  
