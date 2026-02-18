
import os
import mysql.connector
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        # Create uploads folder if it doesn't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        # Save file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Save filepath to database
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            query = "INSERT INTO pdf_files (filename, filepath) VALUES (%s, %s)"
            cursor.execute(query, (filename, filepath))
            conn.commit()
            
            file_id = cursor.lastrowid
            cursor.close()
            conn.close()
            
            return jsonify({
                'message': 'File uploaded successfully',
                'file_id': file_id,
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
        
        query = "SELECT filename, filepath FROM pdf_files WHERE id = %s"
        cursor.execute(query, (file_id,))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if result and os.path.exists(result['filepath']):
            return send_file(
                result['filepath'],
                as_attachment=True,
                download_name=result['filename']
            )
        else:
            return jsonify({'error': 'File not found'}), 404
            
    except mysql.connector.Error as err:
        return jsonify({'error': f'Database error: {err}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
