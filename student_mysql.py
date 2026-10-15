
from db import get_connection


def add_student():
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ").strip()
        marks = float(input("Enter marks: "))

        if not name:
            print("Name cannot be empty.")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
            INSERT INTO students (id, name, marks)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (student_id, name, marks))
        connection.commit()

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numbers.")

    except Exception as e:
        if connection is not None and connection.is_connected():
            connection.rollback()
        print("Error:", e)

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()


def view_students():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("SELECT id, name, marks FROM students")
        students = cursor.fetchall()

        if not students:
            print("No students found.")
            return

        for student in students:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()
        

def search_student():
    try:
        student_id = int(input("Enter student ID to search: "))

        connection = get_connection()
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name, marks FROM students WHERE id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student:
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Marks: {student[2]}")
        else:
            print("Student not found.")

    except ValueError:
        print("Enter a valid student ID.")

    except Exception as e:
        print("Error:", e)

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
        

def update_student():
    connection = None
    cursor = None

    try:
        student_id = int(input("Enter student ID to update: "))
        new_name = input("Enter new name: ").strip()
        new_marks = float(input("Enter new marks: "))

        if not new_name:
            print("Name cannot be empty.")
            return

        if not 0 <= new_marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        connection = get_connection()
        if connection is None:
            return

        cursor = connection.cursor()
        query = """
            UPDATE students
            SET name = %s, marks = %s
            WHERE id = %s
        """

        cursor.execute(query, (new_name, new_marks, student_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully!")
        else:
            print("Student not found or no changes made.")

    except ValueError:
        print("Enter a valid ID and marks.")

    except Exception as e:
        if connection is not None and connection.is_connected():
            connection.rollback()
        print("Error:", e)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


def delete_student():
    connection = None
    cursor = None

    try:
        student_id = int(input("Enter student ID to delete: "))

        connection = get_connection()
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.execute(
            "SELECT name FROM students WHERE id = %s",
            (student_id,)
        )
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        confirm = input(
            f"Delete {student[0]}? Type yes to confirm: "
        ).strip().lower()

        if confirm == "yes":
            cursor.execute(
                "DELETE FROM students WHERE id = %s",
                (student_id,)
            )
            connection.commit()
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Enter a valid student ID.")

    except Exception as e:
        if connection is not None and connection.is_connected():
            connection.rollback()
        print("Error:", e)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


def sort_students():
    connection = None
    cursor = None

    try:
        print("\nSort Students By:")
        print("1. Name (A to Z)")
        print("2. Marks (Highest to Lowest)")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            query = "SELECT id, name, marks FROM students ORDER BY name ASC"

        elif choice == "2":
            query = "SELECT id, name, marks FROM students ORDER BY marks DESC"

        else:
            print("Invalid choice.")
            return

        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()
        cursor.execute(query)
        students = cursor.fetchall()

        if not students:
            print("No students found.")
            return

        print("\n--- Sorted Student List ---")

        for student in students:
            print(
                f"ID: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()




def calculate_average():
    connection = None
    cursor = None

    try:
        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
            SELECT COUNT(*), SUM(marks), AVG(marks)
            FROM students
        """

        cursor.execute(query)
        result = cursor.fetchone()

        total_students = result[0]
        total_marks = result[1] or 0
        average = result[2]

        print(f"Total students: {total_students}")
        print(f"Total marks: {total_marks}")

        if average is not None:
            print(f"Class average: {average:.2f}")
        else:
            print("Class average: No marks available.")

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()
