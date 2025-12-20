import numpy as np

marks = [87, 93, 85, 82]
print(type(marks))

marks_array = np.array(marks)
print(type(marks_array))

print("Total marks:",np.sum(marks_array))
print("Total avg:",np.average(marks_array))

