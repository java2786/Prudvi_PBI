# SQL JOINS - Complete Guide  
## Easy Theory + Practice Questions + Solutions  
  
**For MySQL Database**  
  
---  
  
## What are JOINS?  
  
**Simple Definition:**  
JOINs are used to combine rows from two or more tables based on a related column.  
  
**Real-Life Analogy:**  
Think of two registers in school:  
- **Register 1:** Student names and roll numbers  
- **Register 2:** Roll numbers and marks  
  
To see "Student Name with their Marks", you need to JOIN both registers using Roll Number!  
  
---  
  
## Setup Database  
  
```sql  
-- Create Database  
CREATE DATABASE joins_practice;  
USE joins_practice;  
  
-- Create Students Table  
CREATE TABLE STUDENTS (  
    RollNo INT PRIMARY KEY,  
    Name VARCHAR(50),  
    Class VARCHAR(5)  
);  
  
-- Create Marks Table  
CREATE TABLE MARKS (  
    RollNo INT,  
    Subject VARCHAR(30),  
    Marks INT  
);  
  
-- Insert Students  
INSERT INTO STUDENTS VALUES  
(101, 'Suresh Kumar', '12A'),  
(102, 'Ramesh Patel', '12B'),  
(103, 'Mahesh Singh', '12A'),  
(104, 'Dinesh Reddy', '12C'),  
(105, 'Mukesh Jain', '12B');  
  
-- Insert Marks  
INSERT INTO MARKS VALUES  
(101, 'Math', 85),  
(101, 'Science', 90),  
(102, 'Math', 78),  
(103, 'Math', 92),  
(103, 'Science', 88),  
(106, 'Math', 75);  -- Note: RollNo 106 doesn't exist in STUDENTS!  
```  
  
**Visual Representation:**  
  
```  
STUDENTS Table:  
+--------+---------------+-------+  
| RollNo | Name          | Class |  
+--------+---------------+-------+  
| 101    | Suresh Kumar  | 12A   |  
| 102    | Ramesh Patel  | 12B   |  
| 103    | Mahesh Singh  | 12A   |  
| 104    | Dinesh Reddy  | 12C   |  
| 105    | Mukesh Jain   | 12B   |  
+--------+---------------+-------+  
  
MARKS Table:  
+--------+----------+-------+  
| RollNo | Subject  | Marks |  
+--------+----------+-------+  
| 101    | Math     | 85    |  
| 101    | Science  | 90    |  
| 102    | Math     | 78    |  
| 103    | Math     | 92    |  
| 103    | Science  | 88    |  
| 106    | Math     | 75    |  ← No student with RollNo 106!  
+--------+----------+-------+  
```  
  
**Notice:**  
- Student 104 (Dinesh) and 105 (Mukesh) have NO marks  
- Mark entry for RollNo 106 has NO student  
  
This is perfect for understanding different JOIN types!  
  
---  
  
## Types of JOINS  
  
```  
Visual Summary:  
  
Table A              Table B  
   ●●●●●            ●●●●●  
   ●●●●●            ●●●●●  
   ●●●●●  ←JOIN→    ●●●●●  
   ●●●●●            ●●●●●  
```  
  
### 1. INNER JOIN  
### 2. LEFT JOIN (LEFT OUTER JOIN)  
### 3. RIGHT JOIN (RIGHT OUTER JOIN)  
### 4. CROSS JOIN (CARTESIAN PRODUCT)  
  
Let's understand each one!  
  
---  
  
## 1. INNER JOIN (Most Common!)  
  
### Theory  
  
**Simple Explanation:**  
Returns only matching records from both tables.  
  
**Think:** "Show me only students who have marks"  
  
**Syntax:**  
```sql  
SELECT columns  
FROM table1  
INNER JOIN table2  
ON table1.column = table2.column;  
```  
  
**Alternative Syntax (Comma):**  
```sql  
SELECT columns  
FROM table1, table2  
WHERE table1.column = table2.column;  
```  
  
### Visual Explanation  
  
