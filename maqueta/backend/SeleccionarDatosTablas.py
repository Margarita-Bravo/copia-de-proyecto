import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
    
    # Tabla users con usuarios que contengan "ri" en su nombre:
    # mySql_query = "select * from users where first_name like '%ri%'"

    # Tabla empleados con empleados cuyo cargo es "Gerencia de Servicio":
    #mySql_query = "select * from empleado where cargo = 'Gerencia de Servicio'"

    # Tabla autos, mostrar autos de año de fabricacion mayor a 2006:
    #mySql_query = "select * from auto where ano_fabricacion > 2006"

    # Tabla detalle_factura donde el monto de la factura es de 14000:
    #mySql_query = "select * from detalle_factura where monto = 14000"

    # Nombre del servicio ofrecido por la factura con el monto de 14000:
    #mySql_query = "select nombre from servicios inner join detalle_factura on detalle_factura.monto = 14000 and detalle_factura.servicio_id = servicios.servicio_id"

    # Nombre del servicio ofrescido por los presupuestos mayores a 12000:
    #mySql_query = "select nombre from servicios inner join detalle_presupuesto on servicios.servicio_id = detalle_presupuesto.servicio_id and detalle_presupuesto.monto > 12000"

    # Tabla de empleados, cargo de los que cumplen horario de 9 a 18hs
    #mySql_query = "select cargo from empleado where horario = '9-18'"

    # Tabla presupuesto fechas de los presupuestos al dominio gfd579:
    #mySql_query = "select fecha from presupuesto where dominio_id = 'gfd579'"

    # Tabla servicios descripcion del servicio denominado 'Mantenimiento integral':
    #mySql_query = "select descripcion from servicios where nombre = 'Mantenimiento integral'"

    #Tabla sucursal direccion de la Sucursal San Martin:
    #mySql_query = "select direccion from sucursal where nombre = 'Sucursal San Martin'"

    #Tabla turno, que servicio se hara el turno del 2025-10-21 a las 15hs:
    mySql_query = "select nombre from servicios inner join turno on servicios.servicio_id = turno.servicio_id and turno.fecha ='2025-10-21' and turno.hora = 15"

  
    cursor = connection.cursor()
    cursor.execute(mySql_query)
 
    rows=cursor.fetchall()
    for row in rows:
        print(row)
 
    cursor.close()
except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
