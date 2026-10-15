
from student_mysql import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    sort_students,
    calculate_average
)

while True:
    print("\n===== MySQL Student Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("7. Sort Students")
    print("8. Calculate Class Average")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "7":
        sort_students()
    elif choice == "8":
        calculate_average()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
