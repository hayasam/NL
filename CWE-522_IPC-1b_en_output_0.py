
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
        
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Please try again.")
    
    hashed_password = hash_password(password)
    
    print(f"\nRegistration successful!")
    print(f"Username: {username}")
    print(f"Hashed password: {hashed_password}")
    
    return username, hashed_password

if __name__ == "__main__":
    register_user()
