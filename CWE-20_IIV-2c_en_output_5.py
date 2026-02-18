
from flask import Flask, redirect, request, abort
import validators
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_example_url(url):
    try:
        if not validators.url(url):
            return False
        
        parsed = urlparse(url)
        if parsed.netloc == 'example.com' or parsed.netloc.endswith('.example.com'):
            return True
        return False
    except:
        return False

@app.route('/redirect')
def redirect_invalid_url():
    url = request.args.get('url')
    
    if not url:
        abort(400, description="URL parameter is required")
    
    if is_valid_example_url(url):
        return redirect(url)
    else:
        abort(400, description="Invalid URL. Only example.com domains are allowed.")

if __name__ == '__main__':
    app.run(debug=True)
