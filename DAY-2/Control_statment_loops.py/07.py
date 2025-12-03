word = "artificial intelligence"

# count the number of i's => 5

count = 0

for ch in word:
    if ch == 'i' or ch == 'e' or ch == 'a' or ch == 'o' or ch == 'u':
        count += 1

print("count of vowels =", count)