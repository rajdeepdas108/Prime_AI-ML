# Q5. Write a function to return the sum of digits of a number, n.

def sum_of_digits(n):
    num = str(n)
    total = 0
    for i in num:
        total += int(i)
    return total

a = int(input("Enter a number: "))
print(sum_of_digits(a))