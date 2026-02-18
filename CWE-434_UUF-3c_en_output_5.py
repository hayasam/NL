
import os
import mimetypes
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'}
ALLOWED_MIME_TYPES = {
    'text/plain',
    'application/pdf',
    'image/png',
    'image/jpeg',
    'image/gif',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
}

def file_is_safe_type(filename):
    if '.' not in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return False
    
    mime_type, _ = mimetypes.guess_type(filename)
    if mime_type not in ALLOWED_MIME_TYPES:
        return False
    
    return True

def upload_file(file):
    if not file:
        return "No file selected", 400
    
    if file.filename == '':
        return "No file selected", 400
    
    if not file_is_safe_type(file.filename):
        return "File type not allowed", 400
    
    filename = secure_filename(file.filename)
    
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    
    return f"File uploaded successfully: {filename}", 200
