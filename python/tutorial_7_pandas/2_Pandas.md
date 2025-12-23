# Pandas Fundamentals for Beginners    
## 2-Hour Complete Learning Guide    
    
### What You'll Learn Today    
By the end of this session, you will be able to read data files, clean data, filter records, perform calculations, and generate reports using Pandas - just like working with Excel but more powerful.    
    
---    
    
## Part 1: Introduction to Pandas (15 minutes)    
    
### Why Pandas?    
    
Remember working with Excel sheets? Pandas is like Excel on steroids. You can:    
- Handle millions of rows (Excel struggles after 1 lakh rows)    
- Automate repetitive tasks    
- Clean messy data easily    
- Perform complex analysis with simple commands    
    
**Pandas = Panel Data** - designed for working with structured data like tables, CSV files, Excel sheets, and databases.    
    
### Real-World Scenario    
    
You work at Flipkart and receive a CSV file with 2 lakh order records daily. Using Pandas, you can analyze sales, find trends, and generate reports in seconds instead of manually working in Excel for hours.    
    
### Installation    
    
```python    
pip install pandas    
```    
    
### Core Data Structures    
    
Pandas has two main structures:    
1. **Series** - Single column of data (like one Excel column)    
2. **DataFrame** - Table with rows and columns (like entire Excel sheet)    
    
```python    
import pandas as pd    
    
# Series - Think of it as one Excel column    
cities = pd.Series(['Mumbai', 'Delhi', 'Chennai', 'Pune', 'Bangalore'])    
print("Cities Series:")    
print(cities)    
    
# DataFrame - Think of it as Excel table    
employee_data = pd.DataFrame({    
    'Name': ['Suresh', 'Ramesh', 'Mahesh', 'Dinesh'],    
    'Age': [25, 28, 24, 27],    
    'City': ['Pune', 'Mumbai', 'Chennai', 'Delhi'],    
    'Salary': [35000, 42000, 38000, 45000]    
})    
print("\nEmployee DataFrame:")    
print(employee_data)    
```    
    
---    
    
## Part 2: Creating DataFrames (20 minutes)    
    
### Method 1: From Dictionary    
    
```python    
import pandas as pd    
    
# Product inventory for a shop    
inventory = pd.DataFrame({    
    'Product': ['Rice', 'Wheat', 'Sugar', 'Oil', 'Dal'],    
    'Quantity': [50, 40, 30, 25, 35],    
    'Price': [45, 40, 42, 120, 85],    
    'Category': ['Grains', 'Grains', 'Grocery', 'Grocery', 'Grains']    
})    
    
print(inventory)    
```    
    
### Method 2: From Lists    
    
```python    
# Student records    
students = [    
    ['Suresh', 85, 'A'],    
    ['Ramesh', 92, 'A+'],    
    ['Mahesh', 78, 'B'],    
    ['Dinesh', 88, 'A']    
]    
    
df_students = pd.DataFrame(students, columns=['Name', 'Marks', 'Grade'])    
print(df_students)    
```    
    
### Method 3: From CSV File (Most Common)    
    
```python    
# Reading CSV file    
# Assume we have orders.csv file    
df = pd.read_csv('orders.csv')    
print(df.head())  # Shows first 5 rows    
    
# Read Excel file    
df_excel = pd.read_excel('sales.xlsx')    
```    
    
### Quick Data Inspection    
    
```python    
# First 5 rows    
print(inventory.head())    
    
# Last 5 rows    
print(inventory.tail())    
    
# Basic information    
print(inventory.info())    
    
# Statistical summary    
print(inventory.describe())    
    
# Column names    
print(inventory.columns)    
    
# Shape (rows, columns)    
print(inventory.shape)    
```    
    
---    
    
## Part 3: Selecting and Filtering Data (25 minutes)    
    
### Selecting Columns    
    
