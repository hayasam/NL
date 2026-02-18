
def check_mod():
    # Get username and password from form (assuming form fields exist)
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    
    # Check if credentials are correct
    if username == "admin" and password == "secret123":
        return 'true'
    else:
        return 'false'
