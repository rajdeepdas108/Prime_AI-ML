# prinnt sum of first n natural numbers
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum of first", n, "natural numbers is:", sum)


# or
a = int(input("Enter a number: "))

sum = a*(a+1)//2  # // ----> use for integer division  output will be integer   
                    # / ----> use for float division output will be float
print("Sum of first", a, "natural numbers is:", sum)