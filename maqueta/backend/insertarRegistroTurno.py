import mysql.connector

def insert_varibles_into_turno(turno_id, cliente_id, servicio_id, fecha, hora):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO turno (turno_id, cliente_id, servicio_id, fecha, hora) VALUES (%s, %s, %s, %s, %s) """
        record = (turno_id, cliente_id, servicio_id, fecha, hora)
        cursor.execute(mySql_insert_query, record)
        
        
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into turno table")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



respuesta = int(input("Ingrese la cantidad de turnos que desea insertar en la BD: "))
for i in range(respuesta):
    turno_id = input("Ingrese el id del turno: ")
    cliente_id = int(input("Seleccione el numero de cliente: "))
    servicio_id = int(input("Seleccione el numero de servicio: "))
    fecha = input("Seleccione la fecha: ")
    hora = input("Seleccione la hora: ")
    
    
    insert_varibles_into_turno(turno_id, cliente_id, servicio_id, fecha, hora)
    print("*************************************************")