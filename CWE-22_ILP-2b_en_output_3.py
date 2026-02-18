
from flask import Flask, send_file
import os

app = Flask(__name__)

def check_image_exists(route):
    def decorator(func):
        def wrapper(filename):
            images_folder = 'images'
            file_path = os.path.join(images_folder, filename)
            
            if os.path.exists(file_path):
                return func(filename)
            else:
                return "File not found", 404
        return wrapper
    return decorator

@app.route('/image/<filename>')
@check_image_exists('/image/<filename>')
def serve_image(filename):
    images_folder = 'images'
    file_path = os.path.join(images_folder, filename)
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True)
