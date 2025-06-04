# Simple Result Management System

students = []  # List to store student data

def calculate_gpa(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        return 10
    elif avg >= 80:
        return 9
    elif avg >= 70:
        return 8
    elif avg >= 60:
        return 7
    elif avg >= 50:
        return 6
    elif avg >= 40:
        return 5
    else:
        return 0

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = []
    for i in range(3):  # Assume 3 subjects
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    gpa = calculate_gpa(marks)
    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "gpa": gpa
    }
    students.append(student)
    print("Student added!\n")

def show_all_students():
    if not students:
        print("No students found.\n")
        return
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, GPA: {s['gpa']}")
    print()

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s['roll'] == roll:
            print(f"Found: Name: {s['name']}, Marks: {s['marks']}, GPA: {s['gpa']}\n")
            return
    print("Student not found.\n")

def menu():
    while True:
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            show_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
