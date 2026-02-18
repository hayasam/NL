
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
            filetype VARCHAR(50) NOT NULL,
            image_data LONGBLOB NOT NULL,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")

def insert_image(image_path):
    """Insert image into database"""
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found")
        return False
    
    try:
        # Read image file
        with open(image_path, 'rb') as file:
            image_data = file.read()
        
        # Get file info
        filename = os.path.basename(image_path)
        filetype = os.path.splitext(filename)[1].lower()
        
        # Connect to database
        connection = create_connection()
        if connection is None:
            return False
        
        # Create table if needed
        create_table(connection)
        
        # Insert image
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO images (filename, filetype, image_data)
        VALUES (%s, %s, %s)
        """
        
        cursor.execute(insert_query, (filename, filetype, image_data))
        connection.commit()
        
        print(f"Image '{filename}' inserted successfully. ID: {cursor.lastrowid}")
        
        cursor.close()
        connection.close()
        return True
        
    except Error as e:
        print(f"Error inserting image: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python store_image.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    insert_image(image_path)

if __name__ == "__main__":
    main()
