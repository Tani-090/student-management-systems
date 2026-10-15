from db import get_connection
connection=get_connection()

if connection:
    cursor=connection.cursor()
    
    query= """
         INSERT INTO students (id,name,marks)
         Values(%s,%s,%s)
    """     
         
    values=(501,"Mina",88.5)
    
try:
    cursor.execute(query,values)
    connection.commit()
    print("Student inserted successfully")
    
except Exception as e:
    connection.rollback()
    print("Error", e)  
    
finally:
    cursor.close()
    connection.close()    