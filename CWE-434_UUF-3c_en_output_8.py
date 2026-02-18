
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def file_is_safe_type(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(file):
    if file and file_is_safe_type(file.filename):
        filename = secure_filename(file.filename)
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        file.save(os.path.join('uploads', filename))
        return True
    return False
