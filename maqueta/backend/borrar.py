import mysql.connector 
import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
    #para eliminar el cliente primero eliminamos el auto:
    
    #eliminamos un usuario, para ello debemos eliminar primero el cliente
    mySql_insert_query = " DELETE FROM cliente WHERE cliente_id = '5';"
    #mySql_insert_query = " DELETE FROM users WHERE user_id = '5';"
 
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "registro(s) borrado") 
except mysql.connector.Error as error:
    print("Failed to delete record into MySQL table {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
