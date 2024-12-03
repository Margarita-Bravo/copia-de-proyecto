import mysql.connector

def insert_varibles_into_auto(dominio_id, marca, modelo, ano_fabricacion, cliente_id):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO auto (dominio_id, marca, modelo, ano_fabricacion, cliente_id) VALUES (%s, %s, %s, %s, %s) """
        record = (dominio_id, marca, modelo, ano_fabricacion, cliente_id)
        cursor.execute(mySql_insert_query, record)
        
        
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into auto table")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



respuesta = int(input("Ingrese la cantidad de autos que desea insertar en la BD: "))
for i in range(respuesta):
    dominio_id = input("Ingrese el dominio del auto: ")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    ano_fabricacion = input("Ingrese el año de fabricacion del auto: ")
    
    cliente_id = int(input("Seleccione el numero de cliente: "))
    insert_varibles_into_auto(dominio_id, marca, modelo, ano_fabricacion, cliente_id)
    print("*************************************************")