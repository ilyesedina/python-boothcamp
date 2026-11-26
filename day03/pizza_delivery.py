print("Wlecome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
bill = 0

# Calculate the bill based on size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size selected.")
# print (f"Your current bill is: ${bill}")
add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni == "Y":
    print("Pepperoni cost additional $2")
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    print("No pepperoni added.")
# print (f"Your current bill is: ${bill}")
extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese == "Y":
    bill += 1
else:
    print("No cheese added.")
print (f"Your current bill is: ${bill}")
