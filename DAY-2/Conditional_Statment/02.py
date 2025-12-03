user_name = input("Enter your name: ")
user_password = input("Enter your password: ")

# Simple authentication check
if user_name == "admin" and user_password == "pass" :
    print("Access granted.")
else :
    print("Access denied.")