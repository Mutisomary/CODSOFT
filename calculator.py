# Creating a command line calculator
import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

operations_dict = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

print("Welcome to the command line calculator\n")

def calculator():
    number1 = float(input("Input the first value want to perform operation on: "))

    continue_flag = True

    while continue_flag:

        operation = input("Which operation do you want to perform? (+, -, *, /): ")

        number2 = float(input("Input the second value want to perform operation on: "))

        calculator_function = operations_dict[operation]

        output = calculator_function(number1, number2)

        print(f"{number1} {operation} {number2} = {output}\n")

        to_continue = input(f"Enter 'y' to continue operation with {output} or 'n' to start a new operation or 'x' to exit operation ").lower()
        if to_continue == 'y':
            number1 = output
        elif to_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator()
        else:
            continue_flag = False
            print("Bye")

calculator()