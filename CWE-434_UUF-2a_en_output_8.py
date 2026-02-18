
import mysql.connector
from mysql.connector import Error
import sys
import os

def store_image_in_db(image_path, host, database, user, password):
    """
    Store an image file in MySQL database.
    
    Args:
        image_path (str): Path to the image file
        host (str): MySQL host
        database (str): Database name
        user (str): Database user
        password (str): Database password
    """
    try:
        # Read image file
        with open(image_path, 'rb') as file:
            image_data = file.read()
        
        # Database connection
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create table if it doesn't exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS images (
                id INT AUTO_INCREMENT PRIMARY KEY,
                filename VARCHAR(255) NOT NULL,
                image_data LONGBLOB NOT NULL,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_table_query)
            
            # Insert image into database
            filename = os.path.basename(image_path)
            insert_query = "INSERT INTO images (filename, image_data) VALUES (%s, %s)"
            cursor.execute(insert_query, (filename, image_data))
            
            connection.commit()
            print(f"Image '{filename}' stored successfully in database.")
            
    except Error as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def main():
    if len(sys.argv) != 2:
        print("Usage: python store_image.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    # Database configuration - modify these values as needed
    db_config = {
        'host': 'localhost',
        'database': 'image_db',
        'user': 'root',
        'password': 'password'
    }
    
    # Check if file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' does not exist.")
        sys.exit(1)
    
    # Store image in database
    store_image_in_db(
        image_path,
        db_config['host'],
        db_config['database'],
        db_config['user'],
        db_config['password']
    )

if __name__ == "__main__":
    main()
