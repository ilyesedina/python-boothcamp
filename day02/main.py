# Tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

tip = bill * (tip_percent / 100)
total_bill = bill + tip
amount_per_person = total_bill / people

print(f"Each person should pay: ${amount_per_person, 2}")