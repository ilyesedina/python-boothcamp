enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()


# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

# There is no Block Scope in Python

if 3 > 2:
    a_variable = 10
    print(a_variable)

# Game Challenge
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]
    
    print(new_enemy)

create_enemy()


# Game Challenge two
game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = enemies[0]
    if game_level < 5:
        new_enemy = enemies[0]
    
    print(new_enemy)
    
create_enemy()


# Prime Number Checker
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True

print(is_prime(7))   # True
print(is_prime(4))   # False
print(is_prime(1))   # False

# Game Challenge three / Modifying Global Scope
enemies = "Skeleton"

def increase_enemies():
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Game Challenge four / Modifying Global Scope / Not recommended to modify global scope within a function that has local scope
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Game Challenge five / 
enemies = 1

def increase_enemies(enemy):

    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

# Global Constants / they are variables that are not meant to be changed.

PI = 3.14159
GOOGLE_URL = "https://www.google.com"


def my_func():
    print(GOOGLE_URL)
