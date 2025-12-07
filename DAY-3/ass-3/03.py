# Q3. Input two lists of integers from the user. Merge them into one list and sort the result. Eg –

# Code
# list1 = [1, 2, 7]  
# list2 = [2, 4, 5]  
# result = [1, 2, 2, 4, 5, 7]


list1 = [int(x) for x in input("Enter integers for list1 separated by space: ").split()]
list2 = [int(x) for x in input("Enter integers for list2 separated by space: ").split()]

result = list1 + list2
result.sort()
print("Merged and sorted list:", result)

