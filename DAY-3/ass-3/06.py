# Q6. Given a list of words:

# Code
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length. Example:

# Code
# {"apple": 5, "banana": 6, "kiwi": 4, ...}


words = ["apple", "banana", "kiwi", "cherry", "mango"]

word_length_dict = {word: len(word) for word in words}
print(word_length_dict)