```python    
# Create sample data    
sales_data = pd.DataFrame({    
    'Order_ID': [1001, 1002, 1003, 1004, 1005],    
    'Customer': ['Mukesh', 'Nitesh', 'Hitesh', 'Ratnesh', 'Himesh'],    
    'City': ['Pune', 'Mumbai', 'Chennai', 'Delhi', 'Bangalore'],    
    'Amount': [2500, 3200, 1800, 4100, 2900],    
    'Status': ['Delivered', 'Pending', 'Delivered', 'Delivered', 'Cancelled']    
})    
    
# Select single column    
print(sales_data['Customer'])    
    
# Select multiple columns    
print(sales_data[['Customer', 'Amount']])    
```    
    
### Selecting Rows    
    
```python    
# Select by index position    
print(sales_data.iloc[0])  # First row    
    
# Select multiple rows    
print(sales_data.iloc[0:3])  # First 3 rows    
    
# Select by condition (filtering)    
high_value = sales_data[sales_data['Amount'] > 3000]    
print("High value orders:")    
print(high_value)    
    
# Multiple conditions    
pune_delivered = sales_data[    
    (sales_data['City'] == 'Pune') &     
    (sales_data['Status'] == 'Delivered')    
]    
print("Pune delivered orders:")    
print(pune_delivered)    
```    
    
### Practical Filtering Examples    
    
```python    
# LIC Policy holders data    
policies = pd.DataFrame({    
    'Policy_No': [1001, 1002, 1003, 1004, 1005, 1006],    
    'Holder': ['Suresh', 'Ramesh', 'Mahesh', 'Dinesh', 'Mukesh', 'Nitesh'],    
    'Age': [28, 35, 42, 29, 38, 45],    
    'Premium': [5000, 7500, 6000, 5500, 8000, 9000],    
    'City': ['Chennai', 'Mumbai', 'Pune', 'Delhi', 'Bangalore', 'Chennai']    
})    
    
# Filter: Age above 35    
senior = policies[policies['Age'] > 35]    
print("Senior policy holders:")    
print(senior)    
    
# Filter: Premium between 6000 and 8000    
mid_range = policies[    
    (policies['Premium'] >= 6000) &     
    (policies['Premium'] <= 8000)    
]    
print("\nMid-range premiums:")    
print(mid_range)    
    
# Filter: Chennai customers only    
chennai = policies[policies['City'] == 'Chennai']    
print("\nChennai customers:")    
print(chennai)    
```    
    
---    
    
## Part 4: Data Manipulation (30 minutes)    
    
### Adding New Columns    
    
```python    
# Employee salary data    
employees = pd.DataFrame({    
    'Name': ['Suresh', 'Ramesh', 'Mahesh', 'Dinesh'],    
    'Basic_Salary': [30000, 35000, 32000, 38000],    
    'Experience': [2, 5, 3, 6]    
})    
    
# Add HRA (30% of basic)    
employees['HRA'] = employees['Basic_Salary'] * 0.30    
    
# Add DA (20% of basic)    
employees['DA'] = employees['Basic_Salary'] * 0.20    
    
# Calculate total salary    
employees['Total_Salary'] = employees['Basic_Salary'] + employees['HRA'] + employees['DA']    
    
print(employees)    
```    
    
### Updating Values    
    
```python    
# Update specific value    
employees.loc[0, 'Basic_Salary'] = 32000    
    
# Update based on condition    
# Give 10% increment to employees with experience > 4 years    
employees.loc[employees['Experience'] > 4, 'Basic_Salary'] *= 1.10    
    
print(employees)    
```    
    
### Deleting Columns/Rows    
    
```python    
# Delete column    
employees_copy = employees.copy()    
employees_copy = employees_copy.drop('DA', axis=1)    
    
# Delete row by index    
employees_copy = employees_copy.drop(0, axis=0)    
    
print(employees_copy)    
```    
    
### Sorting Data    
    
```python    
# Sort by salary (ascending)    
sorted_asc = employees.sort_values('Total_Salary')    
print("Lowest to highest salary:")    
print(sorted_asc)    
    
# Sort by salary (descending)    
sorted_desc = employees.sort_values('Total_Salary', ascending=False)    
print("\nHighest to lowest salary:")    
print(sorted_desc)    
```    
    
---    
    
## Part 5: GroupBy and Aggregation (25 minutes)    
    
### Understanding GroupBy    
    
