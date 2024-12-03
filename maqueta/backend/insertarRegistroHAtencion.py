import mysql.connector

def insert_varibles_into_f_h_atencion(id, f_de, f_hasta, h_de, h_hasta):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO f_h_atencion (id, f_de, f_hasta, h_de, h_hasta) VALUES (%s, %s,%s, %s, %s) """
        record = (id, f_de, f_hasta, h_de, h_hasta)
        cursor.execute(mySql_insert_query, record)
        
        
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into f_h_atencion table")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



respuesta = int(input("Ingrese la cantidad de horarios que desea insertar en la BD: "))
for i in range(respuesta):
    id = int(input("Ingrese el id del horario: "))
    f_de = input("Ingrese el dia de atencion que inicia: ")
    f_hasta = input("Ingrese el dia de atencion que cierra: ")
    h_de = input("Ingrese el horario de atencion que inicia: ")
    h_hasta = input("Ingrese el horario de atencion que cierra: ")
    insert_varibles_into_f_h_atencion(id, f_de,f_hasta, h_de, h_hasta)
    print("*************************************************")