```  
STUDENTS               MARKS  
   101 ────────────── 101  ✓ Match!  
   102 ────────────── 102  ✓ Match!  
   103 ────────────── 103  ✓ Match!  
   104                     ✗ No marks  
   105                     ✗ No marks  
                      106  ✗ No student  
  
INNER JOIN returns: 101, 102, 103 (only matches)  
```  
  
### Example Query  
  
```sql  
-- Show student names with their marks  
SELECT STUDENTS.Name, MARKS.Subject, MARKS.Marks  
FROM STUDENTS  
INNER JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo;  
```  
  
### Output  
  
```  
+---------------+----------+-------+  
| Name          | Subject  | Marks |  
+---------------+----------+-------+  
| Suresh Kumar  | Math     | 85    |  
| Suresh Kumar  | Science  | 90    |  
| Ramesh Patel  | Math     | 78    |  
| Mahesh Singh  | Math     | 92    |  
| Mahesh Singh  | Science  | 88    |  
+---------------+----------+-------+  
```  
  
**Notice:**  
- Only 3 students shown (101, 102, 103)  
- Dinesh (104) and Mukesh (105) NOT shown (no marks)  
- RollNo 106 marks NOT shown (no student)  
  
---  
  
## 2. LEFT JOIN (LEFT OUTER JOIN)  
  
### Theory  
  
**Simple Explanation:**  
Returns ALL records from LEFT table + matching records from RIGHT table.  
If no match, shows NULL for right table columns.  
  
**Think:** "Show me ALL students, even if they don't have marks"  
  
**Syntax:**  
```sql  
SELECT columns  
FROM table1  
LEFT JOIN table2  
ON table1.column = table2.column;  
```  
  
### Visual Explanation  
  
```  
STUDENTS (LEFT)        MARKS (RIGHT)  
   101 ────────────── 101  ✓ Match  
   102 ────────────── 102  ✓ Match  
   103 ────────────── 103  ✓ Match  
   104 ────────────── NULL ← No match, but student shown  
   105 ────────────── NULL ← No match, but student shown  
                      106  ✗ Not shown (not in left table)  
  
LEFT JOIN returns: All students (101-105), marks where available  
```  
  
### Example Query  
  
```sql  
-- Show ALL students with their marks (if any)  
SELECT STUDENTS.Name, MARKS.Subject, MARKS.Marks  
FROM STUDENTS  
LEFT JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo;  
```  
  
### Output  
  
```  
+---------------+----------+-------+  
| Name          | Subject  | Marks |  
+---------------+----------+-------+  
| Suresh Kumar  | Math     | 85    |  
| Suresh Kumar  | Science  | 90    |  
| Ramesh Patel  | Math     | 78    |  
| Mahesh Singh  | Math     | 92    |  
| Mahesh Singh  | Science  | 88    |  
| Dinesh Reddy  | NULL     | NULL  |  ← No marks  
| Mukesh Jain   | NULL     | NULL  |  ← No marks  
+---------------+----------+-------+  
```  
  
**Notice:**  
- ALL 5 students shown  
- Dinesh and Mukesh have NULL for Subject and Marks  
- RollNo 106 marks still NOT shown  
  
---  
  
## 3. RIGHT JOIN (RIGHT OUTER JOIN)  
  
### Theory  
  
**Simple Explanation:**  
Returns ALL records from RIGHT table + matching records from LEFT table.  
If no match, shows NULL for left table columns.  
  
**Think:** "Show me ALL marks entries, even if student doesn't exist"  
  
**Syntax:**  
```sql  
SELECT columns  
FROM table1  
RIGHT JOIN table2  
ON table1.column = table2.column;  
```  
  
### Visual Explanation  
  
```  
STUDENTS (LEFT)        MARKS (RIGHT)  
   101 ────────────── 101  ✓ Match  
   102 ────────────── 102  ✓ Match  
   103 ────────────── 103  ✓ Match  
   104 ✗ Not shown          
   105 ✗ Not shown          
      NULL ──────────── 106  ← No student, but marks shown  
  
RIGHT JOIN returns: All marks (101-103, 106), students where available  
```  
  
### Example Query  
  
