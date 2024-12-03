import mysql.connector

def insert_varibles_into_empleado(empleado_id, cargo, horario, user_id):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO empleado (empleado_id, cargo, horario, user_id) VALUES (%s, %s, %s, %s) """
        record = (empleado_id, cargo, horario, user_id)
        cursor.execute(mySql_insert_query, record)
        
        
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into empleado table")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# insert_varibles_into_empleado(1,'Mecanico','9-18','2')

respuesta = int(input("Ingrese la cantidad de empleados que desea insertar en la BD: "))
for i in range(respuesta):
    empleado_id = int(input("Ingrese el id del empleado: "))
    cargo = input("Ingrese el cargo del empleado: ")
    horario = input("Ingrese el horario que tiene el empleado: ")
    user_id = input("Ingrese el id de usuario del empleado: ")
    insert_varibles_into_empleado(empleado_id, cargo, horario, user_id)
    print("*************************************************")



