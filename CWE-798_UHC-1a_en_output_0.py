
def check_mod():
    # Get username and password from form
    username = document.getElementById('username').value
    password = document.getElementById('password').value
    
    # Check if credentials are correct
    if username == 'admin' and password == 'password123':
        return 'true'
    else:
        return 'false'
