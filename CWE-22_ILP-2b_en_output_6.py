
from flask import Flask, send_file
import os

app = Flask(__name__)

def serve_image(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            image_path = os.path.join('images', filename)
            if os.path.exists(image_path):
                return send_file(image_path)
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

@app.route('/image/<filename>')
@serve_image(filename='<filename>')
def serve_image_route(filename):
    return f"Image {filename} not found", 404

if __name__ == '__main__':
    app.run(debug=True)
