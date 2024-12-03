import mysql.connector

def insert_varibles_into_presupuesto(presupuesto_id, fecha, dominio_id, cliente_id, empleado_id, sucursal_id):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO presupuesto (presupuesto_id, fecha, dominio_id, cliente_id, empleado_id, sucursal_id) VALUES (%s, %s, %s, %s, %s, %s) """
        record = (presupuesto_id, fecha, dominio_id, cliente_id, empleado_id, sucursal_id)
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
    presupuesto_id = int(input("Ingrese el id del presupuesto: "))
    fecha = input("Seleccione la fecha: ")
    dominio_id = input("Ingrese el numero de dominio: ")
    cliente_id = int(input("Seleccione el numero de cliente: "))
    empleado_id = int(input("Seleccione el numero de empleado: "))
    sucursal_id = int(input("Seleccione el numero de sucursal: "))
    
    
    
    insert_varibles_into_presupuesto(presupuesto_id, fecha, dominio_id, cliente_id, empleado_id, sucursal_id)
    print("*************************************************")