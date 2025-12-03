# MySQL Quickstart Guide (Terminal)  
  
## 1. Check if MySQL is installed  
```bash  
$ mysql --version  
```  
  
## 2. Connect to MySQL Server (2 Options)  
```bash  
$ mysql --host localhost --port 3306 -u root -proot  
# or  
$ mysql -u root -proot  
```  
  
## 3. Show all available databases  
```sql  
SHOW DATABASES;  
```  
  
## 4. Create a new database named `tutorial`  
```sql  
CREATE DATABASE tutorial;  
```  
  
## 5. Switch to the `tutorial` database  
```sql  
USE tutorial;  
```  
  
## 6. Confirm the current active database  
```sql  
SELECT DATABASE();  
```  
  
## 7. Show tables in the current database  
```sql  
SHOW TABLES;  
```  
  
## 8. Create a `product` table  
```sql  
CREATE TABLE product (  
    name VARCHAR(30),  
    price INT,  
    manufacturer VARCHAR(50),  
    release_date DATE,  
    quantity INT  
);  
```  
  
## 9. Describe the structure of the `product` table  
```sql  
DESC product;  
```  
  
## 10. Insert a record into the `product` table  
```sql  
INSERT INTO product   
VALUES ('mobile', 35000, 'one plus', '2025-06-12', 45);  
```  
  
## 11. Read specific data from the table  
```sql  
SELECT name, price FROM product;  
```  
  
## 12. Read all data from the table  
```sql  
SELECT * FROM product;  
```  
  
