# Q7. Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit”.

while True:
    user_input = input("Enter a number (or 'Quit' to stop): ")
    if user_input.lower() == "quit":
        break
    n = int(user_input)
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")