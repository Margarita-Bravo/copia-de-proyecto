import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',
    database='service_automotor',
    user='root',
    password='1234')
#     mySql_Create_Table_Query = """CREATE TABLE users(
# 	user_id 	VARCHAR(20),
#     first_name	VARCHAR(200),
#     email		VARCHAR(50),
#     pass		VARCHAR(20),
#     telefono	VARCHAR(20),
#     cuil		VARCHAR(20),

#     CONSTRAINT PK_usuario PRIMARY KEY(user_id)
# ); """

    # mySql_Create_Table_Query = """CREATE TABLE empleado(
	# empleado_id 	INT NOT NULL AUTO_INCREMENT,
    # cargo			VARCHAR(200),
    # horario			VARCHAR(50),
    # user_id			VARCHAR(20),

    # CONSTRAINT PK_empleado PRIMARY KEY(empleado_id),
    # CONSTRAINT FK_emp_user FOREIGN KEY (user_id) REFERENCES users(user_id)
    # ); """

    # mySql_Create_Table_Query = """create table cliente (
	# cliente_id int not null auto_increment,
    # user_id		varchar(20),
    
    # constraint PK_cliente primary key(cliente_id),
    # constraint FK_cli_user foreign key (USER_ID) references users(user_id)
    # );"""

    # mySql_Create_Table_Query = """create table f_h_atencion(
	# id 	int not null auto_increment,
    # f_de			varchar(10),
    # f_hasta			varchar(10),
    # h_de			varchar(10),
    # h_hasta			varchar(10),
    
    # constraint PK_atencion primary key(id)
    # ); """

    # mySql_Create_Table_Query = """create table sucursal(
	# sucursal_id	int not null auto_increment,
    # nombre		varchar(50),
    # direccion	varchar(200),
    # telefono	varchar(20),
    # mail		varchar(20),
    # cuit		varchar(10),
    # f_h_atencion	int,
    
    # constraint PK_sucursal primary key(sucursal_id),
    # constraint FK_suc_aten foreign key(f_h_atencion) references f_h_atencion(id)
    # );"""

    # mySql_Create_Table_Query = """create table servicios(
	# servicio_id int not null auto_increment,
    # nombre		varchar(50),
    # descripcion	varchar(100),
    
    #  constraint PK_servicios primary key(servicio_id)
    # );""" 

    # mySql_Create_Table_Query = """create table auto(
	# dominio_id		varchar(20),
    # marca			varchar(20),
    # modelo			varchar(20),
    # ano_fabricacion	varchar(4),
    # cliente_id		int,
    
    # constraint PK_auto primary key(dominio_id),
    # constraint FK_auto_client foreign key(cliente_id) references cliente(cliente_id)
    # );"""

    # mySql_Create_Table_Query = """create table turno(
	# turno_id		int not null auto_increment,
    # cliente_id		int,
    # servicio_id		int,
    # fecha			date,
    # hora			varchar(5),
    
    # constraint PK_turno primary key(turno_id),
    # constraint FK_tur_cli foreign key(cliente_id) references cliente(cliente_id),
    # constraint FK_tur_ser foreign key(servicio_id) references servicios(servicio_id)
    # );"""

    # mySql_Create_Table_Query = """create table presupuesto(
	# presupuesto_id		int not null auto_increment,
    # fecha				date,
    # dominio_id			varchar(20),
    # cliente_id			int,
    # empleado_id			int,
    # sucursal_id			int,
    
    # constraint PK_presupuesto primary key(presupuesto_id),
    # constraint FK_pre_auto foreign key(dominio_id) references auto(dominio_id),
    # constraint FK_pre_cli foreign key(cliente_id) references cliente(cliente_id),
    # constraint FK_pre_emp foreign key(empleado_id) references empleado(empleado_id),
    # constraint FK_pre_suc foreign key(sucursal_id) references sucursal(sucursal_id)
    # );"""

    # mySql_Create_Table_Query = """create table detalle_presupuesto(
	# id					int not null auto_increment,
    # presupuesto_id		int,
    # servicio_id			int,
    # monto				double,
    # descripcion			varchar(100),
    
    # constraint PK_detalle primary key(id),
    # constraint FK_detpre_pre foreign key(presupuesto_id) references presupuesto(presupuesto_id),
    # constraint FK_detpre_ser foreign key(servicio_id) references servicios(servicio_id)
    # );"""

    # mySql_Create_Table_Query = """create table factura(
	# factura_id		int not null auto_increment,
    # fecha			date,
    # sucursal_id		int,
    
    # constraint PK_factura primary key(factura_id),
    # constraint FK_fac_suc foreign key(sucursal_id) references sucursal(sucursal_id)
    # );"""

    mySql_Create_Table_Query = """create table detalle_factura(
	factura_id		int,
    servicio_id			int,
    monto				double,
    descripcion			varchar(100),
    
    constraint FK_detfac_fac foreign key(factura_id) references factura(factura_id),
    constraint FK_detfac_ser foreign key(servicio_id) references servicios(servicio_id)
    );"""
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("tabla creada con éxito,,!! ")
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")