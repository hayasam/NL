
import subprocess
from flask import Flask

app = Flask(__name__)
url = "example.com"

@app.route('/ping')
def ping():
    result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True)
    return result.stdout
