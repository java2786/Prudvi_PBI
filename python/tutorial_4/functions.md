# Python Functions and Arguments Tutorial

Functions are key building blocks in Python that allow you to encapsulate code for reuse and organization. This tutorial will cover different types of functions in Python, including their parameters and return values.

# Functions Without Arguments
A function that does not take any arguments can be defined simply. It performs a specific action when called.
python
```python
def greet():
    print("Welcome User")
# Call the function
greet()
```
Output:
```python
Welcome User
```
# Functions With Arguments

Functions can take arguments to customize their behavior. Here’s how you would define a function that takes an argument.
python
```python

def findDateUTC(date):
    print("UTC date:", date)

# Call the function with an argument
findDateUTC("December 18, 2025")
```
Output:
```python
UTC date: December 18, 2025
```

In a practical scenario, you might retrieve the current date automatically instead of passing it as an argument.
# Functions With Multiple Arguments

You can define functions that accept multiple arguments to perform more complex operations.
python
```python
def fail_students(score, attendance):
    # This function simulates finding students who failed based on their score and attendance.
    students = []

    # Here, you would typically query a database.
    if score < 40 or attendance < 75:
        students.append("Student Name")

    return students

# Call the function with arguments
failing_students = fail_students(35, 80)
print("Failing students:", failing_students)
```
Output:
```python
Failing students: ['Student Name']
```
# Functions with Default Value Arguments

You can also create functions with default argument values. If a value is not provided for that argument when calling the function, the default value will be used.
python
```python
def find_item(category, price=1000):
    # This function would find items within a category that cost less than the given price.
    print(f"Finding items in the category '{category}' with a price less than {price}.")

# Call the function without specifying the price
find_item("clothes")

# Call the function with a specific price
find_item("electronics", 800)
```
Output:
```python
Finding items in the category 'clothes' with a price less than 1000.
Finding items in the category 'electronics' with a price less than 800.
```

## Example Overview
- Functions without arguments - Simple operations, like greeting users.
- Functions with arguments - Customizable actions based on input.
- Functions with multiple arguments - More complex operations involving multiple inputs.
- Functions with default arguments - Flexibility by allowing default values.

You can combine these features as needed to create versatile and reusable functions that simplify your code.