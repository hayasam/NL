
from flask import Flask, send_file
import os

app = Flask(__name__)

def serve_image_from_folder(folder_path):
    def decorator(func):
        def wrapper(filename):
            file_path = os.path.join(folder_path, filename)
            if os.path.exists(file_path):
                return send_file(file_path)
            return func(filename)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

@app.route('/images/<filename>')
@serve_image_from_folder('images')
def serve_image(filename):
    return f"Image {filename} not found", 404

if __name__ == '__main__':
    app.run(debug=True)
