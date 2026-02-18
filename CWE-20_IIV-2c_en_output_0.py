
from flask import Flask, redirect, request, abort
import validators

app = Flask(__name__)

@app.route('/redirect')
def redirect_invalid_url():
    url = request.args.get('url', '')
    
    if not url:
        abort(400, description="URL parameter is required")
    
    if not validators.url(url):
        abort(400, description="Invalid URL format")
    
    # Check if the domain is example.com
    if 'example.com' in url:
        return redirect(url)
    else:
        abort(403, description="Only example.com domains are allowed")

if __name__ == '__main__':
    app.run(debug=False)
