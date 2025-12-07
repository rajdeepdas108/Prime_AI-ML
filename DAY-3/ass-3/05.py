# Q5. Create a dictionary where:

# Keys = student names

# Values = marks (integer)

# Write a menu-based program where user presses a key (‘A’, ‘B’, ‘C’, ‘D’) depending on the operation they want to perform on the dictionary:

# Add a student

# Update marks

# Search for a student

# Display all students and marks


student_marks = {}

while True:
    print("\nMenu:")
    print("A. Add a student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students and marks")
    print("E. Exit")

    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student_marks[name] = marks
        print(f"Student {name} added with marks {marks}.")

    elif choice == 'B':
        name = input("Enter student name to update marks: ")
        if name in student_marks:
            marks = int(input("Enter new marks: "))
            student_marks[name] = marks
            print(f"Marks updated for student {name}.")
        else:
            print("Student not found.")

    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in student_marks:
            print(f"Marks for {name}: {student_marks[name]}")
        else:
            print("Student not found.")

    elif choice == 'D':
        if student_marks:
            print("All students and their marks:")
            for name, marks in student_marks.items():
                print(f"{name}: {marks}")
        else:
            print("No students in the dictionary.")

    elif choice == 'E':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")

