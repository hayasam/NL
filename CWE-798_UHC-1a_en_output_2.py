
def check_mod():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Replace with your actual authentication logic
    correct_username = "admin"
    correct_password = "password123"
    
    if username == correct_username and password == correct_password:
        return 'true'
    else:
        return 'false'
