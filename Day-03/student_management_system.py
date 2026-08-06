students = []

def add_student():
    sid = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = list(map(int, input("Enter Marks (space separated): ").split()))

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    for s in students:
        avg = sum(s["marks"]) / len(s["marks"])
        print(f"ID: {s['id']}")
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Course: {s['course']}")
        print(f"Marks: {s['marks']}")
        print(f"Average: {avg:.2f}")
        print()


def update_student():
    sid = int(input("Enter Student ID to update: "))

    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter New Name: ")
            s["age"] = int(input("Enter New Age: "))
            s["course"] = input("Enter New Course: ")
            s["marks"] = list(map(int, input("Enter New Marks: ").split()))
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    sid = int(input("Enter Student ID to delete: "))

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def search_student():
    term = input("Enter Student ID or Name: ").lower()

    for s in students:
        if term == str(s["id"]) or term == s["name"].lower():
            avg = sum(s["marks"]) / len(s["marks"])
            print(f"\nID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")
            print(f"Course: {s['course']}")
            print(f"Marks: {s['marks']}")
            print(f"Average: {avg:.2f}\n")
            return

    print("Student not found.\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        search_student()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")
