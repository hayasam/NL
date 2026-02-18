
import re
from urllib.parse import parse_qs, urlparse

def handle_request(request):
    pattern = r'^[a-zA-Z0-9\-]+\..+'
    
    # Parse query parameters
    query_params = parse_qs(urlparse(request.path).query)
    target = query_params.get('target', [''])[0]
    
    if re.match(pattern, target):
        return f'Redirect to: {target}'
    else:
        return 'Redirect to: /'
