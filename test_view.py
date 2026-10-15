
from db import get_connection

connection = get_connection()

if connection:
    cursor = connection.cursor()

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    print("\n--- Students from MySQL ---")

    for student in students:
        print(
            f"ID: {student[0]}, "
            f"Name: {student[1]}, "
            f"Marks: {student[2]}"
        )

    cursor.close()
    connection.close()
