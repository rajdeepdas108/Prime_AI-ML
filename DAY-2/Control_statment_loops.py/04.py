i = 1

while (i <= 10):
    if (i== 6):
        break
    print(i)
    i += 1

print("outside loop now.....")

print("\n")
# continue statement
i = 0
while (i < 10):
    i += 1   # ata uper e likhte hobe , karon continue er por nicher line gulo execute hoy na
    if (i % 3 ==0):
        continue
    print(i)

print("outside loop now.....")