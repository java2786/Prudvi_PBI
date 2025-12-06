# SQL Advanced Concepts - Practical Guide  
  
## Database Setup  
  
Let's create a complete database for practicing advanced SQL concepts. We'll use a realistic Indian Railways ticket booking system.  
  
```sql  
-- Create database  
CREATE DATABASE railway_system;  
USE railway_system;  
  
-- Table 1: Passengers  
CREATE TABLE passengers (  
    passenger_id INT PRIMARY KEY AUTO_INCREMENT,  
    name VARCHAR(100),  
    email VARCHAR(100),  
    phone VARCHAR(15),  
    city VARCHAR(50),  
    registration_date DATE  
);  
  
-- Table 2: Trains  
CREATE TABLE trains (  
    train_id INT PRIMARY KEY,  
    train_name VARCHAR(100),  
    source_station VARCHAR(50),  
    destination_station VARCHAR(50),  
    departure_time TIME,  
    fare DECIMAL(10, 2)  
);  
  
-- Table 3: Bookings  
CREATE TABLE bookings (  
    booking_id INT PRIMARY KEY AUTO_INCREMENT,  
    passenger_id INT,  
    train_id INT,  
    booking_date DATE,  
    journey_date DATE,  
    seat_number VARCHAR(10),  
    booking_status VARCHAR(20),  
    fare_paid DECIMAL(10, 2),  
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id),  
    FOREIGN KEY (train_id) REFERENCES trains(train_id)  
);  
  
-- Table 4: Employee Performance  
CREATE TABLE employee_performance (  
    emp_id INT PRIMARY KEY,  
    emp_name VARCHAR(100),  
    department VARCHAR(50),  
    city VARCHAR(50),  
    sales_amount DECIMAL(10, 2),  
    performance_month DATE  
);  
  
-- Insert sample data  
INSERT INTO passengers (name, email, phone, city, registration_date) VALUES  
('Suresh Kumar', 'suresh@email.com', '9876543210', 'Pune', '2024-01-15'),  
('Ramesh Patel', 'ramesh@email.com', '9876543211', 'Chennai', '2024-02-20'),  
('Mahesh Sharma', 'mahesh@email.com', '9876543212', 'Mumbai', '2024-01-10'),  
('Dinesh Reddy', 'dinesh@email.com', '9876543213', 'Hyderabad', '2024-03-05'),  
('Mukesh Verma', 'mukesh@email.com', '9876543214', 'Delhi', '2024-02-28'),  
('Kamlesh Singh', 'kamlesh@email.com', '9876543215', 'Pune', '2024-01-25'),  
('Nitesh Gupta', 'nitesh@email.com', '9876543216', 'Bangalore', '2024-03-12'),  
('Hitesh Joshi', 'hitesh@email.com', '9876543217', 'Chennai', '2024-02-15'),  
('Ratnesh Mehta', 'ratnesh@email.com', NULL, 'Kolkata', '2024-01-30'),  
('Himesh Desai', 'himesh@email.com', '9876543219', 'Ahmedabad', '2024-03-20');  
  
INSERT INTO trains (train_id, train_name, source_station, destination_station, departure_time, fare) VALUES  
(12345, 'Deccan Queen', 'Pune', 'Mumbai', '07:15:00', 250.00),  
(12346, 'Shatabdi Express', 'Chennai', 'Bangalore', '06:00:00', 450.00),  
(12347, 'Rajdhani Express', 'Delhi', 'Mumbai', '16:55:00', 1200.00),  
(12348, 'Duronto Express', 'Hyderabad', 'Chennai', '20:30:00', 650.00),  
(12349, 'Garib Rath', 'Pune', 'Delhi', '22:00:00', 800.00);  
  
INSERT INTO bookings (passenger_id, train_id, booking_date, journey_date, seat_number, booking_status, fare_paid) VALUES  
(1, 12345, '2024-04-01', '2024-04-10', 'A1-25', 'Confirmed', 250.00),  
(1, 12347, '2024-04-05', '2024-04-15', 'B2-10', 'Confirmed', 1200.00),  
(2, 12346, '2024-04-02', '2024-04-12', 'A2-15', 'Confirmed', 450.00),  
(3, 12345, '2024-04-01', '2024-04-10', 'A1-26', 'Cancelled', 250.00),  
(4, 12348, '2024-04-03', '2024-04-13', 'C1-05', 'Confirmed', 650.00),  
(5, 12347, '2024-04-04', '2024-04-14', 'B1-20', 'Confirmed', 1200.00),  
(6, 12345, '2024-04-06', '2024-04-16', 'A3-12', 'Confirmed', 250.00),  
(7, 12346, '2024-04-07', '2024-04-17', 'A1-08', 'Waitlisted', 450.00),  
(8, 12348, '2024-04-08', '2024-04-18', 'C2-22', 'Confirmed', 650.00),  
(2, 12349, '2024-04-09', '2024-04-19', 'D1-15', 'Confirmed', 800.00),  
(9, 12345, '2024-04-10', '2024-04-20', NULL, 'Cancelled', 250.00),  
(10, 12347, '2024-04-11', '2024-04-21', 'B3-30', 'Confirmed', 1200.00);  
  
INSERT INTO employee_performance (emp_id, emp_name, department, city, sales_amount, performance_month) VALUES  
(101, 'Suresh Manager', 'Sales', 'Pune', 150000, '2024-01-01'),  
(102, 'Ramesh Lead', 'Sales', 'Chennai', 200000, '2024-01-01'),  
(103, 'Mahesh Executive', 'Marketing', 'Mumbai', 120000, '2024-01-01'),  
(104, 'Dinesh Agent', 'Sales', 'Hyderabad', 180000, '2024-01-01'),  
(101, 'Suresh Manager', 'Sales', 'Pune', 175000, '2024-02-01'),  
(102, 'Ramesh Lead', 'Sales', 'Chennai', 190000, '2024-02-01'),  
(103, 'Mahesh Executive', 'Marketing', 'Mumbai', 130000, '2024-02-01'),  
(104, 'Dinesh Agent', 'Sales', 'Hyderabad', 195000, '2024-02-01'),  
(101, 'Suresh Manager', 'Sales', 'Pune', 185000, '2024-03-01'),  
(102, 'Ramesh Lead', 'Sales', 'Chennai', 210000, '2024-03-01');  
```  
  
