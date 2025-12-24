# Matplotlib Fundamentals for Beginners    
## 2-Hour Complete Learning Guide    
    
### What You'll Learn Today    
By the end of this session, you will be able to create professional charts and graphs to visualize your data - converting numbers into meaningful pictures that tell stories at a glance.    
    
---    
    
## Part 1: Introduction to Matplotlib (15 minutes)    
    
### Why Matplotlib?    
    
Remember the saying "A picture is worth a thousand words"? In data analysis, a chart is worth a thousand numbers. Matplotlib helps you:    
- Visualize trends and patterns    
- Present data in reports and presentations    
- Spot anomalies and outliers quickly    
- Make data-driven decisions faster    
    
**Matplotlib = Mathematical Plotting Library** - the foundation for data visualization in Python.    
    
### Real-World Scenario    
    
You analyzed Flipkart sales data using Pandas. Now you need to show your manager which cities are performing best. Instead of showing a table with 50 rows, you create a bar chart that shows top 5 cities instantly. That's the power of visualization.    
    
### Installation    
    
```python    
python3 -m venv myenv
# windows
myenv/Scripts/activate
# mac/linux
source myenv/bin/activate
pip install matplotlib    
```    
    
### Your First Chart    
    
```python    
import matplotlib.pyplot as plt    
    
# Sales data for 5 days    
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']    
sales = [120, 150, 130, 180, 160]    
    
# Create line chart    
plt.plot(days, sales)    
plt.title('Weekly Sales')    
plt.xlabel('Days')    
plt.ylabel('Sales (in thousands)')    
plt.show()    
```    
    
**Understanding the Code:**    
- `plt.plot()` - Creates the line    
- `plt.title()` - Adds chart title    
- `plt.xlabel()` - Label for x-axis    
- `plt.ylabel()` - Label for y-axis    
- `plt.show()` - Displays the chart    
    
---    
    
## Part 2: Line Charts (20 minutes)    
    
### Basic Line Chart    
    
Line charts show trends over time - perfect for sales, temperature, stock prices, etc.    
    
```python    
import matplotlib.pyplot as plt    
    
# Monthly sales for a Chennai shop (in lakhs)    
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']    
sales = [4.5, 5.2, 4.8, 6.1, 5.5, 6.8]    
    
plt.plot(months, sales)    
plt.title('Monthly Sales Trend - Chennai Shop')    
plt.xlabel('Months')    
plt.ylabel('Sales (in Lakhs)')    
plt.grid(True)  # Add grid for better readability    
plt.show()    
```    
    
### Customizing Line Charts    
    
```python    
# Indian Railways passenger count (in lakhs)    
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']    
passengers = [85, 92, 88, 95, 90, 98]    
    
plt.plot(months, passengers,     
         color='blue',           # Line color    
         linewidth=2,            # Line thickness    
         marker='o',             # Add markers at data points    
         markersize=8,           # Marker size    
         linestyle='--')         # Dashed line    
    
plt.title('Monthly Passenger Count - Indian Railways', fontsize=14, fontweight='bold')    
plt.xlabel('Months', fontsize=12)    
plt.ylabel('Passengers (in Lakhs)', fontsize=12)    
plt.grid(True, alpha=0.3)  # Transparent grid    
plt.show()    
```    
    
### Multiple Lines in One Chart    
    
```python    
# Comparing two shops    
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']    
pune_sales = [45, 52, 48, 61, 55, 68]    
mumbai_sales = [50, 48, 55, 58, 62, 65]    
    
plt.plot(months, pune_sales, label='Pune', marker='o', linewidth=2)    
plt.plot(months, mumbai_sales, label='Mumbai', marker='s', linewidth=2)    
    
plt.title('Sales Comparison: Pune vs Mumbai')    
plt.xlabel('Months')    
plt.ylabel('Sales (in thousands)')    
plt.legend()  # Show legend    
plt.grid(True, alpha=0.3)    
plt.show()    
```    
    
---    
    
## Part 3: Bar Charts (20 minutes)    
    
### Vertical Bar Chart    
    
Bar charts compare quantities across categories - perfect for comparing cities, products, departments, etc.    
    
```python    
import matplotlib.pyplot as plt    
    
# Top 5 cities by sales    
cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Pune']    
revenue = [125, 110, 98, 85, 92]  # in lakhs    
    
plt.bar(cities, revenue, color='steelblue')    
plt.title('Top 5 Cities by Revenue')    
plt.xlabel('Cities')    
plt.ylabel('Revenue (in Lakhs)')    
plt.show()    
```    
    
### Horizontal Bar Chart    
    
