# read file or write file

# 2 thing - read and write
with open("p1_function.py", "r") as fileObj:
    # print(fileObj)
    for data in fileObj:
        print(data.strip())
    
print("Bye Bye")