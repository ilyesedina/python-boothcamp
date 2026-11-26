from art import logo
from random import randint

# Attempt limits based on selected difficulty. Global Constant 
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, secret_number, turns_left):
    # Wrong guesses cost one turn and provide directional feedback.
    if user_guess > secret_number:
        print("Too high.")
        return turns_left - 1
    if user_guess < secret_number:
        print("Too low.")
        return turns_left - 1

    print(f"You got it! The answer was {secret_number}.")
    return turns_left


def set_difficulty():
    # Default to hard turns unless the user explicitly chooses easy.
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    return HARD_LEVEL_TURNS


def game():
    # Intro screen and game setup.
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("\nI am thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()

    # Keep asking until the player finds the answer or runs out of turns.
    guess = None
    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose. The number was {answer}.")
            return
        if guess != answer:
            print("Guess again.")


game()

