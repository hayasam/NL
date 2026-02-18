
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

def save_filepath_to_db(filepath):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = "INSERT INTO pdf_files (filepath) VALUES (%s)"
    cursor.execute(query, (filepath,))
    
    connection.commit()
    cursor.close()
    connection.close()

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
        
        # Save file to uploads folder
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Save filepath to database
        save_filepath_to_db(filepath)
        
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename,
            'filepath': filepath
        }), 200
    
    return jsonify({'error': 'Invalid file type. Only PDF files are allowed.'}), 400

@app.route('/download_pdf/<int:file_id>', methods=['GET'])
def download_pdf(file_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT filepath FROM pdf_files WHERE id = %s"
    cursor.execute(query, (file_id,))
    result = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if result and os.path.exists(result['filepath']):
        return send_file(
            result['filepath'],
            as_attachment=True,
            download_name=os.path.basename(result['filepath'])
        )
    
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
