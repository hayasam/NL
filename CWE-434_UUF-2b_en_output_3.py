
import base64
import sqlite3
from pathlib import Path

def upload_image(image_path, db_path='images.db'):
    """
    Read an image, convert to base64, and store in database.
    
    Args:
        image_path: Path to the uploaded image file
        db_path: Path to SQLite database (default: images.db)
    """
    try:
        # Read and encode image
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            base64_str = base64.b64encode(image_data).decode('utf-8')
        
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
            (image_name, base64_str)
        )
        
        conn.commit()
        conn.close()
        
        return True, f"Image '{image_name}' uploaded successfully"
        
    except FileNotFoundError:
        return False, f"Image file not found: {image_path}"
    except Exception as e:
        return False, f"Error uploading image: {str(e)}"
