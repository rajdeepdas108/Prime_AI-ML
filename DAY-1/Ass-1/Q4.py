'''
Q4. The user enters a string containing a number (e.g., "45"). Convert it to:

an integer

a float

a string again

Print all three values with their types.  '''

number_str = input("Enter a number as a string: ")


number_int = int(number_str)
number_float = float(number_str)
number_str_again = str(number_float)

print(f"Integer: {number_int}, Type: {type(number_int)}")
print(f"Float: {number_float}, Type: {type(number_float)}")
print(f"String again: {number_str_again}, Type: {type(number_str_again)}")