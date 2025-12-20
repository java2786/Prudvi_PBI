# Common NumPy Methods Reference  
  
## Quick Reference Table  
  
| Method | Description | Input Example | Output |  
|--------|-------------|---------------|--------|  
| `np.add(a, b)` | Element-wise addition of two arrays | `np.add([10, 20, 30], [5, 15, 25])` | `[15, 35, 55]` |  
| `np.subtract(a, b)` | Element-wise subtraction of two arrays | `np.subtract([100, 200, 300], [25, 50, 75])` | `[75, 150, 225]` |  
| `np.multiply(a, b)` | Element-wise multiplication of two arrays | `np.multiply([10, 20, 30], [2, 3, 4])` | `[20, 60, 120]` |  
| `np.divide(a, b)` | Element-wise division of two arrays | `np.divide([100, 200, 300], [10, 20, 30])` | `[10.0, 10.0, 10.0]` |  
| `np.std(array)` | Calculates the standard deviation | `np.std([10, 20, 30, 40, 50])` | `14.142135623730951` |  
| `np.var(array)` | Calculates the variance | `np.var([10, 20, 30, 40, 50])` | `200.0` |  
| `np.median(array)` | Computes the median | `np.median([10, 20, 30, 40, 50])` | `30.0` |  
| `np.percentile(array, q)` | Computes the q-th percentile | `np.percentile([10, 20, 30, 40, 50], 75)` | `40.0` |  
| `np.sort(array)` | Returns a sorted copy of the array | `np.sort([50, 20, 40, 10, 30])` | `[10, 20, 30, 40, 50]` |  
| `np.argsort(array)` | Returns the indices that would sort the array | `np.argsort([50, 20, 40, 10, 30])` | `[3, 1, 4, 2, 0]` |  
| `np.unique(array)` | Finds the unique elements | `np.unique([10, 20, 10, 30, 20, 40])` | `[10, 20, 30, 40]` |  
| `np.sum(array, axis)` | Computes the sum along a specified axis | `np.sum([10, 20, 30, 40])` | `100` |  
| `np.cumsum(array)` | Returns the cumulative sum | `np.cumsum([10, 20, 30, 40])` | `[10, 30, 60, 100]` |  
| `np.clip(array, a_min, a_max)` | Limits values within a specified range | `np.clip([5, 15, 25, 35], 10, 30)` | `[10, 15, 25, 30]` |  
  
---  
  
## Detailed Examples with Real-World Context  
  
### 1. Arithmetic Operations  
  
#### np.add() - Railway Ticket Calculation  
```python  
import numpy as np  
  
# Base ticket prices (Pune to Chennai)  
base_prices = np.array([100, 250, 500, 800])  # Sleeper, AC-3, AC-2, AC-1  
  
# GST and service charges  
charges = np.array([18, 45, 90, 144])  
  
# Calculate total prices  
total = np.add(base_prices, charges)  
print("Total Prices:", total)  
# Output: [118 295 590 944]  
```  
  
#### np.subtract() - Discount Calculator  
```python  
# Original prices at Flipkart  
prices = np.array([15000, 8000, 3000, 1200])  
  
# Discount amounts  
discounts = np.array([2000, 1200, 450, 200])  
  
# Final prices  
final_prices = np.subtract(prices, discounts)  
print("After Discount:", final_prices)  
# Output: [13000  6800  2550  1000]  
```  
  
#### np.multiply() - GST Calculator  
```python  
# Product prices  
product_prices = np.array([1000, 2000, 3000, 5000])  
  
# GST rate (18% = 1.18)  
gst_multiplier = np.array([1.18, 1.18, 1.18, 1.18])  
  
# Prices with GST  
prices_with_gst = np.multiply(product_prices, gst_multiplier)  
print("Prices with GST:", prices_with_gst)  
# Output: [1180. 2360. 3540. 5900.]  
```  
  
#### np.divide() - Average Marks Calculation  
```python  
# Total marks obtained by students  
total_marks = np.array([450, 380, 420, 490])  
  
# Number of subjects  
num_subjects = np.array([5, 5, 5, 5])  
  
# Calculate average marks  
average = np.divide(total_marks, num_subjects)  
print("Average Marks:", average)  
# Output: [90. 76. 84. 98.]  
```  
  
---  
  
### 2. Statistical Operations  
  
