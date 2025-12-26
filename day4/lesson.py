import random
# import my_module

# random_intiger = random.randint(1, 10)
# print("Random Integer between 1 and 10:", random_intiger)

# print("My favorite number is:", my_module.my_favorite_number)

# random_number_0_to_1 = random.random()
# print("Random number between 0 and 1:", random_number_0_to_1)

# random_float_1_to_10 = random.uniform(1, 10)
# print("Random float between 1 and 10:", random_float_1_to_10)

# random_choice = random.choice(['heads', 'tails'])
# print("Random choice from list:", random_choice)

# random_head_tail = random.randomint(0, 1)
# if random_head_tail == 0:
#    print("heads")
# else:
#    print("tails")

stat_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
    "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
    "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

# stat_of_america.append("Angelaland")
stat_of_america.extend(["Angelaland", "New Angelaland"])
print(stat_of_america[-1])

friends = ["Alice", "Bob", "Charlie", "David"]

# option 1
random_friend = random.choice(friends)
print("Random friend selected:", random_friend)

# print(len(stat_of_america))
random_index_state = len(stat_of_america) # 50 -> 49
print(stat_of_america[random_index_state - 1])

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes" ]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)