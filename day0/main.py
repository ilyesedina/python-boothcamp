# String concatenation example with input() function
print("Welcome, " + input("What is your name?\n") + "!")

#Python variables
name = input("What is your name?\n")
print("Hello, " + name + "!")

# Calculate the length of the name variable which is a string
# Use the built in function len()
name_length = len(name)
# Print the length of the name variable with data type conversion
print("Your name has " + str(name_length) + " characters.")

# F-Strings for string formatting
print(f"Your name has {name_length} characters.")

# Directly using len() with input()
print(len(input("What is your name?\n")))

# Combining variables witch output a function and f-Strings
userName = input("What is your name?\n")
nameLength = len(userName)
print(f"Hello, {userName}! Your name has {nameLength} characters.")

