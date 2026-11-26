# Python password generator based on user-defined criteria
import random
import string

print(f"Welcome to the Password Generator!")
letters = input("How many letters would you like in your password?\n")
symbols = input("How many symbols would you like?\n")
numbers = input("How many numbers would you like?\n")

if not (letters.isdigit() and symbols.isdigit() and numbers.isdigit()):
    print("Please enter valid numbers for letters, symbols, and numbers.")
    exit()
letters = int(letters)
symbols = int(symbols)
numbers = int(numbers)

password_characters = []
for _ in range(letters):
    random_letter = random.choice(string.ascii_letters)
for _ in range(symbols):
    password_characters.append(random.choice(string.punctuation))
for _ in range(numbers):
    password_characters.append(random.choice(string.digits))

print(f"Your generated password is: {''.join(password_characters)}")