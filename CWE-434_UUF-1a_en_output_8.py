
import os
import mysql.connector
from mysql.connector import Error
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'your_database',
    'user': 'your_username',
    'password': 'your_password'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def save_filepath_to_db(filepath):
    connection = get_db_connection()
    if connection is None:
        return False
    
    try:
        cursor = connection.cursor()
        query = "INSERT INTO pdf_files (filepath) VALUES (%s)"
        cursor.execute(query, (filepath,))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Error saving to database: {e}")
        if connection.is_connected():
            connection.close()
        return False

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
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        
        # Save file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Save filepath to database
        if save_filepath_to_db(filepath):
            return jsonify({
                'message': 'File uploaded successfully',
                'filepath': filepath
            }), 200
        else:
            # Clean up file if database save fails
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'error': 'Failed to save file information to database'}), 500
    
    return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400

@app.route('/download_pdf/<int:file_id>', methods=['GET'])
def download_pdf(file_id):
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT filepath FROM pdf_files WHERE id = %s"
        cursor.execute(query, (file_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if result and 'filepath' in result:
            filepath = result['filepath']
            if os.path.exists(filepath):
                return send_file(filepath, as_attachment=True)
            else:
                return jsonify({'error': 'File not found on server'}), 404
        else:
            return jsonify({'error': 'File not found in database'}), 404
    except Error as e:
        print(f"Error retrieving file: {e}")
        if connection.is_connected():
            connection.close()
        return jsonify({'error': 'Database error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