---  
  
## Module 1: Data Modification Operations  
  
### Theory Brief  
  
Data modification involves changing existing data in tables through INSERT (adding new records), UPDATE (modifying existing records), and DELETE (removing records). Handling NULL values is critical as NULL represents missing or unknown data.  
  
### Problem 1: Insert a New Passenger  
  
**Scenario:** A new passenger Jitesh from Kolkata wants to register.  
  
```sql  
-- Solution  
INSERT INTO passengers (name, email, phone, city, registration_date)   
VALUES ('Jitesh Roy', 'jitesh@email.com', '9876543220', 'Kolkata', '2024-04-15');  
  
-- Verify  
SELECT * FROM passengers WHERE name = 'Jitesh Roy';  
```  
  
### Problem 2: Insert Multiple Bookings at Once  
  
**Scenario:** Gukesh and Jitesh both booked Deccan Queen for the same date.  
  
```sql  
-- Solution  
INSERT INTO bookings (passenger_id, train_id, booking_date, journey_date, seat_number, booking_status, fare_paid)  
VALUES   
(10, 12345, '2024-04-12', '2024-04-22', 'A2-18', 'Confirmed', 250.00),  
(11, 12345, '2024-04-12', '2024-04-22', 'A2-19', 'Confirmed', 250.00);  
  
-- Verify  
SELECT * FROM bookings WHERE booking_date = '2024-04-12';  
```  
  
### Problem 3: Update Booking Status  
  
**Scenario:** Passenger with booking_id 7 got confirmed from waitlist.  
  
```sql  
-- Solution  
UPDATE bookings   
SET booking_status = 'Confirmed', seat_number = 'A1-25'   
WHERE booking_id = 7;  
  
-- Verify  
SELECT * FROM bookings WHERE booking_id = 7;  
```  
  
### Problem 4: Update Multiple Records Based on Condition  
  
**Scenario:** All cancelled bookings need fare_paid to be set to 0 (refund processed).  
  
```sql  
-- Solution  
UPDATE bookings   
SET fare_paid = 0   
WHERE booking_status = 'Cancelled';  
  
-- Verify  
SELECT * FROM bookings WHERE booking_status = 'Cancelled';  
```  
  
### Problem 5: Update with Calculation  
  
**Scenario:** Apply 10% discount on all bookings for Deccan Queen train.  
  
```sql  
-- Solution  
UPDATE bookings   
SET fare_paid = fare_paid * 0.9   
WHERE train_id = 12345;  
  
-- Verify  
SELECT booking_id, fare_paid FROM bookings WHERE train_id = 12345;  
```  
  
### Problem 6: Delete a Specific Record  
  
**Scenario:** Remove booking with ID 11 (duplicate entry).  
  
```sql  
-- Solution  
DELETE FROM bookings   
WHERE booking_id = 11;  
  
-- Verify  
SELECT * FROM bookings WHERE booking_id = 11;  
```  
  
### Problem 7: Delete Multiple Records  
  
**Scenario:** Remove all cancelled bookings older than March 2024.  
  
