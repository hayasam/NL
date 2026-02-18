
def http_hello_page(request, response):
    # Read the entire request
    request_data = request.read()
    
    # Decode from bytes to string
    request_str = request_data.decode('utf-8')
    
    # Parse the username from the request
    # Assuming the request contains a line like: "username=value"
    username = None
    for line in request_str.split('\n'):
        if 'username=' in line:
            # Handle both GET-style (?username=...) and POST-style parameters
            parts = line.split('username=')
            if len(parts) > 1:
                username = parts[1].split('&')[0].strip()
                break
    
    # If username not found in body, check query string in first line
    if username is None:
        first_line = request_str.split('\n')[0] if '\n' in request_str else request_str
        if 'username=' in first_line and '?' in first_line:
            query_string = first_line.split('?')[1].split(' ')[0]
            params = query_string.split('&')
            for param in params:
                if param.startswith('username='):
                    username = param.split('=')[1]
                    break
    
    # Default if username not found
    if username is None or username == '':
        username = "Guest"
    
    # Construct the response
    response_body = f"Hello {username}"
    
    # Create HTTP response
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain; charset=utf-8\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "\r\n"
        f"{response_body}"
    )
    
    # Write response to the response stream
    response.write(http_response.encode('utf-8'))
