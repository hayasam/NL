
import base64
import sqlite3
from pathlib import Path

def upload_image(image_path, db_path='images.db'):
    """
    Read an image, convert to base64, and store in database.
    
    Args:
        image_path (str): Path to the uploaded image file
        db_path (str): Path to SQLite database file
    """
    try:
        # Read and encode image
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            base64_string = base64.b64encode(image_data).decode('utf-8')
        
        # Extract image name
        image_name = Path(image_path).name
        
        # Connect to database and insert
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                data TEXT NOT NULL,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert image data
        cursor.execute(
            'INSERT INTO images (name, data) VALUES (?, ?)',
            (image_name, base64_string)
        )
        
        conn.commit()
        conn.close()
        
        print(f"Image '{image_name}' uploaded successfully.")
        
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
    except Exception as e:
        print(f"Error uploading image: {str(e)}")
