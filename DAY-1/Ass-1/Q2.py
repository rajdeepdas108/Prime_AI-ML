# Q2. Take two numbers as input from the user and print their product and quotient.


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


product = num1 * num2
# product = num1 * num2   -------> it means multiplication of num1 and num2

quotient = num1 / num2 if num2 != 0 else "undefined (division by zero)" 
#quotient = num1 / num2   -------> it means division of num1 by num2

print(f"The product of {num1} and {num2} is {product}.")
# or 
print("product =", product)

print(f"The quotient of {num1} divided by {num2} is {quotient}.")
# or
print("quotient =", quotient)