# Data Types

# string - str "I am a string"
# integer - int 123
# float - float 12.34
# boolean - bool  True or False

# Subscripting
print("Hello"[0])
# prints H, as that is the 0th index of the string (first letter)

# String
print("123" + "456")
# prints 123456, as the + operator concatenates strings

# Integer = whole numbers
print(123 + 456)
# prints 579, as the + operator adds integers

# Large Integer
print(123_456_789 + 987_654_321)

# Float = decimal numbers
print(3.14 + 1.59)

# Boolean = True or False
print(True)
print(False)

# Type Checking
print(type("Hello"))   # prints <class 'str'>
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion/ Casting
print(int("123") + int("456"))

# Value error example
# print(int("abc"))      # converts string to integer

name = input("What is your name?\n")
length_of_name = len(name)
print("Number of characters in your name: " + str(length_of_name))

print("My age is " + str(27))

# Mathematical operations
print(3 + 5)    # Addition
print(10 - 2)   # Subtraction
print(4 * 2)    # Multiplication
print(8 / 4)    # Division (outputs a float)
print(7 // 3)   # Floor Division (outputs an integer)
print(7 % 3)    # Modulus
print(2 ** 3)   # Exponentiation

# PEMDAS/BODMAS
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
#     ()           **            * OR /                 + OR -

print(3 + 5 * 2)        # prints 13
print((3 + 5) * 2)      # prints 16

print(3 *3 + 3 / 3 - 3)    # prints 7.0 (float)
print(3 *3 + 3 / 3 - 7)    # prints 3.0 (float)

# BMI Calculator

height = 1.69
weight = 57

bmi = (weight / (height ** 2))
print(bmi)
print(int(bmi))
print(round(bmi))

# ------------

# F-Strings (formatted strings)
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
