# Q8. Write a program to check whether two lists share no common elements.

# Examples:

# share no common elements →

# Code
# list1 = [1, 2, 3, 4]  
# list2 = [5, 6, 7, 8]
# share common elements →

# Code
# list1 = [1, 2, 3]  
# list2 = [3, 4]
# [Hint – use sets]


list1 = [1, 2, 3, 4]  
list2 = [5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

if set1.isdisjoint(set2):
    print("The lists share no common elements.")
else:
    print("The lists share common elements.")

