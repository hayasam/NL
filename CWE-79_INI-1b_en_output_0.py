
def http_hello_page(request, response):
    # Read the entire request
    request_data = request.read()
    
    # Decode from bytes to string
    request_str = request_data.decode('utf-8')
    
    # Parse the username from the request
    # Assuming the username is in a query parameter like ?username=name
    username = "Guest"  # Default value
    
    # Look for username in query string
    lines = request_str.split('\r\n')
    if lines and '?' in lines[0]:
        # Get the query string from the first line
        query_part = lines[0].split('?', 1)[1].split(' ')[0]
        params = query_part.split('&')
        
        for param in params:
            if param.startswith('username='):
                username = param.split('=', 1)[1]
                break
    
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
