
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
            continue
        
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            continue
            
        break
    
    hashed_password = hash_password(password)
    
    # In a real application, you would save to a database here
    # For this example, we'll just return the values
    return {
        'username': username,
        'password_hash': hashed_password
    }

if __name__ == "__main__":
    user_data = register_user()
    print(f"\nRegistration successful!")
    print(f"Username: {user_data['username']}")
    print(f"Password hash: {user_data['password_hash']}")
