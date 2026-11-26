def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()

# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")

greet_with_name("Edina")


def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

life_in_weeks(12)

# Functions with more than one input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Jack Power", "New York")
# greet_with(name="Jack Power", location="New York")