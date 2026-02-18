
import mysql.connector
from mysql.connector import Error
import sys
import os

def store_image_in_db(image_path, host, database, user, password):
    """
    Store an image file in MySQL database.
    
    Args:
        image_path: Path to the image file
        host: MySQL host
        database: Database name
        user: MySQL username
        password: MySQL password
    """
    try:
        # Read image file
        with open(image_path, 'rb') as file:
            image_data = file.read()
        
        # Extract filename
        filename = os.path.basename(image_path)
        
        # Connect to MySQL database
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
            insert_query = """
            INSERT INTO images (filename, image_data)
            VALUES (%s, %s)
            """
            
            cursor.execute(insert_query, (filename, image_data))
            connection.commit()
            
            print(f"Image '{filename}' stored successfully in database.")
            
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
        sys.exit(1)
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def main():
    # Database configuration - modify these values
    DB_CONFIG = {
        'host': 'localhost',
        'database': 'image_database',
        'user': 'your_username',
        'password': 'your_password'
    }
    
    # Check if image path is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python store_image.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    # Validate file exists and is an image (basic check)
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' does not exist.")
        sys.exit(1)
    
    # Check if file has common image extension
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    file_ext = os.path.splitext(image_path)[1].lower()
    
    if file_ext not in image_extensions:
        print(f"Warning: File extension '{file_ext}' is not a common image format.")
        proceed = input("Do you want to continue anyway? (y/n): ")
        if proceed.lower() != 'y':
            print("Operation cancelled.")
            sys.exit(0)
    
    # Store image in database
    store_image_in_db(
        image_path,
        DB_CONFIG['host'],
        DB_CONFIG['database'],
        DB_CONFIG['user'],
        DB_CONFIG['password']
    )

if __name__ == "__main__":
    main()