```sql  
-- Solution  
DELETE FROM bookings   
WHERE booking_status = 'Cancelled'   
AND booking_date < '2024-04-01';  
  
-- Verify  
SELECT * FROM bookings WHERE booking_status = 'Cancelled';  
```  
  
### Problem 8: Handling NULL with IFNULL  
  
**Scenario:** Display passenger phone numbers, show 'Not Provided' if NULL.  
  
```sql  
-- Solution  
SELECT name, IFNULL(phone, 'Not Provided') AS phone_number   
FROM passengers;  
```  
  
### Problem 9: Using COALESCE with Multiple Columns  
  
**Scenario:** Display seat number, if NULL show 'No Seat', use booking_status as fallback.  
  
```sql  
-- Solution  
SELECT booking_id,   
       COALESCE(seat_number, 'No Seat Assigned') AS seat_info,  
       booking_status  
FROM bookings;  
```  
  
### Problem 10: Update NULL Values  
  
**Scenario:** Update all NULL phone numbers to 'NA'.  
  
```sql  
-- Solution  
UPDATE passengers   
SET phone = 'NA'   
WHERE phone IS NULL;  
  
-- Verify  
SELECT * FROM passengers WHERE phone = 'NA';  
```  
  
---  
  
## Module 2: Window Functions  
  
### Theory Brief  
  
Window functions perform calculations across a set of rows related to the current row without collapsing the result set. Unlike GROUP BY, they maintain individual row identity while providing aggregate information.  
  
### Problem 11: ROW_NUMBER - Assign Unique Numbers  
  
**Scenario:** Assign row numbers to all bookings ordered by booking_date.  
  
```sql  
-- Solution  
SELECT booking_id, passenger_id, booking_date,  
       ROW_NUMBER() OVER (ORDER BY booking_date) AS row_num  
FROM bookings;  
```  
  
### Problem 12: ROW_NUMBER with PARTITION  
  
**Scenario:** Assign row numbers to bookings for each passenger separately.  
  
```sql  
-- Solution  
SELECT booking_id, passenger_id, train_id, booking_date,  
       ROW_NUMBER() OVER (PARTITION BY passenger_id ORDER BY booking_date) AS booking_sequence  
FROM bookings;  
```  
  
### Problem 13: RANK Function  
  
**Scenario:** Rank trains by fare (highest to lowest), show gaps for ties.  
  
```sql  
-- Solution  
SELECT train_name, fare,  
       RANK() OVER (ORDER BY fare DESC) AS fare_rank  
FROM trains;  
```  
  
### Problem 14: DENSE_RANK Function  
  
**Scenario:** Rank employees by sales_amount without gaps in ranking.  
  
```sql  
-- Solution  
SELECT emp_name, sales_amount, performance_month,  
       DENSE_RANK() OVER (ORDER BY sales_amount DESC) AS sales_rank  
FROM employee_performance;  
```  
  
### Problem 15: RANK vs DENSE_RANK Comparison  
  
**Scenario:** Show difference between RANK and DENSE_RANK for employee sales.  
  
```sql  
-- Solution  
SELECT emp_name, sales_amount,  
       RANK() OVER (ORDER BY sales_amount DESC) AS rank_with_gaps,  
       DENSE_RANK() OVER (ORDER BY sales_amount DESC) AS rank_no_gaps  
FROM employee_performance  
WHERE performance_month = '2024-03-01';  
```  
  
### Problem 16: PARTITION BY with RANK  
  
**Scenario:** Rank employees within each department by sales.  
  
```sql  
-- Solution  
SELECT emp_name, department, sales_amount,  
       RANK() OVER (PARTITION BY department ORDER BY sales_amount DESC) AS dept_rank  
FROM employee_performance  
WHERE performance_month = '2024-03-01';  
```  
  
### Problem 17: Window SUM Function  
  
**Scenario:** Calculate running total of sales for each employee across months.  
  
```sql  
-- Solution  
SELECT emp_id, emp_name, performance_month, sales_amount,  
       SUM(sales_amount) OVER (PARTITION BY emp_id ORDER BY performance_month) AS running_total  
FROM employee_performance  
ORDER BY emp_id, performance_month;  
```  
  
### Problem 18: Window AVG Function  
  
**Scenario:** Show each booking's fare along with average fare of that train.  
  
```sql  
-- Solution  
SELECT b.booking_id, t.train_name, b.fare_paid,  
       AVG(b.fare_paid) OVER (PARTITION BY b.train_id) AS avg_train_fare  
FROM bookings b  
JOIN trains t ON b.train_id = t.train_id;  
```  
  
### Problem 19: Find Top 2 Bookings Per Passenger  
  
**Scenario:** Get the 2 most recent bookings for each passenger.  
  
