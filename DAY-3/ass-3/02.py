# Q2. Given a list of integers compute the average of all numbers in the list.


list = [int(x) for x in input("Enter integers separated by space: ").split()]

average = sum(list) / len(list)
print("Average:", average)
