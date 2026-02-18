
import base64
import mysql.connector
from mysql.connector import Error

def upload_image(image_file, image_name):
    try:
        # Read and convert image to base64
        image_data = image_file.read()
        base64_string = base64.b64encode(image_data).decode('utf-8')
        
        # Database connection
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database',
            user='your_username',
            password='your_password'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Insert into database
            insert_query = """
                INSERT INTO images (image_name, image_data)
                VALUES (%s, %s)
            """
            cursor.execute(insert_query, (image_name, base64_string))
            connection.commit()
            
            print("Image uploaded successfully")
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
