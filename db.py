from decouple import config
import pymysql

def get_connection():
    return pymysql.connect(
        host = config('MYSQL_HOST'),
        database = config('MYSQL_DB'),
        user = config('MYSQL_USER'),
        password = config('MYSQL_PASSWORD')
    )


# Función para insertar un maestro por medio de un procedimiento almacenado:
def agregar_maestro(nombre, ape_paterno, ape_materno, espec, correo, tel):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL agregar_maestro(%s, %s, %s, %s, %s, %s)', (nombre, ape_paterno, ape_materno, espec, correo, tel))
            connection.commit()
        connection.close()

    except Exception as ex:
        print('Error')

# Función para actualizar un maestro por medio de un procedimiento almacenado:
def actualizar_maestro(nombre, ape_paterno, ape_materno, espec, correo, tel, id):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL actualizar_maestro(%s, %s, %s, %s, %s, %s, %s)', (nombre, ape_paterno, ape_materno, espec, correo, tel, id))
            connection.commit()
        connection.close()

    except Exception as ex:
        print('Error')

# Función para eliminar un maestro por medio de un procedimiento almacenado:
def eliminar_maestro(id):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL eliminar_maestro(%s)', (id))
            connection.commit()
        connection.close()

    except Exception as ex:
        print('Error')

# Función para consultar el registro de un maestro por medio de un procedimiento almacenado:
def consultar_maestro(id):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL consultar_maestro(%s)', (id))
            result = curso.fetchall()
        connection.close()
        return result

    except Exception as ex:
        print('Error')

# Función para consultar una lista de maestros por medio de un procedimiento almacenado:
def consultar_maestros():
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('CALL consultar_maestros()')
            result = curso.fetchall()
        connection.close()
        return result

    except Exception as ex:
        print('Error')