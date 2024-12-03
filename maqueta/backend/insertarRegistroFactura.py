import mysql.connector

def insert_varibles_into_factura(factura_id, fecha, sucursal_id):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO factura (factura_id, fecha, sucursal_id) VALUES (%s, %s, %s) """
        record = (factura_id, fecha, sucursal_id)
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



respuesta = int(input("Ingrese la cantidad de facturas que desea insertar en la BD: "))
for i in range(respuesta):
    factura_id = int(input("Ingrese el id de la factura: "))
    fecha = input("Ingrese la fecha de la factura: ")
    sucursal_id = int(input("Ingrese el id de la sucursal: "))
    insert_varibles_into_factura(factura_id, fecha, sucursal_id)
    print("*************************************************")
