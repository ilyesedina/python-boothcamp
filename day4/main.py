# Rock papers scissors game
import random

print("Welcome to Rock, Paper, Scissors!")
options = ["rock", "paper", "scissors"]

user_input = input("Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
user_choice = options[int(user_input)]
computer_choice = random.choice(options)
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

#prit out choices drawing ascii art
rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper_art = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---._______)
'''
art_options = [rock_art, paper_art, scissors_art]
print(art_options[int(user_input)])
print(art_options[options.index(computer_choice)])

# Logic to determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")