```python    
# Employee performance ratings    
employees = ['Suresh', 'Ramesh', 'Mahesh', 'Dinesh', 'Mukesh']    
ratings = [4.2, 4.8, 4.5, 4.9, 4.3]    
    
plt.barh(employees, ratings, color='coral')    
plt.title('Employee Performance Ratings')    
plt.xlabel('Rating (out of 5)')    
plt.ylabel('Employees')    
plt.xlim(0, 5)  # Set x-axis limit    
plt.show()    
```    
    
### Customizing Bar Colors    
    
```python    
# Category-wise sales    
categories = ['Electronics', 'Fashion', 'Home', 'Books', 'Grocery']    
sales = [145, 120, 85, 65, 95]    
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']    
    
plt.bar(categories, sales, color=colors)    
plt.title('Sales by Category - Flipkart')    
plt.xlabel('Categories')    
plt.ylabel('Sales (in Lakhs)')    
plt.xticks(rotation=45)  # Rotate labels    
plt.tight_layout()  # Prevent label cutoff    
plt.show()    
```    
    
### Grouped Bar Chart    
    
```python    
import numpy as np    
    
# Quarterly sales for 3 products    
categories = ['Q1', 'Q2', 'Q3', 'Q4']    
product_a = [45, 52, 48, 61]    
product_b = [38, 45, 42, 55]    
product_c = [42, 48, 45, 58]    
    
x = np.arange(len(categories))    
width = 0.25    
    
plt.bar(x - width, product_a, width, label='Product A', color='#FF6B6B')    
plt.bar(x, product_b, width, label='Product B', color='#4ECDC4')    
plt.bar(x + width, product_c, width, label='Product C', color='#45B7D1')    
    
plt.xlabel('Quarters')    
plt.ylabel('Sales (in thousands)')    
plt.title('Quarterly Sales Comparison')    
plt.xticks(x, categories)    
plt.legend()    
plt.show()    
```    
    
---    
    
## Part 4: Pie Charts (15 minutes)    
    
### Basic Pie Chart    
    
Pie charts show parts of a whole - perfect for market share, budget distribution, etc.    
    
```python    
import matplotlib.pyplot as plt    
    
# Market share of mobile brands in India    
brands = ['Samsung', 'Xiaomi', 'Vivo', 'Oppo', 'Others']    
market_share = [22, 25, 18, 15, 20]    
    
plt.pie(market_share, labels=brands, autopct='%1.1f%%')    
plt.title('Mobile Phone Market Share - India')    
plt.show()    
```    
    
### Enhanced Pie Chart    
    
```python    
# Monthly expense breakdown    
categories = ['Food', 'Rent', 'Transport', 'Shopping', 'Bills', 'Savings']    
expenses = [8000, 15000, 3000, 5000, 4000, 10000]    
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#96CEB4']    
    
# Explode the largest slice (Rent)    
explode = (0, 0.1, 0, 0, 0, 0)    
    
plt.pie(expenses,     
        labels=categories,     
        autopct='%1.1f%%',    
        startangle=90,    
        colors=colors,    
        explode=explode,    
        shadow=True)    
    
plt.title('Monthly Expense Distribution - Rs. 45,000')    
plt.axis('equal')  # Equal aspect ratio ensures circular pie    
plt.show()    
```    
    
---    
    
## Part 5: Scatter Plots (15 minutes)    
    
### Basic Scatter Plot    
    
Scatter plots show relationships between two variables - perfect for finding correlations.    
    
```python    
import matplotlib.pyplot as plt    
    
# Relationship between study hours and exam marks    
study_hours = [2, 3, 4, 5, 6, 7, 8, 3, 5, 6, 7, 4, 8, 2, 5]    
marks = [45, 55, 60, 70, 75, 80, 90, 50, 68, 72, 85, 62, 92, 48, 70]    
    
plt.scatter(study_hours, marks, color='purple', s=100, alpha=0.6)    
plt.title('Study Hours vs Exam Marks')    
plt.xlabel('Study Hours per Day')    
plt.ylabel('Marks Obtained')    
plt.grid(True, alpha=0.3)    
plt.show()    
```    
    
### Customized Scatter Plot    
    
```python    
# Employee experience vs salary    
experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 5, 7, 2, 6]    
salary = [25, 28, 32, 35, 40, 45, 50, 55, 60, 65, 30, 42, 52, 27, 48]  # in thousands    
    
plt.scatter(experience, salary,     
            s=200,              # Size of dots    
            c=salary,           # Color based on salary    
            cmap='viridis',     # Color map    
            alpha=0.6,          # Transparency    
            edgecolors='black') # Border color    
    
plt.colorbar(label='Salary (in thousands)')    
plt.title('Experience vs Salary - IT Company')    
plt.xlabel('Years of Experience')    
plt.ylabel('Salary (in thousands)')    
plt.grid(True, alpha=0.3)    
plt.show()    
```    
    
