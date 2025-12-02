# Q8. Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest:

# Code
# SI = (P * R * T) / 100


P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time period: "))
SI = (P * R * T) / 100
print("Simple Interest:", SI)