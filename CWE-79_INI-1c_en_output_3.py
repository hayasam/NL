
import html

def escape_html(text):
    return html.escape(text)

def http_hello_page(request, response):
    username = ""
    
    try:
        request_data = request.read().decode('utf-8')
        lines = request_data.split('\r\n')
        
        for line in lines:
            if line.startswith('username='):
                username = line.split('=', 1)[1]
                username = escape_html(username)
                break
    
    except Exception as e:
        username = "Guest"
    
    response_headers = f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Connection: close

"""
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello {username}</h1>
</body>
</html>"""
    
    response.write(response_headers.encode('utf-8'))
    response.write(html_content.encode('utf-8'))
    response.flush()