---    
    
## Part 6: Histograms (15 minutes)    
    
### Basic Histogram    
    
Histograms show distribution of data - perfect for age groups, salary ranges, test scores, etc.    
    
```python    
import matplotlib.pyplot as plt    
import numpy as np    
    
# Student marks distribution    
marks = [45, 52, 67, 78, 89, 55, 62, 75, 82, 91, 48, 58, 72, 85, 92,    
         50, 65, 70, 80, 88, 54, 61, 73, 83, 90, 47, 59, 71, 81, 87]    
    
plt.hist(marks, bins=5, color='skyblue', edgecolor='black')    
plt.title('Student Marks Distribution')    
plt.xlabel('Marks Range')    
plt.ylabel('Number of Students')    
plt.grid(True, alpha=0.3)    
plt.show()    
```    
    
### Customized Histogram    
    
```python    
# Employee age distribution in a company    
ages = np.random.normal(32, 8, 100)  # Mean 32, SD 8    
    
plt.hist(ages, bins=10, color='coral', edgecolor='black', alpha=0.7)    
plt.axvline(ages.mean(), color='red', linestyle='--', linewidth=2, label='Mean Age')    
plt.title('Employee Age Distribution')    
plt.xlabel('Age')    
plt.ylabel('Frequency')    
plt.legend()    
plt.grid(True, alpha=0.3)    
plt.show()    
```    
    
---    
    
## Part 7: Subplots (20 minutes)    
    
### Creating Multiple Charts in One Figure    
    
```python    
import matplotlib.pyplot as plt    
import numpy as np    
    
# Create sample data    
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']    
sales = [45, 52, 48, 61, 55, 68]    
expenses = [30, 35, 32, 40, 38, 45]    
profit = [15, 17, 16, 21, 17, 23]    
    
# Create 2 rows, 2 columns of subplots    
fig, axes = plt.subplots(2, 2, figsize=(12, 8))    
    
# Plot 1: Line chart    
axes[0, 0].plot(months, sales, marker='o', color='blue')    
axes[0, 0].set_title('Monthly Sales')    
axes[0, 0].set_ylabel('Sales')    
axes[0, 0].grid(True, alpha=0.3)    
    
# Plot 2: Bar chart    
axes[0, 1].bar(months, expenses, color='red')    
axes[0, 1].set_title('Monthly Expenses')    
axes[0, 1].set_ylabel('Expenses')    
    
# Plot 3: Area chart    
axes[1, 0].fill_between(months, profit, color='green', alpha=0.3)    
axes[1, 0].plot(months, profit, color='green', marker='s')    
axes[1, 0].set_title('Monthly Profit')    
axes[1, 0].set_ylabel('Profit')    
axes[1, 0].grid(True, alpha=0.3)    
    
# Plot 4: Pie chart    
categories = ['Sales', 'Expenses', 'Profit']    
values = [sum(sales), sum(expenses), sum(profit)]    
axes[1, 1].pie(values, labels=categories, autopct='%1.1f%%')    
axes[1, 1].set_title('Overall Distribution')    
    
plt.tight_layout()    
plt.show()    
```    
    
---    
    
## Part 8: Real-World Project (25 minutes)    
    
### Project: Complete Sales Dashboard    
    
