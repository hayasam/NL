
from flask import Flask
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    server = get_server_name()
    database = get_database_name()
    username = get_database_user()
    password = get_database_password()
    
    connection_string = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    
    try:
        connection = pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as e:
        print(f"Database connection failed: {e}")
        return None

def get_server_name():
    return os.getenv('DB_SERVER', 'localhost')

def get_database_name():
    return os.getenv('DB_NAME', 'mydatabase')

def get_database_user():
    return os.getenv('DB_USER', 'sa')

def get_database_password():
    return os.getenv('DB_PASSWORD', '')

if __name__ == '__main__':
    app.run(debug=True)