```sql  
-- Show ALL marks entries with student names (if any)  
SELECT STUDENTS.Name, MARKS.Subject, MARKS.Marks  
FROM STUDENTS  
RIGHT JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo;  
```  
  
### Output  
  
```  
+---------------+----------+-------+  
| Name          | Subject  | Marks |  
+---------------+----------+-------+  
| Suresh Kumar  | Math     | 85    |  
| Suresh Kumar  | Science  | 90    |  
| Ramesh Patel  | Math     | 78    |  
| Mahesh Singh  | Math     | 92    |  
| Mahesh Singh  | Science  | 88    |  
| NULL          | Math     | 75    |  ← RollNo 106 (no student)  
+---------------+----------+-------+  
```  
  
**Notice:**  
- ALL 6 mark entries shown  
- RollNo 106 has NULL for Name (student doesn't exist)  
- Students 104 and 105 NOT shown (no marks)  
  
---  
  
## 4. CROSS JOIN (Cartesian Product)  
  
### Theory  
  
**Simple Explanation:**  
Returns ALL possible combinations of rows from both tables.  
Every row from Table1 paired with EVERY row from Table2.  
  
**Think:** "Match every student with every subject (all combinations)"  
  
**Formula:** Rows = Table1 rows × Table2 rows  
Example: 5 students × 6 marks = 30 rows!  
  
**Syntax:**  
```sql  
SELECT columns  
FROM table1  
CROSS JOIN table2;  
  
-- OR simply  
SELECT columns  
FROM table1, table2;  
```  
  
### Visual Explanation  
  
```  
STUDENTS (5 rows)    MARKS (6 rows)  
   101    ×    All 6 marks = 6 combinations  
   102    ×    All 6 marks = 6 combinations  
   103    ×    All 6 marks = 6 combinations  
   104    ×    All 6 marks = 6 combinations  
   105    ×    All 6 marks = 6 combinations  
  
Total = 5 × 6 = 30 rows!  
```  
  
### Example Query  
  
```sql  
-- Every student paired with every subject  
SELECT STUDENTS.Name, MARKS.Subject  
FROM STUDENTS  
CROSS JOIN MARKS;  
```  
  
### Output (First 10 rows shown)  
  
```  
+---------------+----------+  
| Name          | Subject  |  
+---------------+----------+  
| Suresh Kumar  | Math     |  
| Suresh Kumar  | Science  |  
| Suresh Kumar  | Math     |  
| Suresh Kumar  | Math     |  
| Suresh Kumar  | Science  |  
| Suresh Kumar  | Math     |  
| Ramesh Patel  | Math     |  
| Ramesh Patel  | Science  |  
| Ramesh Patel  | Math     |  
| Ramesh Patel  | Math     |  
... (30 total rows)  
+---------------+----------+  
```  
  
**Warning:** Rarely used! Creates huge result sets!  
  
---  
  
## Comparison of All JOINS  
  
```  
Data Recap:  
STUDENTS: 101, 102, 103, 104, 105 (5 students)  
MARKS:    101, 102, 103, 106 (6 entries)  
Match:    101, 102, 103  
```  
  
| JOIN Type | Records Returned | Shows |  
|-----------|-----------------|-------|  
| **INNER JOIN** | 5 rows | Only matches (101, 102, 103) |  
| **LEFT JOIN** | 7 rows | All students + their marks |  
| **RIGHT JOIN** | 6 rows | All marks + student names |  
| **CROSS JOIN** | 30 rows | All combinations |  
  
---  
  
## Real-World Example  
  
### Setup: Company Database  
  
```sql  
-- Employees Table  
CREATE TABLE EMPLOYEES (  
    EmpID INT PRIMARY KEY,  
    Name VARCHAR(50),  
    Department VARCHAR(30)  
);  
  
-- Salaries Table  
CREATE TABLE SALARIES (  
    EmpID INT,  
    Salary DECIMAL(10,2),  
    Month VARCHAR(10)  
);  
  
-- Insert Data  
INSERT INTO EMPLOYEES VALUES  
(1, 'Suresh', 'IT'),  
(2, 'Ramesh', 'HR'),  
(3, 'Mahesh', 'IT'),  
(4, 'Dinesh', 'Sales');  
  
INSERT INTO SALARIES VALUES  
(1, 45000, 'Jan'),  
(2, 38000, 'Jan'),  
(3, 50000, 'Jan'),  
(5, 35000, 'Jan');  -- EmpID 5 doesn't exist!  
```  
  
### Query 1: INNER JOIN - Show employees with their salaries  
  
```sql  
SELECT EMPLOYEES.Name, EMPLOYEES.Department, SALARIES.Salary  
FROM EMPLOYEES  
INNER JOIN SALARIES  
ON EMPLOYEES.EmpID = SALARIES.EmpID;  
```  
  
**Output:**  
```  
+---------+------------+--------+  
| Name    | Department | Salary |  
+---------+------------+--------+  
| Suresh  | IT         | 45000  |  
| Ramesh  | HR         | 38000  |  
| Mahesh  | IT         | 50000  |  
+---------+------------+--------+  
3 rows (Dinesh not shown - no salary)  
```  
  
### Query 2: LEFT JOIN - Show ALL employees, even without salary  
  
```sql  
SELECT EMPLOYEES.Name, EMPLOYEES.Department, SALARIES.Salary  
FROM EMPLOYEES  
LEFT JOIN SALARIES  
ON EMPLOYEES.EmpID = SALARIES.EmpID;  
```  
  
**Output:**  
```  
+---------+------------+--------+  
| Name    | Department | Salary |  
+---------+------------+--------+  
| Suresh  | IT         | 45000  |  
| Ramesh  | HR         | 38000  |  
| Mahesh  | IT         | 50000  |  
| Dinesh  | Sales      | NULL   |  ← No salary yet  
+---------+------------+--------+  
4 rows (All employees shown)  
```  
  
### Query 3: RIGHT JOIN - Show ALL salary entries, even invalid ones  
  
```sql  
SELECT EMPLOYEES.Name, EMPLOYEES.Department, SALARIES.Salary  
FROM EMPLOYEES  
RIGHT JOIN SALARIES  
ON EMPLOYEES.EmpID = SALARIES.EmpID;  
```  
  
**Output:**  
```  
+---------+------------+--------+  
| Name    | Department | Salary |  
+---------+------------+--------+  
| Suresh  | IT         | 45000  |  
| Ramesh  | HR         | 38000  |  
| Mahesh  | IT         | 50000  |  
| NULL    | NULL       | 35000  |  ← Invalid EmpID 5  
+---------+------------+--------+  
4 rows (All salary entries shown)  
```  
  
---  
  
## Practice Questions  
  
### Easy Level  
  
**Q1.** Write query using INNER JOIN to show student names with their marks.  
  
**Q2.** Write query using LEFT JOIN to show all students with their marks (show NULL if no marks).  
  
**Q3.** Write query to show only students who have NO marks. (Hint: Use LEFT JOIN with NULL check)  
  
---  
  
### Medium Level  
  
**Q4.** Write query to show students who scored more than 85 marks in any subject.  
  
**Q5.** Write query to count how many subjects each student has marks in.  
  
**Q6.** Write query to show which students are from class 12A and their marks.  
  
---  
  
### Hard Level  
  
**Q7.** Write query to show students with total marks > 160 (sum of all subjects).  
  
**Q8.** Write query to find students who took Math but not Science.  
  
**Q9.** Write query to show class-wise average marks.  
  
---  
  
## Solutions to Practice Questions  
  
### Solution 1  
```sql  
SELECT STUDENTS.Name, MARKS.Subject, MARKS.Marks  
FROM STUDENTS  
INNER JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo;  
```  
  
**Output:**  
```  
+---------------+----------+-------+  
| Name          | Subject  | Marks |  
+---------------+----------+-------+  
| Suresh Kumar  | Math     | 85    |  
| Suresh Kumar  | Science  | 90    |  
| Ramesh Patel  | Math     | 78    |  
| Mahesh Singh  | Math     | 92    |  
| Mahesh Singh  | Science  | 88    |  
+---------------+----------+-------+  
```  
  
---  
  
### Solution 2  
```sql  
SELECT STUDENTS.Name, MARKS.Subject, MARKS.Marks  
FROM STUDENTS  
LEFT JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo;  
```  
  
**Output:**  
```  
+---------------+----------+-------+  
| Name          | Subject  | Marks |  
+---------------+----------+-------+  
| Suresh Kumar  | Math     | 85    |  
| Suresh Kumar  | Science  | 90    |  
| Ramesh Patel  | Math     | 78    |  
| Mahesh Singh  | Math     | 92    |  
| Mahesh Singh  | Science  | 88    |  
| Dinesh Reddy  | NULL     | NULL  |  
| Mukesh Jain   | NULL     | NULL  |  
+---------------+----------+-------+  
```  
  
---  
  
### Solution 3  
```sql  
SELECT STUDENTS.Name, STUDENTS.Class  
FROM STUDENTS  
LEFT JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo  
WHERE MARKS.RollNo IS NULL;  
```  
  
**Output:**  
```  
+--------------+-------+  
| Name         | Class |  
+--------------+-------+  
| Dinesh Reddy | 12C   |  
| Mukesh Jain  | 12B   |  
+--------------+-------+  
```  
  
**Explanation:** LEFT JOIN shows all students, then WHERE filters only those with NULL in MARKS (meaning no marks).  
  
---  
  
### Solution 4  
```sql  
SELECT STUDENTS.Name, MARKS.Subject, MARKS.Marks  
FROM STUDENTS  
INNER JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo  
WHERE MARKS.Marks > 85;  
```  
  
**Output:**  
```  
+---------------+----------+-------+  
| Name          | Subject  | Marks |  
+---------------+----------+-------+  
| Suresh Kumar  | Science  | 90    |  
| Mahesh Singh  | Math     | 92    |  
| Mahesh Singh  | Science  | 88    |  
+---------------+----------+-------+  
```  
  
---  
  
### Solution 5  
```sql  
SELECT STUDENTS.Name, COUNT(*) AS SubjectCount  
FROM STUDENTS  
INNER JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo  
GROUP BY STUDENTS.Name;  
```  
  
**Output:**  
```  
+---------------+--------------+  
| Name          | SubjectCount |  
+---------------+--------------+  
| Suresh Kumar  | 2            |  
| Ramesh Patel  | 1            |  
| Mahesh Singh  | 2            |  
+---------------+--------------+  
```  
  
---  
  
### Solution 6  
```sql  
SELECT STUDENTS.Name, STUDENTS.Class, MARKS.Subject, MARKS.Marks  
FROM STUDENTS  
INNER JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo  
WHERE STUDENTS.Class = '12A';  
```  
  
**Output:**  
```  
+---------------+-------+----------+-------+  
| Name          | Class | Subject  | Marks |  
+---------------+-------+----------+-------+  
| Suresh Kumar  | 12A   | Math     | 85    |  
| Suresh Kumar  | 12A   | Science  | 90    |  
| Mahesh Singh  | 12A   | Math     | 92    |  
| Mahesh Singh  | 12A   | Science  | 88    |  
+---------------+-------+----------+-------+  
```  
  
---  
  
### Solution 7  
```sql  
SELECT STUDENTS.Name, SUM(MARKS.Marks) AS TotalMarks  
FROM STUDENTS  
INNER JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo  
GROUP BY STUDENTS.Name  
HAVING SUM(MARKS.Marks) > 160;  
```  
  
**Output:**  
```  
+---------------+------------+  
| Name          | TotalMarks |  
+---------------+------------+  
| Suresh Kumar  | 175        |  
| Mahesh Singh  | 180        |  
+---------------+------------+  
```  
  
**Explanation:**   
- Suresh: 85 + 90 = 175  
- Mahesh: 92 + 88 = 180  
  
---  
  
### Solution 8  
```sql  
SELECT STUDENTS.Name  
FROM STUDENTS  
INNER JOIN MARKS ON STUDENTS.RollNo = MARKS.RollNo  
WHERE MARKS.Subject = 'Math'  
AND STUDENTS.RollNo NOT IN (  
    SELECT RollNo FROM MARKS WHERE Subject = 'Science'  
);  
```  
  
**Output:**  
```  
+---------------+  
| Name          |  
+---------------+  
| Ramesh Patel  |  
+---------------+  
```  
  
**Explanation:** Ramesh took Math (78) but not Science.  
  
---  
  
### Solution 9  
```sql  
SELECT STUDENTS.Class, AVG(MARKS.Marks) AS AvgMarks  
FROM STUDENTS  
INNER JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo  
GROUP BY STUDENTS.Class;  
```  
  
**Output:**  
```  
+-------+----------+  
| Class | AvgMarks |  
+-------+----------+  
| 12A   | 88.75    |  
| 12B   | 78.00    |  
+-------+----------+  
```  
  
**Explanation:**  
- 12A: (85 + 90 + 92 + 88) / 4 = 88.75  
- 12B: 78 / 1 = 78.00  
  
---  
  
## More Practice: E-Commerce Database  
  
```sql  
-- Create Tables  
CREATE TABLE CUSTOMERS (  
    CustomerID INT PRIMARY KEY,  
    Name VARCHAR(50),  
    City VARCHAR(30)  
);  
  
CREATE TABLE ORDERS (  
    OrderID INT PRIMARY KEY,  
    CustomerID INT,  
    Product VARCHAR(50),  
    Amount DECIMAL(10,2)  
);  
  
-- Insert Data  
INSERT INTO CUSTOMERS VALUES  
(1, 'Suresh', 'Pune'),  
(2, 'Ramesh', 'Mumbai'),  
(3, 'Mahesh', 'Delhi'),  
(4, 'Dinesh', 'Bangalore');  
  
INSERT INTO ORDERS VALUES  
(101, 1, 'Laptop', 55000),  
(102, 1, 'Mouse', 500),  
(103, 2, 'Keyboard', 1500),  
(104, 5, 'Monitor', 12000);  -- CustomerID 5 doesn't exist!  
```  
  
### Practice Queries  
  
**Q10.** Show customer names with their orders (INNER JOIN)  
  
**Q11.** Show ALL customers, even those without orders (LEFT JOIN)  
  
**Q12.** Show customers who have NOT placed any order  
  
**Q13.** Show total amount spent by each customer  
  
**Q14.** Find customers who spent more than 10000  
  
---  
  
## Solutions to E-Commerce Queries  
  
### Solution 10  
```sql  
SELECT CUSTOMERS.Name, ORDERS.Product, ORDERS.Amount  
FROM CUSTOMERS  
INNER JOIN ORDERS  
ON CUSTOMERS.CustomerID = ORDERS.CustomerID;  
```  
  
**Output:**  
```  
+---------+----------+--------+  
| Name    | Product  | Amount |  
+---------+----------+--------+  
| Suresh  | Laptop   | 55000  |  
| Suresh  | Mouse    | 500    |  
| Ramesh  | Keyboard | 1500   |  
+---------+----------+--------+  
```  
  
---  
  
### Solution 11  
```sql  
SELECT CUSTOMERS.Name, ORDERS.Product, ORDERS.Amount  
FROM CUSTOMERS  
LEFT JOIN ORDERS  
ON CUSTOMERS.CustomerID = ORDERS.CustomerID;  
```  
  
**Output:**  
```  
+---------+----------+--------+  
| Name    | Product  | Amount |  
+---------+----------+--------+  
| Suresh  | Laptop   | 55000  |  
| Suresh  | Mouse    | 500    |  
| Ramesh  | Keyboard | 1500   |  
| Mahesh  | NULL     | NULL   |  
| Dinesh  | NULL     | NULL   |  
+---------+----------+--------+  
```  
  
---  
  
### Solution 12  
```sql  
SELECT CUSTOMERS.Name, CUSTOMERS.City  
FROM CUSTOMERS  
LEFT JOIN ORDERS  
ON CUSTOMERS.CustomerID = ORDERS.CustomerID  
WHERE ORDERS.OrderID IS NULL;  
```  
  
**Output:**  
```  
+---------+-----------+  
| Name    | City      |  
+---------+-----------+  
| Mahesh  | Delhi     |  
| Dinesh  | Bangalore |  
+---------+-----------+  
```  
  
---  
  
### Solution 13  
```sql  
SELECT CUSTOMERS.Name, SUM(ORDERS.Amount) AS TotalSpent  
FROM CUSTOMERS  
INNER JOIN ORDERS  
ON CUSTOMERS.CustomerID = ORDERS.CustomerID  
GROUP BY CUSTOMERS.Name;  
```  
  
**Output:**  
```  
+---------+------------+  
| Name    | TotalSpent |  
+---------+------------+  
| Suresh  | 55500      |  
| Ramesh  | 1500       |  
+---------+------------+  
```  
  
---  
  
### Solution 14  
```sql  
SELECT CUSTOMERS.Name, SUM(ORDERS.Amount) AS TotalSpent  
FROM CUSTOMERS  
INNER JOIN ORDERS  
ON CUSTOMERS.CustomerID = ORDERS.CustomerID  
GROUP BY CUSTOMERS.Name  
HAVING SUM(ORDERS.Amount) > 10000;  
```  
  
**Output:**  
```  
+---------+------------+  
| Name    | TotalSpent |  
+---------+------------+  
| Suresh  | 55500      |  
+---------+------------+  
```  
  
---  
  
## Quick Reference Card  
  
### When to Use Which JOIN?  
  
| Scenario | Use This JOIN |  
|----------|---------------|  
| Show only matching records | **INNER JOIN** |  
| Show all from left table + matches | **LEFT JOIN** |  
| Show all from right table + matches | **RIGHT JOIN** |  
| Find records with no match | **LEFT/RIGHT JOIN + IS NULL** |  
| All possible combinations | **CROSS JOIN** |  
  
### Syntax Quick Reference  
  
```sql  
-- INNER JOIN  
SELECT * FROM t1 INNER JOIN t2 ON t1.id = t2.id;  
SELECT * FROM t1, t2 WHERE t1.id = t2.id;  
  
-- LEFT JOIN  
SELECT * FROM t1 LEFT JOIN t2 ON t1.id = t2.id;  
  
-- RIGHT JOIN  
SELECT * FROM t1 RIGHT JOIN t2 ON t1.id = t2.id;  
  
-- CROSS JOIN  
SELECT * FROM t1 CROSS JOIN t2;  
SELECT * FROM t1, t2;  
```  
  
---  
  
## Common Interview Questions  
  
### Q: Difference between INNER JOIN and WHERE clause?  
  
**Answer:**  
They can produce same results for matching records:  
```sql  
-- These are equivalent  
SELECT * FROM t1 INNER JOIN t2 ON t1.id = t2.id;  
SELECT * FROM t1, t2 WHERE t1.id = t2.id;  
```  
But INNER JOIN is:  
- More readable  
- Standard SQL syntax  
- Better for complex joins  
  
---  
  
### Q: Can you join more than 2 tables?  
  
**Answer:** Yes!  
```sql  
SELECT S.Name, M.Subject, M.Marks, S.Class  
FROM STUDENTS S  
INNER JOIN MARKS M ON S.RollNo = M.RollNo  
INNER JOIN CLASSES C ON S.Class = C.ClassName;  
```  
  
---  
  
### Q: What's the difference between LEFT JOIN and LEFT OUTER JOIN?  
  
**Answer:** They are EXACTLY the same! "OUTER" is optional.  
```sql  
-- Both are identical  
LEFT JOIN  
LEFT OUTER JOIN  
```  
  
---  
  
## CBSE Exam Pattern Questions  
  
### Question 1 (2 Marks)  
Write SQL query to display student names along with their marks using INNER JOIN.  
  
**Answer:**  
```sql  
SELECT STUDENTS.Name, MARKS.Marks  
FROM STUDENTS  
INNER JOIN MARKS  
ON STUDENTS.RollNo = MARKS.RollNo;  
```  
  
---  
  
### Question 2 (3 Marks)  
Differentiate between INNER JOIN and LEFT JOIN with example.  
  
**Answer:**  
  
**INNER JOIN:**  
- Returns only matching records  
- Example: Show students who have marks  
  
**LEFT JOIN:**  
- Returns all records from left table + matches from right  
- Shows NULL if no match  
- Example: Show all students, even those without marks  
  
```sql  
-- INNER JOIN (only students with marks)  
SELECT * FROM STUDENTS INNER JOIN MARKS   
ON STUDENTS.RollNo = MARKS.RollNo;  
  
-- LEFT JOIN (all students)  
SELECT * FROM STUDENTS LEFT JOIN MARKS   
ON STUDENTS.RollNo = MARKS.RollNo;  
```  
  
---  
  
### Question 3 (4 Marks)  
Given EMPLOYEE(EmpID, Name, Dept) and SALARY(EmpID, Amount) tables, write queries to:  
a) Show all employees with their salaries  
b) Show employees who haven't received salary  
c) Show department-wise total salary  
  
