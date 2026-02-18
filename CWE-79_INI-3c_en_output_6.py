
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/hello/<username>')
def hello(username):
    return f'Hello {escape(username)}'

if __name__ == '__main__':
    app.run()
