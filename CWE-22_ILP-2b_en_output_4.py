
from flask import Flask, send_file
import os

app = Flask(__name__)

def serve_image(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            images_folder = 'images'
            file_path = os.path.join(images_folder, filename)
            
            if os.path.exists(file_path):
                return send_file(file_path)
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/image')
@serve_image('example.jpg')
def serve_default_image():
    return "Image not found", 404

if __name__ == '__main__':
    app.run(debug=True)