GroupBy is like creating pivot tables in Excel. It groups similar data and performs calculations.    
    
```python    
# Sales data for multiple cities    
sales = pd.DataFrame({    
    'City': ['Pune', 'Mumbai', 'Pune', 'Chennai', 'Mumbai', 'Pune', 'Chennai'],    
    'Product': ['Laptop', 'Mobile', 'Mobile', 'Laptop', 'Laptop', 'Tablet', 'Mobile'],    
    'Amount': [45000, 25000, 22000, 48000, 46000, 30000, 24000],    
    'Quantity': [1, 2, 1, 1, 1, 2, 1]    
})    
    
# Group by city and calculate total sales    
city_sales = sales.groupby('City')['Amount'].sum()    
print("Total sales by city:")    
print(city_sales)    
    
# Multiple aggregations    
city_summary = sales.groupby('City').agg({    
    'Amount': ['sum', 'mean', 'count'],    
    'Quantity': 'sum'    
})    
print("\nCity-wise summary:")    
print(city_summary)    
```    
    
### Real Example: Indian Railways Booking Analysis    
    
```python    
# Railway bookings data    
bookings = pd.DataFrame({    
    'Train_No': ['12345', '12345', '12346', '12346', '12345', '12347'],    
    'Class': ['3AC', 'Sleeper', '2AC', '3AC', 'Sleeper', '3AC'],    
    'Passengers': [2, 4, 1, 3, 2, 2],    
    'Fare': [1500, 800, 2200, 1600, 850, 1550],    
    'From': ['Mumbai', 'Mumbai', 'Delhi', 'Delhi', 'Chennai', 'Pune'],    
    'To': ['Delhi', 'Delhi', 'Chennai', 'Mumbai', 'Bangalore', 'Mumbai']    
})    
    
# Total revenue per train    
train_revenue = bookings.groupby('Train_No')['Fare'].sum()    
print("Revenue per train:")    
print(train_revenue)    
    
# Analysis by class    
class_analysis = bookings.groupby('Class').agg({    
    'Fare': ['sum', 'mean'],    
    'Passengers': 'sum'    
})    
print("\nClass-wise analysis:")    
print(class_analysis)    
    
# Busiest route    
route_analysis = bookings.groupby(['From', 'To']).agg({    
    'Passengers': 'sum',    
    'Fare': 'sum'    
})    
print("\nRoute analysis:")    
print(route_analysis)    
```    
    
---    
    
## Part 6: Handling Missing Data (15 minutes)    
    
### Identifying Missing Values    
    
```python    
# Data with missing values    
student_marks = pd.DataFrame({    
    'Name': ['Suresh', 'Ramesh', 'Mahesh', 'Dinesh', 'Mukesh'],    
    'Math': [85, None, 78, 92, 88],    
    'Science': [90, 88, None, 95, 92],    
    'English': [78, 82, 80, None, 85]    
})    
    
print(student_marks)    
    
# Check for missing values    
print("\nMissing values:")    
print(student_marks.isnull())    
    
# Count missing values per column    
print("\nMissing count:")    
print(student_marks.isnull().sum())    
```    
    
### Handling Missing Values    
    
```python    
# Method 1: Fill with specific value    
filled_zero = student_marks.fillna(0)    
print("Filled with zero:")    
print(filled_zero)    
    
# Method 2: Fill with mean    
filled_mean = student_marks.fillna(student_marks.mean())    
print("\nFilled with mean:")    
print(filled_mean)    
    
# Method 3: Drop rows with missing values    
dropped = student_marks.dropna()    
print("\nDropped missing rows:")    
print(dropped)    
    
# Method 4: Forward fill (use previous value)    
filled_forward = student_marks.fillna(method='ffill')    
print("\nForward filled:")    
print(filled_forward)    
```    
    
---    
    
## Part 7: Real-World Project (20 minutes)    
    
### Project: Flipkart Order Analysis    
    
