
from db import get_connection

connection = get_connection()

if connection:
    cursor = connection.cursor()

    try:
        student_id = int(input("Enter student ID to delete: "))

        # Check whether the student exists
        cursor.execute(
            "SELECT * FROM students WHERE id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student:
            confirm = input(
                f"Delete student {student[1]}? (yes/no): "
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
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")

    except Exception as e:
        connection.rollback()
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()
