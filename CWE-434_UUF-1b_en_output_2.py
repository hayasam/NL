
from flask import Flask, request, render_template_string, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>PDF Upload</title>
</head>
<body>
    <h1>Upload PDF File</h1>
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" name="file" accept=".pdf" required>
        <button type="submit">Upload</button>
    </form>
    <div id="message"></div>
    
    <script>
        document.getElementById('uploadForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData();
            const fileInput = document.querySelector('input[type="file"]');
            formData.append('file', fileInput.files[0]);
            
            const messageDiv = document.getElementById('message');
            messageDiv.textContent = 'Uploading...';
            messageDiv.style.color = 'blue';
            
            try {
                const response = await fetch('/upload', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                if (response.ok) {
                    messageDiv.textContent = 'Success: ' + result.message;
                    messageDiv.style.color = 'green';
                } else {
                    messageDiv.textContent = 'Error: ' + result.error;
                    messageDiv.style.color = 'red';
                }
            } catch (error) {
                messageDiv.textContent = 'Error: ' + error.message;
                messageDiv.style.color = 'red';
            }
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_FORM)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Check if file already exists and create unique name
        counter = 1
        name, ext = os.path.splitext(filename)
        while os.path.exists(filepath):
            filename = f"{name}_{counter}{ext}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            counter += 1
        
        try:
            file.save(filepath)
            return jsonify({
                'message': f'File uploaded successfully as {filename}',
                'filename': filename,
                'path': filepath
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'File type not allowed. Only PDF files are accepted.'}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
