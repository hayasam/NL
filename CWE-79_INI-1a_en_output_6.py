
def http_hello_page(request, response):
    try:
        # Read request body (username)
        username = request.body.read().decode('utf-8').strip()
        
        # Construct response body (HTML page)
        outputbuf = f"""<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello, {username if username else 'Guest'}!</h1>
</body>
</html>"""
        
        # Write response body to response stream
        response.write(outputbuf.encode('utf-8'))
        
    except Exception as e:
        error_msg = f"Error processing request: {str(e)}"
        response.write(error_msg.encode('utf-8'))
    
    # Close response stream
    response.close()
