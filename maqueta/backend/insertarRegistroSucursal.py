import mysql.connector

def insert_varibles_into_sucursal(sucursal_id, nombre, direccion, telefono, mail, cuit, f_h_atencion):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO sucursal (sucursal_id, nombre, direccion, telefono, mail, cuit, f_h_atencion) VALUES (%s, %s, %s, %s, %s, %s, %s) """
        record = (sucursal_id, nombre, direccion, telefono, mail, cuit, f_h_atencion)
        cursor.execute(mySql_insert_query, record)
        
        
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into sucursal table")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



respuesta = int(input("Ingrese la cantidad de sucursales que desea insertar en la BD: "))
for i in range(respuesta):
    sucursal_id = int(input("Ingrese el id de la sucursal: "))
    nombre = input("Ingrese el nombre de la sucursal: ")
    direccion = input("Ingrese la direccion de la sucursal: ")
    telefono = input("Ingrese el numero de telefono de la sucursal: ")
    mail = input("Ingrese el mail de la sucursal: ")
    cuit = input("Ingrese el cuit de la sucursal: ")
    f_h_atencion = int(input("Seleccione el horario de la sucursal: "))
    insert_varibles_into_sucursal(sucursal_id, nombre, direccion, telefono, mail, cuit, f_h_atencion)
    print("*************************************************")


