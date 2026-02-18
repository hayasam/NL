
import os
import mysql.connector
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Save filepath to database
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Create table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pdf_files (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    filename VARCHAR(255) NOT NULL,
                    filepath VARCHAR(500) NOT NULL,
                    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Insert filepath into database
            query = "INSERT INTO pdf_files (filename, filepath) VALUES (%s, %s)"
            cursor.execute(query, (filename, filepath))
            conn.commit()
            
            cursor.close()
            conn.close()
            
            return jsonify({
                'message': 'File uploaded successfully',
                'filename': filename,
                'filepath': filepath
            }), 200
            
        except mysql.connector.Error as err:
            return jsonify({'error': f'Database error: {err}'}), 500
    
    return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400

@app.route('/download_pdf/<int:file_id>', methods=['GET'])
def download_pdf(file_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Get filepath from database
        query = "SELECT filepath, filename FROM pdf_files WHERE id = %s"
        cursor.execute(query, (file_id,))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if result:
            filepath = result['filepath']
            filename = result['filename']
            
            if os.path.exists(filepath):
                return send_file(
                    filepath,
                    as_attachment=True,
                    download_name=filename,
                    mimetype='application/pdf'
                )
            else:
                return jsonify({'error': 'File not found on server'}), 404
        else:
            return jsonify({'error': 'File not found in database'}), 404
            
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {err}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
