
import base64
import sqlite3
from pathlib import Path

def upload_image(image_path, db_path='images.db'):
    # Read image file
    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Convert to base64
    base64_string = base64.b64encode(image_data).decode('utf-8')
    
    # Get image name
    image_name = Path(image_path).name
    
    # Insert into database
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                data TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insert the image
        cursor.execute('''
            INSERT INTO images (name, data) VALUES (?, ?)
        ''', (image_name, base64_string))
        
        conn.commit()
        print(f"Image '{image_name}' uploaded successfully.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
