# Q1. Ask the user for a string and check whether it is a palindrome or not. A palindrome “madam”, “racecar” is a string which is same when we read it forward & backward. [Hint – A palindrome string is equal to the reversed version of the string. We can use a loop to reverse the string manually.]

str = input("Enter a string: ")

reverse_str = ""
for char in str:
    reverse_str = char + reverse_str

if str == reverse_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")