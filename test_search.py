
from db import get_connection

connection = get_connection()

if connection:
    cursor = connection.cursor()

    student_id = int(input("Enter student ID to search: "))

    query = "SELECT * FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if student:
        print("\nStudent found!")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Marks: {student[2]}")
    else:
        print("Student not found.")

    cursor.close()
    connection.close()
