# Variables & Data Types

'''
Variables are just like constainer that stores items in it, very similar
to the jars in out kitchen that stores jam, dates and etc.
'''

# Example

a = 1        # number
b = "Sufyan" # string
c = True     # boolean
d = None     # NoneType

# Simple operations with variables

num1 = 1
num2 = 2

print(num1 + num2)

# We can also print 2 different types of values in single "print" statement (Simplified)

greet = "Hello"
name = "Sufyan!"

print(greet, name) # we can seperate then by using ",". This will work as a seperator of different values

# we can perform operation in variables by using values and operators

a1 = 1+1
a2 = 1+2

print(a1 + a2)

# Data Types

'''
Data type specifies the type of values a variable holds. This is required
in programming to do various operations without causing an error.
'''

# Printing data types 

dataType1 = 14
print(type(dataType1))

dataType2 = "Sufyan"
print(type(dataType2))

dataType3 = True
print(type(dataType3))

dataType4 = 1.1        # Float
print(type(dataType4))

dataType5 = complex(5 + 5j) # Complex
print(type(dataType5))

# Boolean Data

'''
boolean is basically True or False. For example: You want to give
answer in yes or no
'''

# Sequenced Data: List & Tuple (Simplified)

# List

'''
List is a special kind of variable that can store several different
types of data in it.
'''

list1 = ["apple", "Banana", "Grapes", "Mango", "Orange"]
print(list1)

# we can also store different types of data in it

list2 = ["blue", 13, "green", 4, True]
print(list2)

# Tuple

'''
Tuple is exactly the same thing as list, except it is immutable
(cannot be changed).
'''

tuple = (("Parrot", "Sparrow"),
         ("Lion", "Tiger"))
print(tuple)

# Mapped Data: dict

'''
ever saw a dictionary that have information of a specific thing.
Just like mapped data is same as dictionary.
'''

dict = {"name": "Sufyan",
        "age": 14,
        "canDrive": False,
        "car": None}
print(dict)