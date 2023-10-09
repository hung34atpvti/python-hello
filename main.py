import keyword

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
