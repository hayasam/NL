
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/img')
def img():
    file_path = request.args.get('file')
    if file_path:
        try:
            return send_file(file_path, mimetype='image/jpeg')
        except Exception as e:
            return f"Error: {str(e)}", 404
    return "No file specified", 400

if __name__ == '__main__':
    app.run(debug=True)
