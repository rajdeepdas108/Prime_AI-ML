# Q9. Given a list, print all elements that appear more than once in the list. [Hint – use sets]

list_elements = [1, 2, 3, 2, 4, 5, 1, 6, 3]

seen = set()
duplicates = set()

for element in list_elements:
    if element in seen:
        duplicates.add(element)
    else:
        seen.add(element)

print("Elements that appear more than once:", duplicates)
