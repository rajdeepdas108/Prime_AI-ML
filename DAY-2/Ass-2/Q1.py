#Q1. Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:

# If salary < 30,000 → 5%

# If salary is 30,000–70,000 → 15%

# If salary > 70,000 → 25%


salary = float(input("Enter your salary: "))

if salary < 30000:
    tax_rate = 5
elif salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

print(f"Your tax rate is: {tax_rate}%")

# Calculate the tax amount
tax_amount = (tax_rate / 100) * salary
print(f"The tax amount on your salary is: {tax_amount}")

