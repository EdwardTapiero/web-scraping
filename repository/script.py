import mysql.connector


def __connection_db():
    connection = mysql.connector.connect(user='root',
                                         password='root1234',
                                         host='localhost',
                                         database='mercado_libre')
    return connection


def delete_table():
    try:
        connection = __connection_db()

        sql = "DELETE FROM productos"
        sql_alter = "ALTER TABLE productos AUTO_INCREMENT = 1"

        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.execute(sql_alter)
        connection.commit()
        print("Record remove successfully")

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Failed to insert into PostgreSQL table {}".format(error))


def insert_product(marca, referencia, modelo, memoria_int, memoria_ram, precio, ini):
    try:
        connection = __connection_db()

        cursor = connection.cursor()

        sql = "INSERT INTO productos(marca, referencia, modelo, memoria_int, memoria_ram, precio, pagina)" \
              " VALUES (%s,%s,%s,%s,%s,%s,%s)"

        record = (marca, referencia, modelo, memoria_int, memoria_ram, precio, ini)
        cursor.execute(sql, record)
        connection.commit()
        print("Record inserted successfully")

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Failed to insert into PostgreSQL table {}".format(error))


def count_by_brand(brand):
    try:
        connection = __connection_db()

        cursor = connection.cursor()

        record = (brand, )
        sql = "SELECT COUNT(marca) FROM productos WHERE marca = %s"

        cursor.execute(sql, record)
        count = cursor.fetchall()
        cursor.close()
        connection.close()
        count = count[0]
        return int(count[0])

    except mysql.connector.Error as error:
        print("Failed to find into PostgreSQL table {}".format(error))


def max_pag():
    try:
        connection = __connection_db()

        cursor = connection.cursor()

        sql ="SELECT MAX(pagina) FROM productos"

        cursor.execute(sql)
        pag = cursor.fetchall()
        cursor.close()
        connection.close()
        pag = pag[0]

        return int(pag[0])

    except mysql.connector.Error as error:
        print("Failed to find into PostgreSQL table {}".format(error))
