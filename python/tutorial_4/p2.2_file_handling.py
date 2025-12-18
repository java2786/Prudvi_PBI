messages = [
    "Prudvi: Hello friends, how are you ?",
    "Arun: I am great."
    ]

# how to open a file for write operation
with open("abc.txt", "a") as fileObj:
    for message in messages:
        fileObj.write(message+"\n") 
    
    
# read abc.txt file
with open("abc.txt", "r") as fileObj:
    for line in fileObj:
        print(line.strip())
       
