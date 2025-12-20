# NumPy for Fast Data Operations  
  
## Introduction to NumPy  
  
Welcome back! Today we'll learn NumPy - Python's powerful library for working with large amounts of numerical data quickly.  
  
**Real-world scenario:** Suresh at Indian Railways needs to analyze 50,000 ticket bookings from last month. Using regular Python lists would take minutes. With NumPy? Just seconds!  
  
---  
  
## Day 3: NumPy Arrays and Basic Operations  
  
### What is NumPy?  
  
NumPy (Numerical Python) is like a super-charged calculator that can handle millions of numbers at once.  
  
**Why NumPy?**  
- **Speed:** 50-100x faster than Python lists  
- **Memory efficient:** Uses less RAM  
- **Built for math:** Easy calculations on entire datasets  
  
### Your First NumPy Array  
  
```python  
import numpy as np  
  
# Regular Python list  
ticket_prices_list = [450, 890, 1200, 350, 670]  
print("Python list:", ticket_prices_list)  
  
# NumPy array  
ticket_prices = np.array([450, 890, 1200, 350, 670])  
print("NumPy array:", ticket_prices)  
print("Type:", type(ticket_prices))  
```  
  
### Creating Arrays from Real Data  
  
```python  
import numpy as np  
  
# Daily passenger count for a week  
passengers_week1 = np.array([12450, 11890, 13200, 10350, 14670, 15890, 13450])  
  
print("Total passengers:", total_passengers)
print("Average per day:", average_passengers)
print("Busiest day:", busiest_day)
print("Quietest day:", quietest_day)
print("Standard deviation:", passengers_week1.std())
print("Variance:", passengers_week1.var())
print("Median passengers:", np.median(passengers_week1))
print("Sorted passenger counts:", np.sort(passengers_week1))
```  
  
**Output:**  
```  
Total passengers: 91900  
Average per day: 13128.571428571428  
Busiest day: 15890  
Quietest day: 10350  
...  
```
  
#### Quick Reference Table  
  
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

### Array Operations - The Power of NumPy  
  
**Scenario:** Dinesh manages pricing. He needs to apply a 10% discount to all Sleeper class tickets.  
  
```python  
import numpy as np  
  
# Original Sleeper class prices (10 bookings)  
sleeper_prices = np.array([450, 520, 480, 500, 470, 490, 510, 460, 530, 495])  
  
# Apply 10% discount to ALL prices at once  
discounted_prices = sleeper_prices * 0.90  
  
print("Original prices:", sleeper_prices)  
print("After 10% discount:", discounted_prices)  
print("Total savings:", (sleeper_prices - discounted_prices).sum())  
```  
  
**Compare with regular Python:**  
```python  
# Without NumPy - need a loop!  
prices = [450, 520, 480, 500, 470, 490, 510, 460, 530, 495]  
discounted = []  
for price in prices:  
    discounted.append(price * 0.90)  
  
# With NumPy - one line!  
prices_np = np.array([450, 520, 480, 500, 470, 490, 510, 460, 530, 495])  
discounted_np = prices_np * 0.90  
```  
  
### Mathematical Operations  
  
```python  
import numpy as np  
  
# Ticket sales for 5 days (different classes)  
general_sales = np.array([1200, 1450, 1300, 1550, 1480])  
sleeper_sales = np.array([850, 920, 880, 950, 910])  
ac_sales = np.array([320, 380, 350, 410, 395])  
  
# Calculate revenue (price per ticket)  
general_revenue = general_sales * 50    # ₹50 per ticket  
sleeper_revenue = sleeper_sales * 150   # ₹150 per ticket  
ac_revenue = ac_sales * 500             # ₹500 per ticket  
  
# Total daily revenue  
total_revenue = general_revenue + sleeper_revenue + ac_revenue  
  
print("Daily Revenue:")  
for day, revenue in enumerate(total_revenue, 1):  
    print(f"Day {day}: ₹{revenue:,}")  
  
print(f"\nWeek Total: ₹{total_revenue.sum():,}")  
print(f"Daily Average: ₹{total_revenue.mean():,.2f}")  
```  
  
### Array Indexing and Slicing  
  
```python  
import numpy as np  
  
# Ticket prices for different routes  
route_prices = np.array([450, 890, 1200, 350, 670, 540, 780, 920, 410, 630])  
  
# Access specific elements  
print("First route price:", route_prices[0])  
print("Fifth route price:", route_prices[4])  
print("Last route price:", route_prices[-1])  
  
# Slicing - get multiple elements  
print("\nFirst 3 routes:", route_prices[:3])  
print("Routes 4 to 7:", route_prices[3:7])  
print("Every alternate route:", route_prices[::2])  
  
# Get routes with price > ₹600  
expensive_routes = route_prices[route_prices > 600]  
print("\nExpensive routes (>₹600):", expensive_routes)  
print("Count:", len(expensive_routes))  
```  
  
