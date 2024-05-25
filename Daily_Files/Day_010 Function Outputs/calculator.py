import os
clear = lambda: os.system('cls')

from calculator_art import logo

print(logo)

# Add
def add(add1, add2):
    return add1 + add2
# Subtract
def subtract(sub1, sub2):
    return sub1 - sub2
    
#Multiply
def multiply(mult1, mult2):
    return mult1 * mult2

#Divide
def divide(div1, div2):
    return div1 / div2

#Operation Dictionary
operaitons = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():


    num_1 = float(input("What's the first number?: "))

    for symbol in operaitons:
        print(symbol)

    keep_calcualting = True

    while keep_calcualting:
        operation_symbol = input("Pick an operation: ")
        num_2 = float(input("What's the next number?: "))
        answer = operaitons[operation_symbol](num_1,num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num_1 = answer
        else:
            keep_calcualting - False
            clear()
            calculator()
        
calculator()


    