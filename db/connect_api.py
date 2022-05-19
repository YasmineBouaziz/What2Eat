# API endpoint to SQL databse
import mysql.connector
from mysql.connector import Error
from config import USER, PASSWORD, HOST


def _connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin="mysql_native_password",
            database="What2Eat",
        )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print(f"connected to MYSQL Server version {db_Info}")
            cursor = connection.cursor()
            # cursor.execute("select database();")
            cursor.execute("SELECT name FROM course WHERE id = 4;")
            for row in cursor.fetchall():
                print(row[0])
            # record = cursor.fetchone()
            # print(f"You're connected to database {record}")

    except Error as e:
        print(f"Error while connecting to MYSQL {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MYSQL connection is closed")


if __name__ == "__main__":
    _connect_to_db()
