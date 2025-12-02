# Q9. Take a decimal number as input (like 45.78) and output its:

# integer part → 45

# fractional part → .78

decimal_number = float(input("Enter a decimal number: "))

integer_part = int(decimal_number)   # TYPE CASTING


fractional_part = decimal_number - integer_part     # FRACTION = FLOAT VALUE - INTEGER VALUE


print("Integer part:", integer_part)
print("Fractional part:", fractional_part)