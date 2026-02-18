
import re
from urllib.parse import parse_qs, urlparse

def handle_request(environ):
    query_string = environ.get('QUERY_STRING', '')
    query_params = parse_qs(query_string)
    
    target = query_params.get('target', [''])[0]
    
    pattern = r'^[a-zA-Z0-9\-]+\..+'
    
    if re.match(pattern, target):
        redirect_url = target
    else:
        redirect_url = '/'
    
    return f'302 Found', [('Location', redirect_url)], b''