```python    
import matplotlib.pyplot as plt    
import numpy as np    
    
# Generate sample data for a retail chain    
np.random.seed(42)    
    
# Monthly data    
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']    
total_sales = [450, 520, 480, 610, 550, 680, 720, 650, 700, 750, 800, 850]    
    
# City-wise sales (last month)    
cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Pune', 'Hyderabad']    
city_sales = [180, 165, 142, 128, 145, 135]    
    
# Category-wise distribution    
categories = ['Electronics', 'Fashion', 'Home', 'Grocery', 'Books']    
category_sales = [280, 240, 180, 220, 130]    
    
# Customer age distribution    
customer_ages = np.random.normal(35, 12, 500)    
    
# Create comprehensive dashboard    
fig = plt.figure(figsize=(16, 10))    
    
# Main title    
fig.suptitle('RETAIL CHAIN - ANNUAL SALES DASHBOARD 2024',     
             fontsize=20, fontweight='bold', y=0.98)    
    
# Chart 1: Monthly Sales Trend (Top, Full Width)    
ax1 = plt.subplot(2, 3, (1, 3))    
ax1.plot(months, total_sales, marker='o', linewidth=3, color='#2E86AB', markersize=8)    
ax1.fill_between(months, total_sales, alpha=0.3, color='#2E86AB')    
ax1.set_title('Monthly Sales Trend (in Lakhs)', fontsize=14, fontweight='bold', pad=10)    
ax1.set_ylabel('Sales (Lakhs)', fontsize=11)    
ax1.grid(True, alpha=0.3)    
ax1.axhline(y=np.mean(total_sales), color='red', linestyle='--',     
            linewidth=2, label=f'Average: ₹{np.mean(total_sales):.0f}L')    
ax1.legend()    
    
# Chart 2: City-wise Performance    
ax2 = plt.subplot(2, 3, 4)    
colors_cities = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#96CEB4']    
ax2.barh(cities, city_sales, color=colors_cities)    
ax2.set_title('City-wise Sales (Dec 2024)', fontsize=12, fontweight='bold')    
ax2.set_xlabel('Sales (Lakhs)')    
ax2.invert_yaxis()    
    
# Chart 3: Category Distribution    
ax3 = plt.subplot(2, 3, 5)    
colors_cat = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']    
explode = (0.05, 0, 0, 0, 0)    
ax3.pie(category_sales, labels=categories, autopct='%1.1f%%',    
        colors=colors_cat, explode=explode, shadow=True, startangle=90)    
ax3.set_title('Sales by Category', fontsize=12, fontweight='bold')    
    
# Chart 4: Customer Demographics    
ax4 = plt.subplot(2, 3, 6)    
ax4.hist(customer_ages, bins=15, color='#6C5CE7', edgecolor='black', alpha=0.7)    
ax4.axvline(customer_ages.mean(), color='red', linestyle='--',     
            linewidth=2, label=f'Mean: {customer_ages.mean():.1f} years')    
ax4.set_title('Customer Age Distribution', fontsize=12, fontweight='bold')    
ax4.set_xlabel('Age')    
ax4.set_ylabel('Number of Customers')    
ax4.legend()    
ax4.grid(True, alpha=0.3)    
    
# Add summary statistics as text    
summary_text = f"""    
YEAR SUMMARY 2024    
━━━━━━━━━━━━━━━━━━━━    
Total Revenue: ₹{sum(total_sales)} Lakhs    
Avg Monthly: ₹{np.mean(total_sales):.0f} Lakhs    
Best Month: {months[np.argmax(total_sales)]} (₹{max(total_sales)}L)    
Growth: {((total_sales[-1] - total_sales[0]) / total_sales[0] * 100):.1f}%    
Top City: {cities[np.argmax(city_sales)]}    
"""    
    
plt.figtext(0.02, 0.02, summary_text, fontsize=10,     
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),    
            family='monospace')    
    
plt.tight_layout(rect=[0, 0.05, 1, 0.96])    
plt.savefig('sales_dashboard.png', dpi=300, bbox_inches='tight')    
plt.show()    
    
print("Dashboard created successfully!")    
print(f"Total Annual Revenue: Rs. {sum(total_sales)} Lakhs")    
```    
    
---    
    
## Part 9: Saving Charts (10 minutes)    
    
### Saving Charts as Images    
    
```python    
import matplotlib.pyplot as plt    
    
# Create a simple chart    
cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Pune']    
sales = [125, 110, 98, 85, 92]    
    
plt.figure(figsize=(10, 6))    
plt.bar(cities, sales, color='steelblue')    
plt.title('City-wise Sales Report')    
plt.xlabel('Cities')    
plt.ylabel('Sales (in Lakhs)')    
    
# Save as PNG (high quality)    
plt.savefig('sales_report.png', dpi=300, bbox_inches='tight')    
    
# Save as PDF (for printing)    
plt.savefig('sales_report.pdf', bbox_inches='tight')    
    
# Save as JPG    
plt.savefig('sales_report.jpg', dpi=150, bbox_inches='tight')    
    
plt.show()    
print("Charts saved successfully!")    
```    
    
---    
    
## Quick Reference Cheat Sheet    
    
