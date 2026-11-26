import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []

while not game_over:

    print(f"***********************{lives}/6 lives left***********************")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed the letter {guess}. Try again.")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("World to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        print(stages[lives])
        if lives == 0:
            game_over = True
            print("You lose. The word was " + chosen_word)

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])