#### np.std() - Temperature Variation Analysis  
```python  
# Daily temperatures in Chennai (in Celsius)  
temperatures = np.array([32, 35, 33, 36, 34, 35, 33])  
  
# Calculate standard deviation  
std_dev = np.std(temperatures)  
print("Temperature Standard Deviation:", std_dev)  
# Output: 1.247219128924647  
```  
  
#### np.var() - Sales Variance  
```python  
# Daily sales at a shop in Pune  
daily_sales = np.array([5000, 6000, 5500, 7000, 6500])  
  
# Calculate variance  
variance = np.var(daily_sales)  
print("Sales Variance:", variance)  
# Output: 440000.0  
```  
  
#### np.median() - Salary Analysis  
```python  
# Salaries of employees (in thousands)  
salaries = np.array([25, 30, 35, 40, 28, 32, 90])  # Note: 90 is outlier  
  
# Calculate median (better than mean for outliers)  
median_salary = np.median(salaries)  
print("Median Salary:", median_salary)  
# Output: 32.0  
```  
  
#### np.percentile() - Student Performance  
```python  
# Marks of 20 students  
marks = np.array([45, 67, 89, 56, 78, 92, 65, 70, 85, 60,   
                  55, 75, 80, 88, 72, 95, 50, 82, 77, 90])  
  
# Calculate 75th percentile (top 25% threshold)  
percentile_75 = np.percentile(marks, 75)  
print("75th Percentile:", percentile_75)  
# Output: 85.75  
```  
  
---  
  
### 3. Sorting and Ordering  
  
#### np.sort() - Rank Students by Marks  
```python  
# Student marks (unsorted)  
marks = np.array([78, 92, 65, 88, 71, 95, 82])  
  
# Sort marks in ascending order  
sorted_marks = np.sort(marks)  
print("Sorted Marks:", sorted_marks)  
# Output: [65 71 78 82 88 92 95]  
```  
  
#### np.argsort() - Get Student Positions  
```python  
# Marks of Suresh, Ramesh, Mahesh, Dinesh, Mukesh  
students = ["Suresh", "Ramesh", "Mahesh", "Dinesh", "Mukesh"]  
marks = np.array([78, 92, 65, 88, 71])  
  
# Get indices that would sort the array  
positions = np.argsort(marks)  
print("Ranking Order (indices):", positions)  
# Output: [2 4 0 3 1]  
# Means: Mahesh (65) < Mukesh (71) < Suresh (78) < Dinesh (88) < Ramesh (92)  
  
# Show students in rank order  
print("\nRank Order:")  
for rank, idx in enumerate(positions[::-1], 1):  # Reverse for highest first  
    print(f"Rank {rank}: {students[idx]} - {marks[idx]} marks")  
```  
  
**Output:**  
```  
Rank 1: Ramesh - 92 marks  
Rank 2: Dinesh - 88 marks  
Rank 3: Suresh - 78 marks  
Rank 4: Mukesh - 71 marks  
Rank 5: Mahesh - 65 marks  
```  
  
#### np.unique() - Find Unique Orders  
```python  
# Product IDs in orders (some products ordered multiple times)  
order_ids = np.array([101, 203, 101, 305, 203, 407, 101, 305])  
  
# Find unique product IDs  
unique_products = np.unique(order_ids)  
print("Unique Product IDs:", unique_products)  
# Output: [101 203 305 407]  
print("Total Unique Products:", len(unique_products))  
# Output: 4  
```  
  
---  
  
### 4. Aggregation Operations  
  
#### np.sum() - Total Sales Calculation  
```python  
# Daily sales for a week  
daily_sales = np.array([5000, 6000, 5500, 7000, 6500, 8000, 9000])  
  
# Calculate total weekly sales  
total_sales = np.sum(daily_sales)  
print("Total Weekly Sales:", total_sales)  
# Output: 47000  
  
# For 2D array (multiple weeks)  
weekly_sales = np.array([  
    [5000, 6000, 5500, 7000, 6500, 8000, 9000],  # Week 1  
    [5200, 6100, 5800, 7200, 6600, 8200, 9200]   # Week 2  
])  
  
# Sum along axis 1 (row-wise - each week's total)  
week_totals = np.sum(weekly_sales, axis=1)  
print("Week-wise Totals:", week_totals)  
# Output: [47000 48300]  
  
# Sum along axis 0 (column-wise - each day's total across weeks)  
day_totals = np.sum(weekly_sales, axis=0)  
print("Day-wise Totals:", day_totals)  
# Output: [10200 12100 11300 14200 13100 16200 18200]  
```  
  
