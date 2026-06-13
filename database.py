import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():

    try:

        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=3306,
            cursorclass=pymysql.cursors.DictCursor
        )

        return connection

    except Exception as e:
        print("Error de conexión:", e)
        raise