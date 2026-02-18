
import mysql.connector
from mysql.connector import Error
import sys
import os

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        filename VARCHAR(255) NOT NULL,
        image_data LONGBLOB NOT NULL,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_image(connection, filepath):
    filename = os.path.basename(filepath)
    
    try:
        with open(filepath, 'rb') as file:
            image_data = file.read()
    except IOError as e:
        print(f"Error reading file: {e}")
        return
    
    insert_query = """
    INSERT INTO images (filename, image_data)
    VALUES (%s, %s)
    """
    
    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, (filename, image_data))
        connection.commit()
        print(f"Image '{filename}' inserted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_file_path>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    if not os.path.exists(filepath):
        print(f"File '{filepath}' does not exist")
        sys.exit(1)
    
    connection = create_connection()
    if connection:
        create_table(connection)
        insert_image(connection, filepath)
        connection.close()

if __name__ == "__main__":
    main()
