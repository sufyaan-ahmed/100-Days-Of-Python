# printing Hello World!
print("Hello World!")

# escape sequence character
print("I am good boy\nand the viwer is also a good boy/girl") # here \n adds new line
print("Who is good boy? \"Sufyan\"") # here two \"\" specify a charcter, because if you add "" directly to the print it will show error

# Data Types

print(5) # number
print("Sufyan") # string (includes inverted commas "")
print(False) # boolean (true or false)

# simple equations

print(10 + 10) # adding numbers
print(10 - 10) # subtracting numbers
print(10 * 10) # multiplying numbers
print(10 / 10) # dividing numbers

# print parameters

print("Sufyan", 5, True) # you can combine different data types in a single print statment and seperate them by adding ","
print("Hey", "I", "am", "Sufyan", sep="-") # you can seperate the values by adding sep= and add whatever character you want like: ~, -, _, and etc 
print("Hey", "I", "am", "Sufyan,", end=" 14 ") # you can add string at the end of the statment by using end=, as you can see first I add My name is Sufyan and at the end I add end= " 14 ", and the print statment at bottom has "is my age", because "end" statment add end= value before the bottom or second print statment 
print("is my age")