### 2D Arrays - Like Excel Spreadsheets  
  
Think of 2D arrays as tables with rows and columns.  
  
```python  
import numpy as np  
  
# Weekly sales: Rows = Days, Columns = [General, Sleeper, AC]  
weekly_sales = np.array([  
    [1200, 850, 320],  # Monday  
    [1450, 920, 380],  # Tuesday  
    [1300, 880, 350],  # Wednesday  
    [1550, 950, 410],  # Thursday  
    [1480, 910, 395],  # Friday  
    [1680, 980, 450],  # Saturday  
    [1590, 940, 430]   # Sunday  
])  
  
print("Shape:", weekly_sales.shape)  # (7 rows, 3 columns)  
print("\nMonday sales:", weekly_sales[0])  
print("Thursday sales:", weekly_sales[3])  
  
# Get all General class sales (first column)  
general_sales = weekly_sales[:, 0]  
print("\nGeneral class daily:", general_sales)  
print("General class total:", general_sales.sum())  
  
# Get Friday sales (row 4, all columns)  
friday_sales = weekly_sales[4, :]  
print("\nFriday sales:", friday_sales)  
```  
  
---  
  
## Day 4: Advanced NumPy Operations  
  
### Statistical Analysis  
  
```python  
import numpy as np  
  
# Mukesh analyzes last month's daily revenue (30 days)  
daily_revenue = np.array([  
    145000, 152000, 138000, 160000, 155000, 142000, 148000,  
    159000, 168000, 175000, 162000, 158000, 151000, 147000,  
    172000, 181000, 165000, 170000, 163000, 156000, 149000,  
    167000, 178000, 185000, 192000, 188000, 176000, 169000,  
    174000, 182000  
])  
  
# Basic statistics  
print("Revenue Analysis:")  
print(f"Total Revenue: ₹{daily_revenue.sum():,}")  
print(f"Average Daily: ₹{daily_revenue.mean():,.2f}")  
print(f"Median: ₹{np.median(daily_revenue):,.2f}")  
print(f"Std Deviation: ₹{daily_revenue.std():,.2f}")  
print(f"Best Day: ₹{daily_revenue.max():,}")  
print(f"Worst Day: ₹{daily_revenue.min():,}")  
  
# Percentiles  
print(f"\n25th Percentile: ₹{np.percentile(daily_revenue, 25):,.2f}")  
print(f"75th Percentile: ₹{np.percentile(daily_revenue, 75):,.2f}")  
```  
  
### Conditional Operations  
  
```python  
import numpy as np  
  
# Passenger ages  
passenger_ages = np.array([25, 62, 8, 45, 70, 32, 15, 58, 5, 38,   
                          67, 22, 50, 12, 55, 28, 72, 35, 18, 48])  
  
# Count by category  
children = passenger_ages[passenger_ages < 12]  
senior_citizens = passenger_ages[passenger_ages >= 60]  
adults = passenger_ages[(passenger_ages >= 12) & (passenger_ages < 60)]  
  
print(f"Total Passengers: {len(passenger_ages)}")  
print(f"Children (<12): {len(children)}")  
print(f"Adults (12-59): {len(adults)}")  
print(f"Senior Citizens (60+): {len(senior_citizens)}")  
  
# Calculate discounted fare  
base_fare = 500  
children_fare = base_fare * 0.5      # 50% discount  
senior_fare = base_fare * 0.6        # 40% discount  
adult_fare = base_fare  
  
total_revenue = (len(children) * children_fare +   
                 len(adults) * adult_fare +   
                 len(senior_citizens) * senior_fare)  
  
print(f"\nTotal Revenue: ₹{total_revenue:,}")  
```  
  
### Array Manipulation  
  
```python  
import numpy as np  
  
# Reshaping data  
monthly_sales = np.array([120, 145, 132, 158, 165, 142, 138, 149,  
                          167, 178, 185, 192, 176, 169, 174, 182,  
                          188, 195, 201, 208, 215, 210, 198, 205,  
                          218, 225, 232, 228, 220, 213])  
  
# Reshape to weeks (30 days → 5 weeks × 6 days)  
weekly_view = monthly_sales.reshape(5, 6)  
print("Weekly Sales View:")  
print(weekly_view)  
  
# Calculate weekly totals  
weekly_totals = weekly_view.sum(axis=1)  # Sum across columns  
print("\nWeekly Totals:", weekly_totals)  
print("Best Week:", weekly_totals.max())  
  
# Calculate daily averages per week  
daily_avg = weekly_view.mean(axis=1)  
print("\nAverage Daily Sales per Week:", daily_avg)  
```  
  