```sql  
-- Solution  
SELECT * FROM (  
    SELECT booking_id, passenger_id, booking_date, train_id,  
           ROW_NUMBER() OVER (PARTITION BY passenger_id ORDER BY booking_date DESC) AS rn  
    FROM bookings  
) AS ranked_bookings  
WHERE rn <= 2;  
```  
  
### Problem 20: Moving Average  
  
**Scenario:** Calculate 2-month moving average of sales for each employee.  
  
```sql  
-- Solution  
SELECT emp_id, emp_name, performance_month, sales_amount,  
       AVG(sales_amount) OVER (  
           PARTITION BY emp_id   
           ORDER BY performance_month   
           ROWS BETWEEN 1 PRECEDING AND CURRENT ROW  
       ) AS moving_avg  
FROM employee_performance  
ORDER BY emp_id, performance_month;  
```  
  
---  
  
## Module 3: String Functions  
  
### Theory Brief  
  
String functions manipulate text data. Common operations include concatenation (joining strings), changing case, extracting substrings, and calculating string length.  
  
### Problem 21: CONCAT - Combine Columns  
  
**Scenario:** Create full address format "Name - City".  
  
```sql  
-- Solution  
SELECT CONCAT(name, ' - ', city) AS passenger_info   
FROM passengers;  
```  
  
### Problem 22: CONCAT with Multiple Columns  
  
**Scenario:** Create booking summary: "Passenger Name booked Train Name on Date".  
  
```sql  
-- Solution  
SELECT CONCAT(p.name, ' booked ', t.train_name, ' on ', b.booking_date) AS booking_summary  
FROM bookings b  
JOIN passengers p ON b.passenger_id = p.passenger_id  
JOIN trains t ON b.train_id = t.train_id  
LIMIT 5;  
```  
  
### Problem 23: LENGTH Function  
  
**Scenario:** Find passengers whose names are longer than 12 characters.  
  
```sql  
-- Solution  
SELECT name, LENGTH(name) AS name_length   
FROM passengers   
WHERE LENGTH(name) > 12;  
```  
  
### Problem 24: UPPER and LOWER Functions  
  
**Scenario:** Display all train names in uppercase and cities in lowercase.  
  
```sql  
-- Solution  
SELECT UPPER(train_name) AS train_upper,   
       LOWER(source_station) AS source_lower,  
       LOWER(destination_station) AS dest_lower  
FROM trains;  
```  
  
### Problem 25: SUBSTRING Function  
  
**Scenario:** Extract first 5 characters of passenger names.  
  
```sql  
-- Solution  
SELECT name, SUBSTRING(name, 1, 5) AS short_name   
FROM passengers;  
```  
  
### Problem 26: SUBSTRING with LOCATE  
  
**Scenario:** Extract first name from full name (everything before first space).  
  
```sql  
-- Solution  
SELECT name,   
       SUBSTRING(name, 1, LOCATE(' ', name) - 1) AS first_name  
FROM passengers  
WHERE LOCATE(' ', name) > 0;  
```  
  
### Problem 27: REPLACE Function  
  
**Scenario:** Replace 'Express' with 'Exp' in train names.  
  
```sql  
-- Solution  
SELECT train_name,   
       REPLACE(train_name, 'Express', 'Exp') AS short_train_name  
FROM trains;  
```  
  
### Problem 28: TRIM Function  
  
**Scenario:** Clean up city names by removing extra spaces.  
  
```sql  
-- Solution  
SELECT city, TRIM(city) AS cleaned_city   
FROM passengers;  
```  
  
### Problem 29: CONCAT_WS (Concat with Separator)  
  
**Scenario:** Create passenger contact info separated by pipes.  
  
```sql  
-- Solution  
SELECT CONCAT_WS(' | ', name, email, phone, city) AS contact_details   
FROM passengers  
LIMIT 5;  
```  
  
### Problem 30: Combining String Functions  
  
**Scenario:** Create formatted passenger ID: First 3 letters of name + passenger_id in uppercase.  
  
```sql  
-- Solution  
SELECT name,   
       CONCAT(UPPER(SUBSTRING(name, 1, 3)), '-', passenger_id) AS formatted_id  
FROM passengers;  
```  
  
---  
  
## Module 4: Date and Time Functions  
  
### Theory Brief  
  
Date functions handle temporal data. They allow extraction of date parts, calculation of differences, addition/subtraction of intervals, and formatting.  
  
### Problem 31: NOW() and CURDATE()  
  
**Scenario:** Display current date and time.  
  
```sql  
-- Solution  
SELECT NOW() AS current_datetime,   
       CURDATE() AS current_date,  
       CURTIME() AS current_time;  
```  
  
### Problem 32: DATEDIFF Function  
  
**Scenario:** Calculate days between booking date and journey date for all bookings.  
  
