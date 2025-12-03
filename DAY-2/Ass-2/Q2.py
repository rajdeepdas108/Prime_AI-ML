# Q2. Write a function that takes two integers a and b and prints all even numbers between them (inclusive).



def print_even_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

# Example usage:
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
print_even_numbers(a, b)