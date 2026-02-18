
def check_mod():
    # Get username and password from form (assuming form elements exist)
    username = document.getElementById('username').value
    password = document.getElementById('password').value
    
    # Check if credentials are correct
    if username == 'admin' and password == 'secret':
        return 'true'
    else:
        return 'false'
