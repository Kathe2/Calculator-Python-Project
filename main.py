#Calculator
# add
from typing import final
from art import logo

def add (n1, n2):
    return n1 + n2

#Subtract
def sub(n1, n2):
    return n1 - n2

#Multiply
def mult(n1, n2):
    return n1 * n2

#Divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    
    for op in operations:
        print(op)
    
    operation_symbol = input("Pick an operation from the line above: ")
    
    num2 = float(input("What's the second number?: "))
    
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    
    
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    
    final_answer = first_answer
    
    cont = input(f"Type 'y' to continue whith {final_answer}, type 'n' to start a new calculation or 'x' to exit: ")
    
    while cont == "y":
        operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        second_answer = calculation_function(final_answer, num3) 
        print(f"{final_answer} {operation_symbol} {num3} = {second_answer}")
        final_answer = second_answer
        
        cont = input(f"Type 'y' to continue whith {final_answer}, type 'n' to start a new calculation or 'x' to exit: ")

    if cont == "n":
        calculator()
    
calculator()