### Combining Arrays  
  
```python  
import numpy as np  
  
# Three railway zones data  
western_zone = np.array([12500, 13200, 11800, 14500])  
central_zone = np.array([15600, 16200, 14900, 17100])  
southern_zone = np.array([11200, 12100, 10800, 13400])  
  
# Stack vertically (zones as rows)  
all_zones = np.vstack([western_zone, central_zone, southern_zone])  
print("All Zones Data:")  
print(all_zones)  
  
# Calculate zone-wise totals  
zone_totals = all_zones.sum(axis=1)  
print("\nZone Totals:", zone_totals)  
  
# Calculate day-wise totals across all zones  
day_totals = all_zones.sum(axis=0)  
print("Day-wise Totals:", day_totals)  
  
# Grand total  
print(f"Grand Total: {all_zones.sum():,}")  
```  
  
### Practical Example: Route Analysis  
  
```python  
import numpy as np  
  
# Kamlesh analyzes top 10 routes  
# Data: [Distance(km), Base_Fare, Daily_Passengers, Avg_Journey_Hours]  
routes = np.array([  
    [150, 200, 1245, 2.5],   # Mumbai-Pune  
    [1450, 1800, 856, 16.5], # Mumbai-Delhi  
    [350, 450, 1100, 5.0],   # Chennai-Bangalore  
    [280, 350, 980, 4.5],    # Delhi-Jaipur  
    [550, 680, 745, 8.0],    # Bangalore-Hyderabad  
    [200, 250, 1320, 3.0],   # Kolkata-Patna  
    [420, 520, 890, 6.5],    # Pune-Hyderabad  
    [320, 400, 1050, 5.5],   # Ahmedabad-Mumbai  
    [180, 230, 1180, 3.0],   # Chennai-Pondicherry  
    [390, 480, 920, 6.0]     # Jaipur-Agra  
])  
  
# Extract columns  
distances = routes[:, 0]  
fares = routes[:, 1]  
passengers = routes[:, 2]  
journey_hours = routes[:, 3]  
  
# Calculate daily revenue per route  
daily_revenue = fares * passengers  
  
print("Route Analysis:")  
print(f"Total daily passengers: {passengers.sum():,.0f}")  
print(f"Total daily revenue: ₹{daily_revenue.sum():,.2f}")  
print(f"Average fare: ₹{fares.mean():.2f}")  
print(f"Average journey time: {journey_hours.mean():.2f} hours")  
  
# Find most profitable route  
most_profitable = np.argmax(daily_revenue)  
print(f"\nMost Profitable Route: #{most_profitable + 1}")  
print(f"Revenue: ₹{daily_revenue[most_profitable]:,.2f}")  
print(f"Passengers: {passengers[most_profitable]:.0f}")  
  
# Routes with > 1000 daily passengers  
busy_routes = routes[passengers > 1000]  
print(f"\nBusy Routes (>1000 passengers): {len(busy_routes)}")  
  
# Calculate revenue per kilometer  
revenue_per_km = daily_revenue / distances  
print(f"\nAverage revenue per km: ₹{revenue_per_km.mean():.2f}")  
```  
  
### Random Data Generation (for Testing)  
  
```python  
import numpy as np  
  
# Generate random test data  
np.random.seed(42)  # For reproducible results  
  
# Simulate 100 random ticket prices between ₹200 and ₹2000  
random_prices = np.random.randint(200, 2001, size=100)  
print("Sample prices:", random_prices[:10])  
print("Average:", random_prices.mean())  
  
# Simulate passenger ages (normally distributed around age 35)  
passenger_ages = np.random.normal(35, 15, size=200)  
passenger_ages = np.clip(passenger_ages, 5, 80).astype(int)  # Between 5-80  
print("\nSample ages:", passenger_ages[:10])  
  
# Simulate booking success rate (80% success)  
bookings = np.random.choice(['Success', 'Failed'], size=500, p=[0.8, 0.2])  
success_count = np.sum(bookings == 'Success')  
print(f"\nSuccessful bookings: {success_count} out of 500")  
print(f"Success rate: {success_count/500*100:.1f}%")  
```  
  
---  
  
## Practice Exercise 1: Fare Calculator  
  
Create a fare calculation system using NumPy:  
  
