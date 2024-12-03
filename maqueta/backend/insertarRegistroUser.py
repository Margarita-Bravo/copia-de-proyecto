import mysql.connector
# try:
#     connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
#     mySql_insert_query = """INSERT INTO users (user_id, first_name, email, pass, telefono, cuil) 
#     VALUES 
#     (1, 'Valeria', 'vale@mail.com', 'valeria1234', '1651646','6646454646') """
#     cursor = connection.cursor()
#     cursor.execute(mySql_insert_query)
#     connection.commit()
#     print(cursor.rowcount, "Record inserted successfully into users table")
#     cursor.close()
# except mysql.connector.Error as error:
#     print("Failed to insert record into users table {}".format(error))
# finally:
#     if connection.is_connected():
#         connection.close()
#         print("MySQL connection is closed")

# try:
#     connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
#     mySql_insert_query = """INSERT INTO users (user_id, first_name, email, pass, telefono, cuil) VALUES (%s, %s, %s, %s, %s, %s) """
#     records_to_insert = [(2, 'Diego', 'diego@mail.com', 'diego1234', '45431654','56445612316'),
#                         (3, 'German', 'german@mail.com', 'german1234', '541216','54564561454'),
#                         (4, 'Elena', 'elena@mail.com', 'elena1234', '545623156','56425565751')]
#     cursor = connection.cursor()
#     cursor.executemany(mySql_insert_query, records_to_insert)
#     connection.commit()
#     print(cursor.rowcount, "Record inserted successfully into users table")
# except mysql.connector.Error as error:
#     print("Failed to insert record into MySQL table {}".format(error))
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

def insert_varibles_into_users(user_id, first_name, email, password, telefono, cuil):
    try:
        connection = mysql.connector.connect(host='localhost',database='service_automotor',user='root',password='1234')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO users (user_id, first_name, email, pass, telefono, cuil) VALUES (%s, %s, %s, %s, %s, %s) """
        record = (user_id, first_name, email, password, telefono, cuil)
        cursor.execute(mySql_insert_query, record)
        
        
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into users table")
    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


insert_varibles_into_users(5, 'Karina', 'karina@mail.com', 'karina1234', '51465489','54564554794')