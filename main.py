
from student_ysql import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    sort_students,
    calculate_average,
    find_topper
)


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("7. Sort Students"),
        print("8. Calculate Class Average"),
        print("9. Find Topper")

        choice = input("Enter your choice: ").strip()

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

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        elif choice == "7":
            sort_students()
            
        elif choice == "8":
            calculate_average()
        
        elif choice == "9":
            find_topper()
            
        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
