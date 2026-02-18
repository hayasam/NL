
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/img')
def img():
    name = request.args.get('name')
    if name:
        try:
            return send_file(f'images/{name}')
        except FileNotFoundError:
            return "Image not found", 404
    return "No image name provided", 400

if __name__ == '__main__':
    app.run()
