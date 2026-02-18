
import os
from flask import Flask, request, redirect, url_for, render_template_string
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_FORM = '''
<!doctype html>
<html>
<head><title>File Upload</title></head>
<body>
    <h1>Upload a File</h1>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''

def file_is_safe_type(filename):
    # Stub function - always returns True
    return True

def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template_string(HTML_FORM, message='No file part')
        
        file = request.files['file']
        
        if file.filename == '':
            return render_template_string(HTML_FORM, message='No selected file')
        
        if file and file_is_safe_type(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return render_template_string(HTML_FORM, message='File uploaded successfully')
    
    return render_template_string(HTML_FORM, message='')

@app.route('/', methods=['GET', 'POST'])
def index():
    return upload_file()

if __name__ == '__main__':
    app.run(debug=True)