```sql  
-- Solution  
SELECT booking_id, booking_date, journey_date,  
       DATEDIFF(journey_date, booking_date) AS days_advance  
FROM bookings;  
```  
  
### Problem 33: Find Bookings Made Within 7 Days  
  
**Scenario:** Find bookings where journey is within 7 days from booking.  
  
```sql  
-- Solution  
SELECT booking_id, booking_date, journey_date,  
       DATEDIFF(journey_date, booking_date) AS advance_days  
FROM bookings  
WHERE DATEDIFF(journey_date, booking_date) <= 7;  
```  
  
### Problem 34: DATE_ADD Function  
  
**Scenario:** Calculate journey date + 1 day (return journey).  
  
```sql  
-- Solution  
SELECT booking_id, journey_date,  
       DATE_ADD(journey_date, INTERVAL 1 DAY) AS return_date  
FROM bookings;  
```  
  
### Problem 35: DATE_SUB Function  
  
**Scenario:** Find what date was 30 days before each booking.  
  
```sql  
-- Solution  
SELECT booking_id, booking_date,  
       DATE_SUB(booking_date, INTERVAL 30 DAY) AS date_30_days_ago  
FROM bookings;  
```  
  
### Problem 36: YEAR, MONTH, DAY Extraction  
  
**Scenario:** Extract year, month, and day from registration dates.  
  
```sql  
-- Solution  
SELECT name, registration_date,  
       YEAR(registration_date) AS reg_year,  
       MONTH(registration_date) AS reg_month,  
       DAY(registration_date) AS reg_day  
FROM passengers;  
```  
  
### Problem 37: MONTHNAME and DAYNAME  
  
**Scenario:** Display month and day names for booking dates.  
  
```sql  
-- Solution  
SELECT booking_id, booking_date,  
       MONTHNAME(booking_date) AS month_name,  
       DAYNAME(booking_date) AS day_name  
FROM bookings;  
```  
  
### Problem 38: DATE_FORMAT Function  
  
**Scenario:** Format booking date as 'DD-MM-YYYY'.  
  
```sql  
-- Solution  
SELECT booking_id,   
       DATE_FORMAT(booking_date, '%d-%m-%Y') AS formatted_date  
FROM bookings;  
```  
  
### Problem 39: Calculate Age of Registration  
  
**Scenario:** Find how many days since passenger registered.  
  
```sql  
-- Solution  
SELECT name, registration_date,  
       DATEDIFF(CURDATE(), registration_date) AS days_since_registration  
FROM passengers;  
```  
  
### Problem 40: Find Registrations in Specific Month  
  
**Scenario:** Find all passengers registered in February 2024.  
  
```sql  
-- Solution  
SELECT name, registration_date  
FROM passengers  
WHERE YEAR(registration_date) = 2024   
AND MONTH(registration_date) = 2;  
```  
  
---  
  
## Module 5: Performance Optimization  
  
### Theory Brief  
  
Indexes are data structures that improve query performance by allowing faster data retrieval. They work like a book index, helping the database find data without scanning every row. However, indexes consume storage and slow down INSERT/UPDATE/DELETE operations.  
  
### Problem 41: Check Query Execution Without Index  
  
**Scenario:** Analyze performance of finding passenger by email.  
  
```sql  
-- Solution  
EXPLAIN SELECT * FROM passengers WHERE email = 'suresh@email.com';  
  
-- Observe: type = ALL (full table scan)  
```  
  
### Problem 42: Create Single Column Index  
  
**Scenario:** Create index on email column to speed up searches.  
  
```sql  
-- Solution  
CREATE INDEX idx_passenger_email ON passengers(email);  
  
-- Verify improvement  
EXPLAIN SELECT * FROM passengers WHERE email = 'suresh@email.com';  
  
-- Observe: type = ref (uses index)  
```  
  
### Problem 43: Create Index on Foreign Key  
  
**Scenario:** Create index on passenger_id in bookings table.  
  
```sql  
-- Solution  
CREATE INDEX idx_booking_passenger ON bookings(passenger_id);  
  
-- Test query  
EXPLAIN SELECT * FROM bookings WHERE passenger_id = 1;  
```  
  
### Problem 44: Composite Index (Multiple Columns)  
  
**Scenario:** Create index on booking_date and booking_status together.  
  
```sql  
-- Solution  
CREATE INDEX idx_booking_date_status ON bookings(booking_date, booking_status);  
  
-- Test query  
EXPLAIN SELECT * FROM bookings   
WHERE booking_date = '2024-04-01' AND booking_status = 'Confirmed';  
```  
  
### Problem 45: Show All Indexes on a Table  
  
**Scenario:** Display all indexes created on bookings table.  
  
