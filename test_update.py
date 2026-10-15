
from db import get_connection

connection = get_connection()

if connection:
    cursor = connection.cursor()

    try:
        student_id = int(input("Enter student ID to update: "))
        new_name = input("Enter new name: ").strip()
        new_marks = float(input("Enter new marks: "))

        if not new_name:
            print("Name cannot be empty.")

        elif not 0 <= new_marks <= 100:
            print("Marks must be between 0 and 100.")

        else:
            query = """
                UPDATE students
                SET name = %s, marks = %s
                WHERE id = %s
            """

            values = (new_name, new_marks, student_id)
            cursor.execute(query, values)
            connection.commit()

            if cursor.rowcount > 0:
                print("Student updated successfully!")
            else:
                print("Student not found or no changes made.")

    except ValueError:
        print("Please enter valid numbers for ID and marks.")

    except Exception as e:
        connection.rollback()
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()
