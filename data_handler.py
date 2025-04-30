import mysql.connector
import bcrypt
import pandas as pd
from database import get_db_connection

def register_user(username, password):
    conn = get_db_connection()
    if conn is None:
        print("Error: Database connection failed.")
        return False

    cursor = conn.cursor()
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        print("User registered successfully.")
        return True
    except mysql.connector.IntegrityError:
        print("Error: Username already exists.")
        return False
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


def authenticate_user(username, password):
    conn = get_db_connection()
    if conn is None:
        print("Error: Database connection failed.")
        return False
    
    cursor = conn.cursor()
    query = "SELECT user_id, password FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
        return user[0]
    else:
        print("Invalid credentials.")
        return None
    cursor.close()
    conn.close()


def fetch_transactions(user_id):
    conn = get_db_connection()
    query = "SELECT id, date, category, amount, type, description FROM transactions WHERE user_id = %s"
    df = pd.read_sql(query, conn, params=(user_id,))
    conn.close()
    return df

def add_transaction(user_id, date, category, amount, txn_type, description):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO transactions (user_id, date, category, amount, type, description) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (user_id, date, category, amount, txn_type, description))
    conn.commit()
    cursor.close()
    conn.close()

def delete_transaction(user_id, transaction_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM transactions WHERE id = %s AND user_id = %s"
    cursor.execute(query, (transaction_id, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def change_transaction(user_id, date, category, amount, txn_type, description, transaction_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """UPDATE transactions 
               SET date = %s, category = %s, amount = %s, type = %s, description = %s 
               WHERE id = %s AND user_id = %s"""
    cursor.execute(query, (date, category, amount, txn_type, description, transaction_id, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def add_contact(name, email, message):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, message))
    conn.commit()
    cursor.close()
    conn.close()


def add_feedback(name, email, feedback):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO feedback (name, email, feedback) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, feedback))
    conn.commit()
    cursor.close()
    conn.close()