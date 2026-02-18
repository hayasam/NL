
import mysql.connector
from mysql.connector import Error
import sys
import os

def create_connection():
    """Create database connection"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='image_db',
            user='your_username',
            password='your_password'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_table(connection):
    """Create images table if it doesn't exist"""
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS images (
            id INT AUTO_INCREMENT PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            file_data LONGBLOB NOT NULL,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")

def store_image(image_path):
    """Store image in database"""
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return False
    
    connection = create_connection()
    if connection is None:
        return False
    
    create_table(connection)
    
    try:
        filename = os.path.basename(image_path)
        
        with open(image_path, 'rb') as file:
            image_data = file.read()
        
        cursor = connection.cursor()
        insert_query = "INSERT INTO images (filename, file_data) VALUES (%s, %s)"
        
        cursor.execute(insert_query, (filename, image_data))
        connection.commit()
        
        print(f"Image '{filename}' stored successfully with ID: {cursor.lastrowid}")
        cursor.close()
        connection.close()
        return True
        
    except Error as e:
        print(f"Error storing image: {e}")
        if connection:
            connection.close()
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        if connection:
            connection.close()
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python store_image.py <image_file_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    store_image(image_path)

if __name__ == "__main__":
    main()
