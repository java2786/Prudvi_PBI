students = [{
    "name": "Ramesh",
    "subjects": {"Math", "English", "Computer"},
    "contact": {"email": ["ram@ymail.com", "ramesh@gmail.com"], "phone": {6789,9878}},
    "age": 23
}]

print(type(students[0]))
print(type(students[0]["contact"]["phone"]))
print(students[0]["contact"]["phone"])
