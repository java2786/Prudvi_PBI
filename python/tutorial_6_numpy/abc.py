import numpy as np  
  
# Daily passenger count for a week  
passengers_week1 = np.array([12450, 11890, 13200, 10350, 14670, 15890, 13450])  
  
print("Total passengers:", passengers_week1.sum())
print("Average per day:", passengers_week1.mean())
print("Busiest day:", passengers_week1.max())
print("Quietest day:", passengers_week1.min())
print("Standard deviation:", passengers_week1.std())
print("Variance:", passengers_week1.var())
print("Median passengers:", np.median(passengers_week1))
print("Sorted passenger counts:", np.sort(passengers_week1))