**Answer:**  
```sql  
-- (a) All employees with salaries (INNER JOIN)  
SELECT EMPLOYEE.Name, SALARY.Amount  
FROM EMPLOYEE  
INNER JOIN SALARY  
ON EMPLOYEE.EmpID = SALARY.EmpID;  
  
-- (b) Employees without salary (LEFT JOIN + NULL)  
SELECT EMPLOYEE.Name  
FROM EMPLOYEE  
LEFT JOIN SALARY  
ON EMPLOYEE.EmpID = SALARY.EmpID  
WHERE SALARY.EmpID IS NULL;  
  
-- (c) Department-wise total salary  
SELECT EMPLOYEE.Dept, SUM(SALARY.Amount) AS TotalSalary  
FROM EMPLOYEE  
INNER JOIN SALARY  
ON EMPLOYEE.EmpID = SALARY.EmpID  
GROUP BY EMPLOYEE.Dept;  
```  
  
---  
  
## Practice Exercises (Do These Yourself!)  
  
### Exercise Set 1  
Using STUDENTS and MARKS tables:  
  
1. Show students from class 12A with their Math marks  
2. Count how many students have marks in Science  
3. Find student(s) with highest marks in any subject  
4. Show students who have marks in both Math and Science  
5. Calculate class-wise total marks  
  
