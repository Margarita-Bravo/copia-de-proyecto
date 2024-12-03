import mysql.connector

def insert_varibles_into_detalle_presupuesto(id, presupuesto_id, servicio_id, monto, descripcion):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO detalle_presupuesto (id, presupuesto_id, servicio_id, monto, descripcion) VALUES (%s, %s, %s, %s, %s) """
        record = (id, presupuesto_id, servicio_id, monto, descripcion)
        cursor.execute(mySql_insert_query, record)
        
        
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into presupuesto table")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



respuesta = int(input("Ingrese la cantidad de presupuestos que desea insertar en la BD: "))
for i in range(respuesta):
    id = int(input("Ingrese el id del detalle: "))
    presupuesto_id = int(input("Ingrese el id del presupuesto: "))
    
    servicio_id = input("Ingrese el id del servicio: ")
    monto = float(input("Ingrese el precio del servicio: "))
    descripcion = input("Ingrese la descripcion del presupuesto: ")
    
    
    
    insert_varibles_into_detalle_presupuesto(id, presupuesto_id, servicio_id, monto, descripcion)
    print("*************************************************")