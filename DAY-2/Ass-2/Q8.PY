# Q8. Let’s create a Simple Calculator. Create a function calculator(a, b, operation) that performs arithmetic operations. The parameter operation can have values: +, -, *, /.

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

print(calculator(a, b, operation))