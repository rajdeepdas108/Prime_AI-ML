#Q4. Write a function to return the count of digits in a number, n.

# def count_digits(a):
#     count = 0
#     while a > 0:
#         a //= 10      # remove last digit
#         count += 1    # increase count
    
#     return count


# a = int(input("Enter a number: "))
# print(count_digits(a))

# simple method 

# a = int(input("Enter a number: "))
# num = str(a)
# count = 0
# for i in num:
#     count = count + 1
# print(count)


# another method using fnx




def count_digits(n):   # fnx declear 
    num = str(n)
    count = 0
    for i in num:
        count = count + 1
    return count

a = int(input("Enter a number: "))

ans = count_digits(a)   # function call

print(ans)

