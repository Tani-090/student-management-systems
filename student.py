
from storage import load_students, save_students

students = load_students()

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
    
def add_student():
    try:
        student_id = int(input("Enter student ID: "))

        if any(s["id"] == student_id for s in students):
            print("Student ID already exists.")
            return

        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        marks = float(input("Enter marks: "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        student = {
            "id": student_id,
            "name": name,
            "marks": marks
        }

        students.append(student)
        save_students(students)

        print("Student added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for student in students:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Marks: {student['marks']}"
        )


def search_student():
    try:
        student_id = int(input("Enter student ID to search: "))

        for student in students:
            if student["id"] == student_id:
                print("Student found:")
                print(student)
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")


def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))

        for student in students:
            if student["id"] == student_id:
                new_name = input("Enter new name: ").strip()

                if not new_name:
                    print("Name cannot be empty.")
                    return

                new_marks = float(input("Enter new marks: "))

                if not 0 <= new_marks <= 100:
                    print("Marks must be between 0 and 100.")
                    return

                student["name"] = new_name
                student["marks"] = new_marks

                save_students(students)
                print("Student updated successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter valid numbers.")


def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                save_students(students)

                print("Student deleted successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")





def sort_students():
    print("Total students:", len(students))

    if not students:
        print("No students found.")
        return

    print("\nSort Students By:")
    print("1. Name (A to Z)")
    print("2. Marks (Highest to Lowest)")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        sorted_students = sorted(
            students,
            key=lambda student: student["name"].lower()
        )

    elif choice == "2":
        sorted_students = sorted(
            students,
            key=lambda student: student["marks"],
            reverse=True
        )

    else:
        print("Invalid choice.")
        return

    print("\n--- Sorted Student List ---")

    for student in sorted_students:
        grade = calculate_grade(student["marks"])

        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Marks: {student['marks']}, "
            f"Grade: {grade}"
        )

    print("End of sorted list.")
    
    
# 8. Calculate class average
def calculate_average():
    if not students:
        print("No students found.")
        return

    total_marks = 0

    for student in students:
        total_marks += student["marks"]

    average = total_marks / len(students)

    print(f"Total students: {len(students)}")
    print(f"Total marks: {total_marks}")
    print(f"Class average: {average:.2f}")


# 9. Find the topper
def find_topper():
    if not students:
        print("No students found.")
        return

    topper = max(students, key=lambda student: student["marks"])

    print("\n--- Class Topper ---")
    print(f"ID: {topper['id']}")
    print(f"Name: {topper['name']}")
    print(f"Marks: {topper['marks']}")
    print(f"Grade: {calculate_grade(topper['marks'])}")
