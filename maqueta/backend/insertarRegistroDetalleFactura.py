import mysql.connector

def insert_varibles_into_detalle_factura(factura_id, servicio_id, monto, descripcion):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO detalle_factura (factura_id, servicio_id, monto, descripcion) VALUES (%s, %s, %s, %s) """
        record = (factura_id, servicio_id, monto, descripcion)
        cursor.execute(mySql_insert_query, record)
        
        
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into detalle_factura table")
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
    servicio_id = int(input("Ingrese el id del servicio: "))
    monto = float(input("Ingrese el monto de la factura: "))
    descripcion = input("Ingrese la descripcion de la factura: ")
    
    insert_varibles_into_detalle_factura(factura_id, servicio_id, monto, descripcion)
    print("*************************************************")