```sql  
-- Solution  
SHOW INDEX FROM bookings;  
```  
  
### Problem 46: Drop an Index  
  
**Scenario:** Remove an unused index.  
  
```sql  
-- Solution  
DROP INDEX idx_booking_date_status ON bookings;  
  
-- Verify  
SHOW INDEX FROM bookings;  
```  
  
### Problem 47: Index on Date Column  
  
**Scenario:** Create index on journey_date for faster date-based queries.  
  
```sql  
-- Solution  
CREATE INDEX idx_journey_date ON bookings(journey_date);  
  
-- Test query  
EXPLAIN SELECT * FROM bookings WHERE journey_date = '2024-04-10';  
```  
  
### Problem 48: Query Optimization - Avoid SELECT *  
  
**Scenario:** Compare performance of SELECT * vs specific columns.  
  
```sql  
-- Bad practice  
SELECT * FROM bookings WHERE train_id = 12345;  
  
-- Good practice (faster)  
SELECT booking_id, passenger_id, journey_date   
FROM bookings   
WHERE train_id = 12345;  
```  
  
### Problem 49: Use LIMIT for Large Result Sets  
  
**Scenario:** Retrieve only required number of records.  
  
```sql  
-- Solution: Get only first 5 bookings instead of all  
SELECT * FROM bookings   
ORDER BY booking_date DESC   
LIMIT 5;  
```  
  
### Problem 50: Index on JOIN Columns  
  
**Scenario:** Optimize JOIN operations with indexes.  
  
```sql  
-- Create indexes on JOIN columns  
CREATE INDEX idx_booking_train ON bookings(train_id);  
CREATE INDEX idx_train_id ON trains(train_id);  
  
-- Test JOIN query  
EXPLAIN SELECT b.booking_id, t.train_name   
FROM bookings b  
JOIN trains t ON b.train_id = t.train_id;  
  
-- Observe: Both tables use indexes for JOIN  
```  
  
### Problem 51: ANALYZE TABLE  
  
**Scenario:** Update table statistics for better query planning.  
  
```sql  
-- Solution  
ANALYZE TABLE bookings;  
ANALYZE TABLE passengers;  
```  
  
### Problem 52: Avoid Functions on Indexed Columns  
  
**Scenario:** Compare inefficient vs efficient date queries.  
  
```sql  
-- Bad: Function on indexed column (doesn't use index)  
SELECT * FROM bookings WHERE YEAR(booking_date) = 2024;  
  
-- Good: Range query (uses index)  
SELECT * FROM bookings   
WHERE booking_date >= '2024-01-01'   
AND booking_date < '2025-01-01';  
```  
  
### Problem 53: Index Cardinality Check  
  
**Scenario:** Check uniqueness of values in indexed columns.  
  
```sql  
-- Solution  
SELECT COUNT(DISTINCT email) AS unique_emails,   
       COUNT(*) AS total_records,  
       (COUNT(DISTINCT email) / COUNT(*)) * 100 AS cardinality_percentage  
FROM passengers;  
  
-- High cardinality (close to 100%) = good for indexing  
```  
  
### Problem 54: Create UNIQUE Index  
  
**Scenario:** Ensure email addresses are unique across passengers.  
  
```sql  
-- Solution  
CREATE UNIQUE INDEX idx_unique_email ON passengers(email);  
  
-- This will fail if duplicate emails exist  
-- Test: Try inserting duplicate email  
-- INSERT INTO passengers (name, email, city, registration_date)   
-- VALUES ('Test User', 'suresh@email.com', 'Pune', '2024-04-20');  
```  
  
### Problem 55: Query Optimization with WHERE Clause  
  
**Scenario:** Use indexed columns in WHERE clause for better performance.  
  
```sql  
-- Good: Uses index on passenger_id  
EXPLAIN SELECT * FROM bookings WHERE passenger_id = 5;  
  
-- Bad: Cannot use index efficiently  
EXPLAIN SELECT * FROM bookings WHERE passenger_id + 1 = 6;  
```  
  
---  
  
## Comprehensive Practice Scenarios  
  
### Scenario 1: Monthly Booking Report  
  
Create a report showing total bookings and revenue per month.  
  
```sql  
-- Solution  
SELECT DATE_FORMAT(booking_date, '%Y-%m') AS booking_month,  
       COUNT(*) AS total_bookings,  
       SUM(fare_paid) AS total_revenue,  
       AVG(fare_paid) AS avg_fare,  
       COUNT(DISTINCT passenger_id) AS unique_passengers  
FROM bookings  
WHERE booking_status = 'Confirmed'  
GROUP BY DATE_FORMAT(booking_date, '%Y-%m')  
ORDER BY booking_month;  
```  
  
