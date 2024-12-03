import mysql.connector

def insert_varibles_into_servicios(servicio_id, nombre, descripcion):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO servicios (servicio_id, nombre, descripcion) VALUES (%s, %s, %s) """
        record = (servicio_id, nombre, descripcion)
        cursor.execute(mySql_insert_query, record)
        
        
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into servicios table")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



respuesta = int(input("Ingrese la cantidad de servicios que desea insertar en la BD: "))
for i in range(respuesta):
    servicio_id = int(input("Ingrese el id del servicio: "))
    nombre = input("Ingrese el nombre del servicio: ")
    descripcion = input("Ingrese la descripcion del servicio")
    insert_varibles_into_servicios(servicio_id, nombre, descripcion)
    print("*************************************************")