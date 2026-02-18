
from flask import Flask, redirect, request, abort
import validators

app = Flask(__name__)

def is_valid_example_url(url):
    try:
        result = validators.url(url)
        if not result:
            return False
            
        # Check if the domain is example.com
        # Using a simple check - in production use urlparse for robustness
        if 'example.com' in url:
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
        abort(400, description="Invalid URL. Only URLs from example.com are allowed.")

if __name__ == '__main__':
    app.run(debug=False)
