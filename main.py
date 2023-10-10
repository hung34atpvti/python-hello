import keyword
import math
from math import isqrt
import calculator

"""Basic
"""

# Hello World
print("Hello World!")  # Hello World!

# Variables
name, age = "Declan", 20
pi = 3.14
numbers = [1, 2, 3, 4, 5]

print(name)  # Declan
print(age)  # 20
print(pi)  # 3.14
print(numbers)  # [1, 2, 3, 4, 5]

# Naming variables
full_name = "Declan Nguyen"  # underscore convention
PI = 3.14  # constants will UPPERCASE

# Datatypes
brand = "Declan code"
age = 2
pi = 3.14
numbers = []
isAdult = True
print(type(brand))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(numbers))  # <class 'list'>
print(type(pi))  # <class 'float'>
print(type(isAdult))  # <class 'bool'>

# Dynamically Typed
brand: str = "Declan code"  # -> brand = "Declan code"
isAdult: bool = False  # -> isAdult = False

# Strings
print(brand)
brand = 'Declan code'
print(brand.upper())
print(brand.replace('a', '33'))
print(len(brand))
print(brand == "Declan code")
print(brand == "declan code")
print(brand != "Declan code")
print("code" in brand)
print("code" not in brand)

# Multiline and Formatting Strings
comment = "abc " \
          "def " \
          "ghi"
cmt = """
abc
def
ghi
"""

name = "Declan"
email = """
hello {},
how are you?
It was nice talking to you
"""
em = f"""
hello {name}, 
how are you?
It was nice talking to you
age {4 + 4}
"""
print(comment)
print(cmt)
print(email.format(name))
print(em)


# Indentation and Keyword
def my_funtion():
    my_name = "Declan"
    surname = "Manh"


# Reserved Keyword
print(keyword.kwlist)

"""Operator
"""
# Arithmetic
result = 1 + 2
print(result)
print(1 + 2)
print(1 * 2)
print(10 / 2)
print(9 % 2)
print(10 ** 2)  # 10^2

# Logical
print(10 > 5)
print(10 >= 9)
print(not
      ((10 > 5)
       or (1 > 3)
       and "A" == "C")
      )  # ! || &&

# Assignment
number = 4
number += 1
number **= 3
print(number)

"""Control Flow
"""
# If
number = 0
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(number)
else:
    print(f"{number} is negative")

message = "positive" if number > 0 else "0 or negative"
print(message)

"""Data structure
"""
# List
numbers = [1, 2, 3, 4, -1, 0, ["A", "B"]]
print(numbers[6][1])
numbers = [1, 2, 3, 4, -1, 0]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(1000)
print(numbers)
print(len(numbers))
numbers.clear()
print(numbers)
numbers = [1, 2, 3, 4, -1, 0, 1]
numbers.remove(1)  # remove first element match
print(numbers)
numbers.pop()
print(numbers)
del numbers[0]
print(numbers)
del numbers[0:3]
print(numbers)

# Set
numbersList = [1, 1]
numbersSet = {1, 1}
lettersSet = {"A", "A", "B", "C", "C"}  # No order
print(numbersList)
print(numbersSet)
print(lettersSet)

# Union Intersection Difference
lettersA = {"A", "B", "C", "D"}
lettersB = {"E", "F", "A"}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB
print(f"union: {union}")
print(f"intersection: {intersection}")
print(f"difference: {difference}")

# Dictionaries ~ Object
person = {
    "name": "Declan",
    "age": 20,
    "address": "VN"
}
print(person["name"])
print(person.keys())
print(person.values())
# person.clear()
# print(person)
print(person.get("age"))
print(person)
person["age"] = 100
print(person)

"""Loop
"""
names = ["Declan", "Thomas", "Nathan"]
for name in names:
    print(name)
names = {"Declan", "Thomas", "Nathan"}  # No order
for name in names:
    print(name)

for key in person:
    print(f"key: {key}, value: {person[key]}")

for key, value in person.items():
    print(f"key: {key}, value: {value}")

number = 0
while number < 10:
    print(number)
    number += 1
else:
    print("while loop ended")

number = 0
while number < 10:
    print(number)
    if number == 5:
        break
    number += 1
else:
    print("while loop ended")

number = 0
while number < 10:
    number += 1
    if number < 5:
        continue
    print(number)
else:
    print("while loop ended")

for n in [1, 2, 3, 4, 5, 6, 7]:
    if n < 5:
        continue
    print(n)

for n in [1, 2, 3, 4, 5, 6, 7]:
    if n == 5:
        break
    print(n)

"""Function
"""


def greet(my_name, my_age=1):
    print(f"Hello {my_name} how are you at {my_age}?")


greet("Declan", 20)
greet("Thomas")


def is_adult(my_age):
    return my_age >= 16


print(is_adult(20))


def convert_gender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender {gender}"


print(convert_gender("m"))

# Built-in
print(math.pi)
print(math.isqrt(25))
print(isqrt(25))

# Modules
print(calculator.add(1, 2))
print(calculator.sub(1, 2))
