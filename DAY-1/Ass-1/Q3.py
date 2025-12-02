# Q3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.

int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
flt = float(input("Enter a float: "))

# Convert all to floats
float1 = float(int1)
float2 = float(int2)

# Calculate average
average = (float1 + float2 + flt) / 3

print(f"The average of {float1}, {float2}, and {flt} is {average}.")