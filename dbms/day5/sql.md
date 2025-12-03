# MySQL Practice Workbook – Students, Subjects, Scores, Customers, Orders  
  
---  
  
## 📁 DATABASE SETUP  
```sql  
CREATE DATABASE fullstack_sql_lab;  
USE fullstack_sql_lab;  
```  
  
---  
  
## 👨‍🎓 TABLE: Students (Basic Info)  
```sql  
CREATE TABLE Students(  
	roll INT PRIMARY KEY AUTO_INCREMENT,  
	name VARCHAR(20)  
);  
```  
  
### Insert Student Records  
```sql  
INSERT INTO Students(name)   
VALUES('Ramesh'), ('Mahesh'), ('Suresh'), ('Mukesh');  
```  
  
---  
  
## 📚 TABLE: Subjects  
```sql  
CREATE TABLE Subjects(  
	id INT PRIMARY KEY AUTO_INCREMENT,  
	name VARCHAR(20)  
);  
```  
  
### Insert Subjects  
```sql  
INSERT INTO Subjects(name)   
VALUES('Hindi'), ('Math');  
```  
  
---  
  
## 🧾 TABLE: Scores  
```sql  
DROP TABLE IF EXISTS Scores;  
  
CREATE TABLE Scores(  
	marks INT,  
	student_id INT,  
	sub_id INT,  
	FOREIGN KEY(student_id) REFERENCES Students(roll),  
	FOREIGN KEY(sub_id) REFERENCES Subjects(id),  
	PRIMARY KEY(student_id, sub_id)  
);  
```  
  
### Insert Score Records (Valid)  
```sql  
INSERT INTO Scores(marks, student_id, sub_id) VALUES  
(78, 3, 1),  
(88, 2, 2),  
(99, 4, 1),  
(91, 4, 1),   -- Will fail: duplicate primary key  
(92, 4, 2);   -- Valid new subject  
```  
  
---  
  
## 📄 STUDENTS TABLE (With Email/Phone/Subject/Marks)  
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
  
### Insert with Manual Roll  
```sql  
INSERT INTO Students(roll, email, phone) VALUES(101, 'ramesh@gmail.com', '9879879876');  
INSERT INTO Students(roll, email, phone) VALUES(102, 'mukesh@gmail.com', '2879879876');  
INSERT INTO Students(roll, email, phone) VALUES(1001, 'dinesh@gmail.com', '9839879876');  
```  
  
### Bulk Insert  
```sql  
INSERT INTO Students(roll, email, phone) VALUES  
(1003,'rajesh@gmail.com', '1839879876'),  
(1004,'ramesh@gmail.com', '9239879876'),  
(1005,'kamlesh@gmail.com', '9833879876'),  
(1006,'ganesh@gmail.com', '9839849876'),  
(1007,'gukesh@gmail.com', '9839879576');  
```  
  
### Auto-Increment Example  
```sql  
-- Test new roll number generation  
INSERT INTO Students(email, phone)   
VALUES('ramesh@gmail.com', '2839879876');  
```  
  
---  
  
## 👥 TABLES: Customers and Orders (16 Jun 2025)  
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
  
### Insert Data  
```sql  
INSERT INTO Customers(name, city) VALUES('Ramesh', 'pune');  
INSERT INTO Orders(customerId, product_name, quantity)   
VALUES(123, 'mobile', 2);  
```  
  
---  
  
## 🔍 DQL: Queries and Joins  
  
### Customers from Pune  
```sql  
SELECT * FROM Customers WHERE city = 'pune';  
SELECT name FROM Customers WHERE city = 'pune';  
```  
  
### Customers who bought 'shirt'  
```sql  
SELECT name FROM Customers   
WHERE id IN (  
	SELECT customerId FROM Orders   
	WHERE product_name = 'shirt'  
);  
```  
  
### Customer by Specific IDs  
```sql  
SELECT name FROM Customers WHERE id = 1;  
SELECT name FROM Customers WHERE id IN (1,2);  
```  
  
---  
  
## 🧱 SQL CATEGORIES SUMMARY  
  
### 🟦 DDL – Define Structure  
```sql  
CREATE TABLE, ALTER TABLE, DROP TABLE, DESC  
```  
  
### 🟨 DML – Modify Data  
```sql  
INSERT INTO, UPDATE, DELETE FROM  
```  
  
### 🟩 DQL – Query Data  
```sql  
SELECT * FROM table_name;  
```  
  
### CRUD Example  
```sql  
-- Read  
SELECT * FROM Customers;  
  
-- Update  
UPDATE Customers   
SET city = 'delhi'   
WHERE name = 'Mukesh';  
```  
  
