
def http_hello_page(request, response):
    # Read request body
    username = request.body.decode('utf-8').strip()
    
    # Construct response body
    outputbuf = f"""<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello, {username if username else 'Guest'}!</h1>
</body>
</html>"""
    
    # Write response
    response.write(outputbuf.encode('utf-8'))
    
    # Close response stream
    response.close()
