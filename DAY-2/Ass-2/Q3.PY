# #Q3. Write a function that prints the digits of a number, n = 312. For example: for n = 312, there are 3 digits in it → 3, 1, and 2 & we need to print them. Hint:

# The rightmost digit of a number N is N % 10.

# To remove the rightmost digit from a number, we can do N = N / 10. WITHOUT FUNCTION


n = int(input("Enter a number: "))
while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10

