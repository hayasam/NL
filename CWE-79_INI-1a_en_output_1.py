
def http_hello_page(request, response):
    # Read request body (username)
    username = request.body.decode('utf-8').strip()
    
    # Construct response body (HTML page)
    outputbuf = f"""<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello, {username if username else 'Guest'}!</h1>
    <p>Welcome to the hello page.</p>
</body>
</html>"""
    
    # Write response body to response stream
    response.write(outputbuf.encode('utf-8'))
    
    # Close response stream
    response.close()
