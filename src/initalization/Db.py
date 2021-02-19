import psycopg2
from psycopg2._psycopg import OperationalError

class Db(object):

    db_name = "yakushevdb"
    db_user = "yakushev"
    db_password = "Yakush#44"
    db_host = "192.168.2.115"
    db_port = "5432"
    connection = None

    def __init__(self):

        # дефаултный коннект
        self.connection = None
        try:
            self.connection = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
         #

    def create_connection(self, db_name, db_user, db_password, db_host, db_port = 5432):
        connection = None
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return connection

    def select_data(self, cursor, schema, table, fieldname):
        list = []
        cursor.execute('SELECT "' + fieldname +
                       '" FROM ' + schema +
                       '."' + table +
                       '" WHERE NOT "login" IS NULL')
        rows = cursor.fetchall()
        for row in rows:
            list.append(f"{row['login']}")

        print("Operation done successfully")
        return list

    def close_connection(self):
        self.close()