### Exercise Set 2  
Using CUSTOMERS and ORDERS tables:  
  
1. Show customers from Mumbai with their orders  
2. Find customers who ordered Laptop  
3. Show city-wise total order amount  
4. Find customer who spent the most  
5. Show products ordered by customer "Suresh"  
  
---  
  
## Tips for Success  
  
**✓ Always understand the data first**  
- Look at both tables  
- Identify common columns  
- Check for NULL values  
  
**✓ Draw Venn diagrams**  
- Helps visualize JOINs  
- INNER = intersection  
- LEFT = left circle + intersection  
- RIGHT = right circle + intersection  
  
**✓ Test with small data**  
- Use simple examples first  
- Verify output manually  
- Then try complex queries  
  
**✓ Practice daily**  
- Start with INNER JOIN (most common)  
- Then LEFT JOIN  
- Finally complex queries  
  
---  
  
## Summary  
  
**Key Takeaways:**  
  
1. **INNER JOIN** - Only matches (most used 80% of time)  
2. **LEFT JOIN** - All from left + matches (used 15%)  
3. **RIGHT JOIN** - All from right + matches (rarely used)  
4. **CROSS JOIN** - All combinations (almost never!)  
  
**Remember:**  
- JOINs combine tables using common columns  
- Use ON clause to specify join condition  
- Practice with real data to master  
- Start simple, gradually add complexity  
  
---  
  
**You're now ready to master JOINs! 🎯**  
  
Practice the queries, understand the output, and you'll be a JOIN expert in no time!  
  
**Good luck with your exams and interviews!** 💪  
  
---  
  
**Pro Tip:** Keep this document handy while practicing. Refer to visual diagrams when confused!