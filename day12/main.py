print(f"Welcome to the Number Guessing Game!")
print(f"I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    attempts = 5
print(f"You have {attempts} attempts remaining to guess the number.")

