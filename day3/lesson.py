# Amusement park

print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))
if height < 120:
    print("Sorry, you have to grow taller before you can ride.")
else :
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    price = int(0)  # default price
    if age >= 18:
        price = int(12)
        print(f"You are an adult, ticket price is {price}.")
    elif age >= 12:
        price = int(7)
        print(f"You are a teenager, ticket price is {price}.")
    elif 45 <= age <= 55:
        price = int(0)
        print("You are in the mid-life special age group, your ticket is free!")
    else :
        price = int(5)
        print(f"You are a youth, ticket price is {price}.")
    picture = input("Do you want a photo taken? y or n: ")
    if picture == "y":
        print(f"Photo added to your ticket for an extra $3. Total price is {price + 3}.")
    if picture == "n":
        print("No photo added. Enjoy your ride!")

# Comparison operators
# >, <, >=, <=, ==, !=
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal to
# != not equal to

# Modulo operator
# It gives the remainder of a division
# Example: 7 % 3 = 1 (7 divided by 3 is 2 with a remainder of 1)

# Odd or Even checker

print("Odd or Even Checker")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")