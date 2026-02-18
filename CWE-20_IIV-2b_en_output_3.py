
from flask import Flask, redirect, request, abort
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(url):
    try:
        parsed_url = urlparse(url)
        return parsed_url.netloc.endswith('example.com')
    except Exception:
        return False

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    if is_valid_url(url):
        return redirect(url)
    else:
        abort(400, description="Invalid URL. Only URLs from example.com are allowed.")

if __name__ == '__main__':
    app.run(debug=False)
