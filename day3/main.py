# Treasure hunt game implementation

print("Welcome to Treasure Island.\nYour mission is to find the treasure. You're at a cross road.")
direction = input('Where do you want to go? \nType "left" or "right": ')

print(f"You chose to go {direction}.")
if direction == "right":
    print("You fell into a hole. Game Over.")
elif direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    if lake == "swim":
        print("You get attacked by an angry trout. Game Over.")
    elif lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        door = input("Which colour do you choose? ")
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
