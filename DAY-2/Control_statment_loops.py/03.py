n = int(input("Enter a number: "))

# multiplication table of n

i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    # print(n*i)
    i += 1

print("\n")
# or method 2

i = 0
while i < 10:
    print(f"{n} x {(i+1)} = {n * (i+1)}")
    # print(n* (i+1))
    i += 1


