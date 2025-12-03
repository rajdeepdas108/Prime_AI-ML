n = int(input("Enter a number: "))

                    # initial value of factorial is 0 for summation
def fact(n):
    factorial = 1  # Initialize factorial to 1 for multiplication
    for i in range(1, n + 1):
        factorial *= i
    return factorial

print(f"The factorial of {n} is {fact(n)}")