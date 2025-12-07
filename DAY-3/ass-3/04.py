# Q4. Given a tuple of integers, create:

# A tuple of all even numbers

# A tuple of all odd numbers


tuple_input = tuple(int(x) for x in input("Enter integers separated by space: ").split())
even_numbers = tuple(x for x in tuple_input if x % 2 == 0)
odd_numbers = tuple(x for x in tuple_input if x % 2 != 0)

print("Even numbers tuple:", even_numbers)
print("Odd numbers tuple:", odd_numbers)
