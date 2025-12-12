# Array vs list 

marks = []

print("Total subjects:",len(marks))

# add marks for three subjects
marks.append(76)
marks.append(91)
marks.append(84)
marks.append(75)

# marks.append("nine")

print("Total subjects:",len(marks))


print("Marks of first subject:",marks[0])
# print("Marks of last subject:",marks[2])
# print("Marks of last subject:",marks[len(marks)-1])
print("Marks of last subject:",marks[-1])

print("All marks:",marks)

# remove third
marks.remove(84)


marks.sort(reverse=False)
print("All marks:",marks)
