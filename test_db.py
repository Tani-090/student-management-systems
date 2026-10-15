from db import get_connection
connection=get_connection()

if connection:
    print("Database test passed!")
    connection.close()
    print("Connection closed")
else:
    print("Please check your MYSQL settings.")        