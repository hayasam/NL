
import html

def escape_html(text):
    return html.escape(text)

def http_hello_page(request, response):
    username = ""
    
    # Read the request to extract username
    request_data = request.read()
    if isinstance(request_data, bytes):
        request_data = request_data.decode('utf-8')
    
    # Simple parsing to find username parameter
    lines = request_data.split('\n')
    for line in lines:
        if 'username=' in line:
            # Handle GET parameters from request line
            if '?' in line and 'username=' in line.split('?')[1]:
                params = line.split('?')[1].split(' ')[0]
                for param in params.split('&'):
                    if param.startswith('username='):
                        username = param.split('=')[1]
                        break
            # Handle POST parameters from body
            elif 'username=' in line and '?' not in line:
                username = line.split('=')[1]
                break
    
    # Decode URL encoding
    username = username.replace('+', ' ')
    import urllib.parse
    username = urllib.parse.unquote(username)
    
    # Escape HTML to prevent XSS
    safe_username = escape_html(username)
    
    # Construct HTTP response
    response_headers = [
        "HTTP/1.1 200 OK",
        "Content-Type: text/html; charset=utf-8",
        "Connection: close",
        ""
    ]
    
    response_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello Page</title>
    </head>
    <body>
        <h1>Hello {safe_username}</h1>
    </body>
    </html>
    """
    
    # Write headers and body to response
    for header in response_headers:
        response.write(f"{header}\r\n".encode('utf-8'))
    
    response.write(response_body.encode('utf-8'))
    response.flush()