```python    
import matplotlib.pyplot as plt    
    
# LINE CHART    
plt.plot(x, y)    
plt.plot(x, y, color='blue', linewidth=2, marker='o', linestyle='--')    
    
# BAR CHART    
plt.bar(categories, values)           # Vertical    
plt.barh(categories, values)          # Horizontal    
    
# PIE CHART    
plt.pie(values, labels=labels, autopct='%1.1f%%')    
    
# SCATTER PLOT    
plt.scatter(x, y, s=100, c='red', alpha=0.6)    
    
# HISTOGRAM    
plt.hist(data, bins=10, color='skyblue')    
    
# LABELS AND TITLES    
plt.title('Chart Title')    
plt.xlabel('X Label')    
plt.ylabel('Y Label')    
plt.legend()    
    
# CUSTOMIZATION    
plt.grid(True)    
plt.xlim(0, 100)    
plt.ylim(0, 100)    
plt.xticks(rotation=45)    
    
# SUBPLOTS    
fig, ax = plt.subplots(2, 2)          # 2x2 grid    
ax[0, 0].plot(x, y)    
    
# SAVE    
plt.savefig('chart.png', dpi=300)    
    
# SHOW    
plt.show()    
```    
    
---    
    
## Quiz Time    
    
### Question 1    
Which function creates a line chart?    
    
A) plt.line()      
B) plt.plot()      
C) plt.chart()      
D) plt.draw()      
    
**Answer: B** - plt.plot() creates line charts.    
    
### Question 2    
How do you add a title to a chart?    
    
A) plt.header('Title')      
B) plt.name('Title')      
C) plt.title('Title')      
D) plt.heading('Title')      
    
**Answer: C** - plt.title() adds chart title.    
    
### Question 3    
Which chart type shows parts of a whole?    
    
A) Line chart      
B) Bar chart      
C) Pie chart      
D) Scatter plot      
    
**Answer: C** - Pie charts show proportions.    
    
### Question 4    
How do you save a chart as PNG?    
    
A) plt.save('file.png')      
B) plt.export('file.png')      
C) plt.savefig('file.png')      
D) plt.write('file.png')      
    
**Answer: C** - plt.savefig() saves charts.    
    
### Question 5    
What does `plt.grid(True)` do?    
    
A) Creates a table      
B) Adds gridlines to chart      
C) Splits chart into sections      
D) Changes background color      
    
**Answer: B** - Adds gridlines for better readability.    
    
---    
    
## Mini Assignments    
    
### Assignment 1: Monthly Temperature Chart    
Create a line chart showing temperature variation for 12 months in Chennai. Include:    
- Average temperature line    
- Grid for readability    
- Proper labels and title    
- Save as PNG    
    
### Assignment 2: Product Sales Comparison    
Create a grouped bar chart comparing sales of 4 products across 4 quarters. Include:    
- Different colors for each product    
- Legend    
- Rotated x-axis labels    
- Save as PDF    
    
### Assignment 3: Expense Pie Chart    
Create a pie chart for monthly expenses with 6 categories. Include:    
- Percentage labels    
- Explode the largest expense    
- Custom colors    
- Shadow effect    
    
### Assignment 4: Student Performance Scatter    
Create a scatter plot showing relationship between attendance percentage and final marks for 30 students. Include:    
- Color gradient based on marks    
- Grid    
- Proper axis labels    
    
### Assignment 5: Complete Dashboard    
Create a 2x2 dashboard with:    
- Top left: Line chart (monthly sales)    
- Top right: Bar chart (city-wise sales)    
- Bottom left: Pie chart (category distribution)    
- Bottom right: Histogram (customer age)    
Save as high-resolution image.    
    
---    
    
## Key Takeaways    
    
1. Choose the right chart for your data type    
2. Line charts for trends, bar for comparisons, pie for proportions    
3. Always add titles, labels, and legends    
4. Use colors and customization to make charts professional    
5. Save charts in appropriate formats for sharing    
    
## Next Steps    
    
You have now mastered the complete data analysis stack:    
- **NumPy**: Fast numerical operations    
- **Pandas**: Data manipulation and analysis    
- **Matplotlib**: Data visualization    
    
**Practice by combining all three**: Read CSV with Pandas, analyze with NumPy, visualize with Matplotlib.    
    
---    
    
## Bonus: Integration Example    
    
```python    
import pandas as pd    
import matplotlib.pyplot as plt    
    
# Read CSV file    
df = pd.read_csv('sales.csv')    
    
# Analyze with Pandas    
city_sales = df.groupby('City')['Amount'].sum()    
    
# Visualize with Matplotlib    
plt.figure(figsize=(10, 6))    
plt.bar(city_sales.index, city_sales.values, color='steelblue')    
plt.title('City-wise Sales Analysis')    
plt.xlabel('Cities')    
plt.ylabel('Total Sales')    
plt.xticks(rotation=45)    
plt.tight_layout()    
plt.savefig('analysis_report.png', dpi=300)    
plt.show()    
```    
    
**This is how professionals work with data - combining multiple tools for complete analysis.**