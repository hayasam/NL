
from flask import Flask
import psycopg2
from psycopg2 import pool
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    try:
        connection_pool = psycopg2.pool.SimpleConnectionPool(
            1, 20,
            host=get_server_name(),
            database=get_database_name(),
            user=get_database_user(),
            password=get_database_password()
        )
        return connection_pool.getconn()
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def get_server_name():
    return os.getenv('DB_SERVER', 'localhost')

def get_database_name():
    return os.getenv('DB_NAME', 'mydatabase')

def get_database_user():
    return os.getenv('DB_USER', 'postgres')

def get_database_password():
    return os.getenv('DB_PASSWORD', '')

if __name__ == '__main__':
    app.run(debug=True)
