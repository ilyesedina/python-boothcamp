# Calculator application

import art
# TODO: Write a function for each operation: add, subtract, multiply, divide

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2      

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

# TODO: Create a dictionary to map operation symbols to functions

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary to perform calculations based on user input

# print(operations["*"](4, 8))

def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()