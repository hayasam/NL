
import html

def escape_html(text):
    return html.escape(text)

def http_hello_page(request, response):
    username = ""
    
    try:
        request_data = request.read().decode('utf-8')
        
        for line in request_data.split('\n'):
            if 'username=' in line:
                parts = line.split('username=')
                if len(parts) > 1:
                    username = parts[1].strip()
                    break
    except:
        username = "Unknown"
    
    safe_username = escape_html(username)
    
    response_content = f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Connection: close

<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello {safe_username}</h1>
</body>
</html>"""
    
    response.write(response_content.encode('utf-8'))
    response.flush()
