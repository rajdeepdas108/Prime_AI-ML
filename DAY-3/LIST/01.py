l = [1, 2, 3, 10, 4, 2]

i = 0
for val in l:
    
    if val == 10:
        print(i) # print the index of 10
        break
    i += 1


# shortcut using index method

print(l.index(10))
print(l.count(2))  # prints the count of occurrences of 2