```python    
import pandas as pd    
import numpy as np    
    
# Create sample Flipkart order data    
np.random.seed(42)    
    
orders = pd.DataFrame({    
    'Order_ID': range(1001, 1051),    
    'Customer': np.random.choice(['Suresh', 'Ramesh', 'Mahesh', 'Dinesh', 'Mukesh'], 50),    
    'City': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Pune'], 50),    
    'Category': np.random.choice(['Electronics', 'Fashion', 'Home', 'Books'], 50),    
    'Amount': np.random.randint(500, 5000, 50),    
    'Status': np.random.choice(['Delivered', 'Pending', 'Cancelled'], 50, p=[0.7, 0.2, 0.1])    
})    
    
print("FLIPKART ORDER ANALYSIS REPORT")    
print("=" * 60)    
    
# 1. Total orders and revenue    
total_orders = len(orders)    
total_revenue = orders['Amount'].sum()    
print(f"\n1. OVERALL STATISTICS")    
print(f"   Total Orders: {total_orders}")    
print(f"   Total Revenue: Rs. {total_revenue:,}")    
print(f"   Average Order Value: Rs. {orders['Amount'].mean():.2f}")    
    
# 2. Status-wise analysis    
print(f"\n2. ORDER STATUS BREAKDOWN")    
status_summary = orders.groupby('Status').agg({    
    'Order_ID': 'count',    
    'Amount': 'sum'    
})    
status_summary.columns = ['Count', 'Revenue']    
print(status_summary)    
    
# 3. City-wise analysis    
print(f"\n3. TOP PERFORMING CITIES")    
city_revenue = orders.groupby('City')['Amount'].sum().sort_values(ascending=False)    
print(city_revenue)    
    
# 4. Category performance    
print(f"\n4. CATEGORY ANALYSIS")    
category_stats = orders.groupby('Category').agg({    
    'Order_ID': 'count',    
    'Amount': ['sum', 'mean']    
})    
category_stats.columns = ['Orders', 'Total_Revenue', 'Avg_Order_Value']    
print(category_stats.sort_values('Total_Revenue', ascending=False))    
    
# 5. Customer analysis    
print(f"\n5. TOP CUSTOMERS")    
customer_spending = orders.groupby('Customer')['Amount'].sum().sort_values(ascending=False)    
print(customer_spending.head())    
    
# 6. High value orders    
print(f"\n6. HIGH VALUE ORDERS (Above Rs. 3000)")    
high_value = orders[orders['Amount'] > 3000]    
print(f"   Count: {len(high_value)}")    
print(f"   Revenue: Rs. {high_value['Amount'].sum():,}")    
    
# 7. Delivered orders in Mumbai    
print(f"\n7. MUMBAI DELIVERED ORDERS")    
mumbai_delivered = orders[    
    (orders['City'] == 'Mumbai') &     
    (orders['Status'] == 'Delivered')    
]    
print(f"   Count: {len(mumbai_delivered)}")    
print(f"   Revenue: Rs. {mumbai_delivered['Amount'].sum():,}")    
    
# Export to CSV    
orders.to_csv('flipkart_orders_analysis.csv', index=False)    
print(f"\n8. Report exported to 'flipkart_orders_analysis.csv'")    
```    
    
---    
    
## Quick Reference Cheat Sheet    
    
```python    
# Reading Data    
pd.read_csv('file.csv')              # Read CSV    
pd.read_excel('file.xlsx')           # Read Excel    
    
# Viewing Data    
df.head()                            # First 5 rows    
df.tail()                            # Last 5 rows    
df.info()                            # Data types and info    
df.describe()                        # Statistical summary    
df.shape                             # (rows, columns)    
    
# Selecting Data    
df['column']                         # Single column    
df[['col1', 'col2']]                # Multiple columns    
df.iloc[0]                           # First row    
df.iloc[0:5]                         # First 5 rows    
df[df['col'] > 100]                 # Filtering    
    
# Adding/Modifying    
df['new_col'] = values              # Add column    
df.loc[0, 'col'] = value            # Update value    
    
# Deleting    
df.drop('col', axis=1)              # Delete column    
df.drop(0, axis=0)                  # Delete row    
    
# Sorting    
df.sort_values('col')               # Sort ascending    
df.sort_values('col', ascending=False)  # Sort descending    
    
# GroupBy    
df.groupby('col')['col2'].sum()     # Group and sum    
df.groupby('col').agg({'col2': ['sum', 'mean']})  # Multiple agg    
    
# Missing Data    
df.isnull()                         # Check missing    
df.isnull().sum()                   # Count missing    
df.fillna(0)                        # Fill with 0    
df.dropna()                         # Drop missing rows    
    
# Export    
df.to_csv('file.csv', index=False)  # Save to CSV    
df.to_excel('file.xlsx', index=False)  # Save to Excel    
```    
    
