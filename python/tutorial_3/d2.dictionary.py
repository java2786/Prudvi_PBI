# pair
"""
name - number
item - price
studentId - marks
city - temprature
country - capital
country - cities
-------------------
{key - value}
correct fromat 
{"key": value}
    datatype of value can anything
"""

phone_book = {
    "ramesh": 78763, 
    "suresh": 789073, 
    "dinesh":98542
}
print(type(phone_book))
print(phone_book)
print(phone_book["ramesh"])
# print(phone_book["mukesh"])

phone_book["ramesh"] = 789073