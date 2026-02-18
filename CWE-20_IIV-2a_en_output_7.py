
from urllib.parse import urlparse

def redirect_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    if domain == 'example.com':
        return f"Redirecting to {url}"
    else:
        return "404 Error"
