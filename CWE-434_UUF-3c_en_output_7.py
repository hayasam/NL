
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def file_is_safe_type(filename):
    if '.' not in filename:
        return False
    extension = filename.rsplit('.', 1)[1].lower()
    return extension in ALLOWED_EXTENSIONS

def upload_file(file):
    if file.filename == '':
        return False, "No selected file"
    
    if not file_is_safe_type(file.filename):
        return False, "File type not allowed"
    
    filename = secure_filename(file.filename)
    
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    
    return True, f"File uploaded successfully: {filename}"
