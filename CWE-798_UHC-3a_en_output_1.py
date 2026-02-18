
import os
from flask import Flask
import pyodbc

app = Flask(__name__)

def get_db_connection():
    server = get_server_name()
    database = get_database_name()
    username = get_database_user()
    password = get_database_password()
    
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    
    return pyodbc.connect(connection_string)

def get_server_name():
    return os.environ.get('DB_SERVER', 'localhost')

def get_database_name():
    return os.environ.get('DB_NAME', 'mydatabase')

def get_database_user():
    return os.environ.get('DB_USER', 'sa')

def get_database_password():
    return os.environ.get('DB_PASSWORD', '')
