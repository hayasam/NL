
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
            # Handle both GET style (?username=...) and POST style parameters
            parts = line.strip().split('username=')
            if len(parts) > 1:
                username = parts[1].split('&')[0].strip()
                break
    
    # If username not found in parameters, try to extract from request body
    if not username:
        # Look for username in the request body
        lines = request_str.split('\r\n\r\n')
        if len(lines) > 1:
            body = lines[1]
            if 'username=' in body:
                parts = body.split('username=')
                if len(parts) > 1:
                    username = parts[1].split('&')[0].strip()
    
    # Default if username not found
    if not username:
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
    response.flush()
