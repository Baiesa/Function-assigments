

'''
Objective:
The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, 
and division.
'''

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def calculator():
    print("Welcome to the Calculator App!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation number (1/2/3/4): ")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operation == '1':
        result = add(num1, num2)
        print("Result:", result)
    elif operation == '2':
        result = subtract(num1, num2)
        print("Result:", result)
    elif operation == '3':
        result = multiply(num1, num2)
        print("Result:", result)
    elif operation == '4':
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print("Invalid operation number")

calculator()
