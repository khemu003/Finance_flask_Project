import mysql.connector
import os

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            database=os.getenv("name"),
            port=int(os.getenv("port", 3306))
        )
        print("Connected to database successfully!")
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None
