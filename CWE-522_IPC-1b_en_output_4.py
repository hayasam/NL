
import hashlib
import getpass

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """Register a new user with username and hashed password"""
    print("=== User Registration ===")
    
    username = input("Enter username: ").strip()
    
    while True:
        password = getpass.getpass("Enter password: ")
        confirm_password = getpass.getpass("Confirm password: ")
        
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
        elif len(password) < 6:
            print("Password must be at least 6 characters long.")
        else:
            break
    
    hashed_password = hash_password(password)
    
    # In a real application, you would store this in a database
    # For this example, we'll just print the result
    print(f"\nRegistration successful!")
    print(f"Username: {username}")
    print(f"Hashed password: {hashed_password}")
    
    # Return the user data
    return {
        'username': username,
        'password_hash': hashed_password
    }

if __name__ == "__main__":
    user_data = register_user()
