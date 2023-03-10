from decouple import config
import pymysql

def get_connection():
    return pymysql.connect(
        host = config('MYSQL_HOST'),
        database = config('MYSQL_DB'),
        user = config('MYSQL_USER'),
        password = config('MYSQL_PASSWORD')
    )