```python  
import numpy as np  
  
# Distance matrix (km) between 5 cities  
# Cities: Mumbai, Pune, Bangalore, Chennai, Delhi  
distances = np.array([  
    [0, 150, 980, 1340, 1450],     # From Mumbai  
    [150, 0, 850, 1190, 1420],     # From Pune  
    [980, 850, 0, 350, 2150],      # From Bangalore  
    [1340, 1190, 350, 0, 2200],    # From Chennai  
    [1450, 1420, 2150, 2200, 0]    # From Delhi  
])  
  
# Your tasks:  
# 1. Calculate fare matrix (₹0.80 per km)  
# 2. Find most expensive route  
# 3. Find cheapest route (excluding 0s)  
# 4. Calculate average distance between all cities  
# 5. Which city has highest total distance to all others?  
  
# Your code here  
```  
  
---  
  
## Practice Exercise 2: Passenger Analysis  
  
```python  
import numpy as np  
  
# Last week's hourly passenger count (7 days × 24 hours)  
np.random.seed(100)  
hourly_passengers = np.random.randint(50, 500, size=(7, 24))  
  
# Your tasks:  
# 1. Find busiest hour of each day  
# 2. Find quietest hour of each day  
# 3. Calculate peak hours (>400 passengers)  
# 4. Find which day had most passengers  
# 5. Calculate average passengers per hour for each day  
  
# Your code here  
```  
  
---  
  
## Mini Quiz  
  
**Question 1:** What does this return?  
```python  
arr = np.array([10, 20, 30, 40, 50])  
result = arr[arr > 25]  
```  
a) [30, 40, 50]    
b) [True, True, True]    
c) Error    
d) [10, 20]  
  
**Question 2:** How to calculate mean of array `prices`?  
a) prices.mean()    
b) np.mean(prices)    
c) Both a and b    
d) sum(prices)/len(prices)  
  
**Question 3:** What is the shape of this array?  
```python  
data = np.array([[1,2,3], [4,5,6]])  
```  
a) (3, 2)    
b) (2, 3)    
c) (6, 1)    
d) (1, 6)  
  
**Question 4:** Which is faster for large datasets?  
a) Python lists    
b) NumPy arrays    
c) Both same    
d) Depends on operation  
  
**Question 5:** What does `arr.sum(axis=0)` do?  
a) Sum all elements    
b) Sum across rows (column-wise)    
c) Sum across columns (row-wise)    
d) Error  
  
---  
  
## Answers  
  
1. **a) [30, 40, 50]** - Boolean indexing returns elements that match condition  
2. **c) Both a and b** - Both methods work for NumPy arrays  
3. **b) (2, 3)** - 2 rows, 3 columns  
4. **b) NumPy arrays** - 50-100x faster for mathematical operations  
5. **b) Sum across rows (column-wise)** - axis=0 means along rows  
  
---  
  
## Assignment: Comprehensive Route Analysis  
  
Himesh is analyzing Indian Railways route data. Help him by completing this program:  
  
```python  
import numpy as np  
  
# Route data: [Route_ID, Distance_km, Fare, Mon, Tue, Wed, Thu, Fri, Sat, Sun]  
# Last 7 columns are daily passenger counts  
route_data = np.array([  
    [101, 150, 200, 1245, 1180, 1320, 1290, 1450, 1680, 1590],  
    [102, 1450, 1800, 856, 820, 890, 870, 920, 980, 940],  
    [103, 350, 450, 1100, 1050, 1180, 1120, 1200, 1320, 1280],  
    [104, 280, 350, 980, 940, 1020, 990, 1050, 1150, 1100],  
    [105, 550, 680, 745, 710, 780, 750, 820, 890, 850]  
])  
  
# Complete these tasks:  
# 1. Calculate total weekly revenue per route  
# 2. Find the most profitable day of the week  
# 3. Calculate average passengers per day per route  
# 4. Identify weekend effect (Sat+Sun vs weekdays average)  
# 5. Find correlation between distance and passenger count  
# 6. Generate a report with all findings  
  
# Your code here  
```  
  
**Expected Output:**  
```  
ROUTE ANALYSIS REPORT  
====================  
Route 101: Weekly Revenue = ₹...  
Most Profitable Day: Saturday  
Average Passengers: ...  
Weekend Boost: +23.5%  
```  
  
---  
  
## Summary  
  
You've learned:  
- Creating and manipulating NumPy arrays  
- Mathematical operations on entire datasets  
- Statistical analysis (mean, median, std)  
- Boolean indexing for filtering data  
- 2D arrays for tabular data  
- Reshaping and combining arrays  
