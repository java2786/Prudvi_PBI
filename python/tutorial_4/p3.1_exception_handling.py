# read xyz.txt file
try:
    with open("xyz.txt", "r") as fileObj:
        print("write is done")
except(FileNotFoundError):
    print("File not found")

try:
    num1= int(input("Enter first number: ")) # "23"
    num2= int(input("Enter second number: ")) # "3"
    print(f"Addition of {num1} and {num2} is {num1+num2}")
    print(f"Subtraction of {num1} and {num2} is {num1-num2}")
except(ValueError):
    print("Input Error occurred")
    