### Scenario 2: Passenger Booking History with Rankings  
  
Show complete booking history with rankings for each passenger.  
  
```sql  
-- Solution  
SELECT p.name,  
       t.train_name,  
       b.booking_date,  
       b.fare_paid,  
       ROW_NUMBER() OVER (PARTITION BY p.passenger_id ORDER BY b.booking_date) AS booking_number,  
       DENSE_RANK() OVER (ORDER BY b.fare_paid DESC) AS fare_rank  
FROM bookings b  
JOIN passengers p ON b.passenger_id = p.passenger_id  
JOIN trains t ON b.train_id = t.train_id  
WHERE b.booking_status = 'Confirmed'  
ORDER BY p.name, b.booking_date;  
```  
  
### Scenario 3: Data Cleanup Operation  
  
Update all records with proper formatting and handle NULLs.  
  
```sql  
-- Solution  
-- Step 1: Clean passenger names (remove extra spaces)  
UPDATE passengers   
SET name = TRIM(name);  
  
-- Step 2: Update NULL seat numbers for cancelled bookings  
UPDATE bookings   
SET seat_number = 'NOT_ASSIGNED'   
WHERE seat_number IS NULL AND booking_status = 'Cancelled';  
  
-- Step 3: Standardize city names to proper case  
UPDATE passengers   
SET city = CONCAT(UPPER(SUBSTRING(city, 1, 1)), LOWER(SUBSTRING(city, 2)));  
  
-- Verify  
SELECT * FROM passengers LIMIT 5;  
```  
  
### Scenario 4: Performance Analysis Query  
  
Find top performing employees with month-over-month growth.  
  
```sql  
-- Solution  
WITH monthly_sales AS (  
    SELECT emp_id, emp_name,   
           performance_month,  
           sales_amount,  
           LAG(sales_amount) OVER (PARTITION BY emp_id ORDER BY performance_month) AS prev_month_sales  
    FROM employee_performance  
)  
SELECT emp_name,  
       DATE_FORMAT(performance_month, '%M %Y') AS month,  
       sales_amount,  
       prev_month_sales,  
       COALESCE(sales_amount - prev_month_sales, 0) AS growth,  
       COALESCE(ROUND(((sales_amount - prev_month_sales) / prev_month_sales) * 100, 2), 0) AS growth_percentage  
FROM monthly_sales  
ORDER BY emp_id, performance_month;  
```  
  
### Scenario 5: Advanced Date Manipulation  
  
Find passengers with upcoming journeys and send reminder.  
  
```sql  
-- Solution  
SELECT p.name,  
       p.email,  
       t.train_name,  
       b.journey_date,  
       DATEDIFF(b.journey_date, CURDATE()) AS days_remaining,  
       CASE   
           WHEN DATEDIFF(b.journey_date, CURDATE()) <= 2 THEN 'Send Urgent Reminder'  
           WHEN DATEDIFF(b.journey_date, CURDATE()) <= 7 THEN 'Send Reminder'  
           ELSE 'No Action'  
       END AS reminder_status  
FROM bookings b  
JOIN passengers p ON b.passenger_id = p.passenger_id  
JOIN trains t ON b.train_id = t.train_id  
WHERE b.booking_status = 'Confirmed'  
AND b.journey_date >= CURDATE()  
ORDER BY days_remaining;  
```  
  
---  
  
## Quiz Section  
  
### Quiz 1: Data Modification  
  
**Q1.** Which command is used to modify existing data in a table?  
a) INSERT  
b) UPDATE  
c) ALTER  
d) MODIFY  
  
**Q2.** What does IFNULL(column_name, 'default') do?  
a) Checks if column is NULL  
b) Returns 'default' if column is NULL  
c) Replaces all NULL values permanently  
d) Deletes NULL rows  
  
**Q3.** What's the difference between DELETE and TRUNCATE?  
a) No difference  
b) DELETE can use WHERE, TRUNCATE cannot  
c) TRUNCATE is slower  
d) DELETE removes table structure  
  
**Answers:** Q1-b, Q2-b, Q3-b  
  
### Quiz 2: Window Functions  
  
**Q4.** What's the difference between RANK() and DENSE_RANK()?  
a) No difference  
b) RANK() skips numbers after ties, DENSE_RANK() doesn't  
c) DENSE_RANK() is faster  
d) RANK() is more accurate  
  
**Q5.** What does PARTITION BY do in window functions?  
a) Divides data into groups for separate calculations  
b) Filters data  
c) Sorts data  
d) Joins tables  
  
**Q6.** Which function assigns sequential numbers without considering duplicates?  
a) RANK()  
b) DENSE_RANK()  
c) ROW_NUMBER()  
d) SEQUENCE()  
  
**Answers:** Q4-b, Q5-a, Q6-c  
  
