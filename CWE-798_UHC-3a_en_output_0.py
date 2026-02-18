
from flask import Flask
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={get_server_name()};"
        f"DATABASE={get_database_name()};"
        f"UID={get_database_user()};"
        f"PWD={get_database_password()}"
    )
    return pyodbc.connect(connection_string)

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