#### np.cumsum() - Running Total of Expenses  
```python  
# Monthly expenses (in rupees)  
monthly_expenses = np.array([15000, 18000, 16000, 20000, 17000, 19000])  
  
# Calculate cumulative sum (running total)  
cumulative = np.cumsum(monthly_expenses)  
print("Month-wise Cumulative Expenses:")  
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]  
for month, expense, total in zip(months, monthly_expenses, cumulative):  
    print(f"{month}: ₹{expense} (Total so far: ₹{total})")  
```  
  
**Output:**  
```  
Jan: ₹15000 (Total so far: ₹15000)  
Feb: ₹18000 (Total so far: ₹33000)  
Mar: ₹16000 (Total so far: ₹49000)  
Apr: ₹20000 (Total so far: ₹69000)  
May: ₹17000 (Total so far: ₹86000)  
Jun: ₹19000 (Total so far: ₹105000)  
```  
  
---  
  
### 5. Value Limiting  
  
#### np.clip() - Normalize Ratings  
```python  
# User ratings (some invalid values outside 1-5 range)  
ratings = np.array([3, 7, 2, -1, 5, 8, 4, 0, 6, 3])  
  
# Clip ratings to valid range (1 to 5)  
valid_ratings = np.clip(ratings, 1, 5)  
print("Original Ratings:", ratings)  
print("Valid Ratings (1-5):", valid_ratings)  
# Output: [3 5 2 1 5 5 4 1 5 3]  
```  
  
**Real Example - LIC Premium Cap:**  
```python  
# Proposed insurance premiums  
proposed_premiums = np.array([5000, 8000, 15000, 25000, 35000])  
  
# Company policy: Min ₹10,000, Max ₹30,000  
final_premiums = np.clip(proposed_premiums, 10000, 30000)  
print("Proposed Premiums:", proposed_premiums)  
print("Final Premiums (capped):", final_premiums)  
# Output: [10000 10000 15000 25000 30000]  
```  
  
---  
  
## Comparison: NumPy vs Regular Python  
  
### Speed Comparison  
```python  
import numpy as np  
import time  
  
# Create large datasets  
size = 1000000  
list1 = list(range(size))  
list2 = list(range(size))  
arr1 = np.array(list1)  
arr2 = np.array(list2)  
  
# Regular Python addition  
start = time.time()  
result_list = [a + b for a, b in zip(list1, list2)]  
python_time = time.time() - start  
  
# NumPy addition  
start = time.time()  
result_numpy = np.add(arr1, arr2)  
numpy_time = time.time() - start  
  
print(f"Python List: {python_time:.6f} seconds")  
print(f"NumPy Array: {numpy_time:.6f} seconds")  
print(f"NumPy is {python_time/numpy_time:.2f}x faster")  
```  
  
**Typical Output:**  
```  
Python List: 0.125000 seconds  
NumPy Array: 0.003000 seconds  
NumPy is 41.67x faster  
```  
  
---  
  
## Key Takeaways  
  
1. **NumPy is Fast:** Operations are 10-100x faster than regular Python for numerical data  
2. **Vectorized Operations:** No need for loops - operations work on entire arrays  
3. **Memory Efficient:** NumPy arrays use less memory than Python lists  
4. **Rich Functionality:** Built-in statistical and mathematical functions  
5. **Industry Standard:** Used in data science, machine learning, scientific computing  
  
---  
  
## When to Use NumPy Methods  
  
**Use NumPy when:**  
- Working with numerical data (integers, floats)  
- Need fast mathematical operations  
- Processing large datasets  
- Performing statistical analysis  
- Building data science or ML applications  
  
**Use Regular Python when:**  
- Working with mixed data types  
- Small datasets (< 1000 elements)  
- String manipulation  
- Simple calculations where performance doesn't matter  
  
---  
  
## Practice Exercise  
  
Try solving this problem using NumPy methods:  
  
**Problem:** A teacher has marks of 30 students. Calculate:  
1. Average marks  
2. Median marks  
3. Standard deviation  
4. Number of students above 75th percentile  
5. Sort students by marks (descending)  
  
```python  
import numpy as np  
  
# Student marks  
marks = np.array([78, 92, 65, 88, 71, 95, 82, 76, 89, 67,   
                  85, 79, 91, 74, 68, 84, 77, 93, 81, 86,  
                  72, 90, 75, 87, 83, 73, 94, 80, 70, 88])  
  
# Your solution here  
```