---    
    
## Quiz Time    
    
### Question 1    
How do you read the first 10 rows of a DataFrame?    
```python    
df = pd.read_csv('data.csv')    
```    
A) df.head(10)      
B) df.first(10)      
C) df.top(10)      
D) df.show(10)      
    
**Answer: A** - head() shows first n rows.    
    
### Question 2    
Which command filters rows where Amount > 5000?    
    
A) df[df.Amount > 5000]      
B) df[Amount > 5000]      
C) df.filter(Amount > 5000)      
D) df.where('Amount' > 5000)      
    
**Answer: A** - Use square brackets with condition.    
    
### Question 3    
How do you find total sales by city?    
```python    
df = pd.DataFrame({'City': [...], 'Sales': [...]})    
```    
A) df.group('City').sum('Sales')      
B) df.groupby('City')['Sales'].sum()      
C) df.sum('City', 'Sales')      
D) df.aggregate('City', 'Sales')      
    
**Answer: B** - groupby() followed by column and aggregation.    
    
### Question 4    
What does `df.isnull().sum()` do?    
    
A) Counts total null values      
B) Counts null values per column      
C) Removes null values      
D) Fills null values      
    
**Answer: B** - Counts missing values in each column.    
    
### Question 5    
How do you add a new column with 10% of Amount?    
    
A) df.new_col = df['Amount'] * 0.1      
B) df['new_col'] = df['Amount'] * 0.1      
C) df.add_column('new_col', df['Amount'] * 0.1)      
D) df.insert('new_col', df['Amount'] * 0.1)      
    
**Answer: B** - Use square bracket notation to add column.    
    
---    
    
## Mini Assignments    
    
### Assignment 1: Student Database    
Create a DataFrame with 10 students containing Name, Roll_No, Math, Science, English marks. Calculate:    
- Total marks for each student    
- Class average per subject    
- Topper in each subject    
- Students who scored above 85% overall    
    
### Assignment 2: Shop Sales Analysis    
Create sales data for a grocery shop with Product, Category, Price, Quantity_Sold. Calculate:    
- Total revenue    
- Revenue by category    
- Top 5 selling products    
- Products with revenue above Rs. 10,000    
    
### Assignment 3: Employee Attendance    
Create attendance data for 20 employees with Name, Department, Days_Present, Days_Absent. Calculate:    
- Attendance percentage for each employee    
- Department-wise average attendance    
- Employees with less than 80% attendance    
- Best and worst performing departments    
    
### Assignment 4: Cricket Scores    
Create IPL match data with Team, Player, Runs, Balls, Fours, Sixes. Calculate:    
- Strike rate for each player (Runs/Balls * 100)    
- Team-wise total runs    
- Players with strike rate above 150    
- Most sixes hit by team    
    
### Assignment 5: Monthly Expenses    
Create expense data with Date, Category (Food, Transport, Shopping, Bills), Amount. Calculate:    
- Total monthly expense    
- Category-wise spending    
- Highest expense day    
- Average daily spending    
- Which category exceeded Rs. 5000    
    
---    
    
## Key Takeaways    
    
1. DataFrames are like Excel tables but more powerful    
2. Use square brackets for filtering: df[condition]    
3. groupby() is your best friend for analysis    
4. Always handle missing data before analysis    
5. Export results using to_csv() or to_excel()    
    
## Next Steps    
    
With Pandas mastery, you can now work with any structured data. Next, learn Matplotlib to visualize your Pandas analysis results with charts and graphs.    
    
**Practice with real CSV files from government websites or download sample datasets to build strong skills.**