# python3 day9/lesson.py
# Python dictionary 
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again until you reach the end of a list, or a certain condition is met."

#print(programming_dictionary)

empty_list = []
empty_dictionary = {}

# Wipe an existing dictionary

# programming_dictionary = {}     
# print(programming_dictionary)

# Edit an item in a dictionary

programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# Dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Print out Lille from the travel_log
print(travel_log["France"][1])

# Nested lists

nested_list = ["a", "b", ["c", "d"]]
print(nested_list[2][1])

# Dictionary in a dictionary

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 6,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    },
}
print(travel_log["Germany"]["cities_visited"][2])