### Quiz 3: String and Date Functions  
  
**Q7.** CONCAT('Hello', ' ', 'World') returns:  
a) Hello World  
b) HelloWorld  
c) Hello, World  
d) Error  
  
**Q8.** What does DATEDIFF('2024-04-10', '2024-04-01') return?  
a) 9  
b) 10  
c) 11  
d) -9  
  
**Q9.** Which function converts text to uppercase?  
a) UCASE()  
b) UPPER()  
c) TO_UPPER()  
d) Both a and b  
  
**Answers:** Q7-a, Q8-a, Q9-d  
  
### Quiz 4: Performance Optimization  
  
**Q10.** What is the primary purpose of an index?  
a) Store data  
b) Speed up data retrieval  
c) Delete data faster  
d) Backup data  
  
**Q11.** When should you avoid using indexes?  
a) On large tables  
b) On columns frequently used in WHERE  
c) On small tables or columns with low cardinality  
d) On primary keys  
  
**Q12.** Which is more efficient?  
a) SELECT * FROM table  
b) SELECT column1, column2 FROM table  
c) Both are same  
d) Depends on the database  
  
**Answers:** Q10-b, Q11-c, Q12-b  
  
---  
  
## Mini Assignments  
  
### Assignment 1: Data Modification Challenge  
  
**Task:** Create a new table called 'train_maintenance' with columns: maintenance_id, train_id, maintenance_date, status. Insert 5 records. Update status to 'Completed' for trains maintained before April 2024. Delete pending maintenance records.  
  
**Expected Operations:**  
- CREATE TABLE  
- INSERT (5 records)  
- UPDATE with WHERE  
- DELETE with condition  
  
### Assignment 2: Window Functions Challenge  
  
**Task:** Using the employee_performance table, create a query that shows:  
- Employee name  
- Current month sales  
- Previous month sales  
- Rank within their department  
- Running total of sales  
  
Use at least 3 different window functions.  
  
### Assignment 3: String Manipulation Challenge  
  
**Task:** Create a formatted report from passengers table showing:  
- Full name in uppercase  
- First name only (extracted from full name)  
- Email domain (part after @)  
- Contact info formatted as "NAME (CITY) - EMAIL"  
  
Use CONCAT, SUBSTRING, UPPER, and other string functions.  
  
### Assignment 4: Date Functions Challenge  
  
**Task:** Create a booking analytics report showing:  
- Bookings made in each month of 2024  
- Average advance booking days (journey_date - booking_date)  
- Count of last-minute bookings (within 3 days)  
- List of upcoming journeys in next 30 days  
  
### Assignment 5: Performance Optimization Challenge  
  
**Task:**   
1. Create appropriate indexes on passengers and bookings tables  
2. Write a query to find all confirmed bookings with passenger details and train info  
3. Use EXPLAIN to verify indexes are being used  
4. Document performance improvement with and without indexes  
  
---  
  
## Key Takeaways  
  
**Data Modification:**  
- Always use WHERE clause with UPDATE and DELETE to avoid modifying all rows  
- Use IFNULL or COALESCE to handle NULL values in queries  
- Test UPDATE and DELETE queries with SELECT first  
  
**Window Functions:**  
- ROW_NUMBER() gives unique sequential numbers  
- RANK() shows gaps in ranking after ties  
- DENSE_RANK() shows no gaps in ranking  
- Use PARTITION BY to reset calculations for each group  
  
**String Functions:**  
- CONCAT() joins strings together  
- LENGTH() returns character count  
- SUBSTRING() extracts part of a string  
- UPPER()/LOWER() change case  
  
**Date Functions:**  
- DATEDIFF() calculates days between dates  
- DATE_ADD()/DATE_SUB() adds or subtracts intervals  
- DATE_FORMAT() formats dates for display  
- YEAR(), MONTH(), DAY() extract date parts  
  
**Performance:**  
- Create indexes on columns used in WHERE, JOIN, and ORDER BY  
- Avoid functions on indexed columns in WHERE clause  
- Select only needed columns, not SELECT *  
- Use EXPLAIN to analyze query performance  
- Regularly run ANALYZE TABLE to update statistics  
  
---  
  
## Next Steps for Practice  
  
1. Create your own tables with Indian context (LIC policies, Flipkart orders, etc.)  
2. Write 10 queries using each topic covered  
3. Experiment with combining multiple concepts in single queries  
4. Use EXPLAIN to understand query execution plans  
5. Practice data modification with backup tables first  
6. Build complete reports using window functions  
7. Create stored procedures combining these concepts  
  
**Remember:** Practice is the key. Run each query multiple times with different conditions. Understanding comes from doing, not just reading!  
  
---  
  
**Document End - Happy Learning!**