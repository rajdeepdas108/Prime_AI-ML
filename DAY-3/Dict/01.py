info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

unique_cources = set()

for tup in info:
    unique_cources.add(tup[1])

print(unique_cources)

# Output: {'Math', 'Science', 'English'}

