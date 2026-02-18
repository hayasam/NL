
import hashlib
import getpass

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("=== Registration Form ===")
    
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
    
    print("\nRegistration successful!")
    print(f"Username: {username}")
    print(f"Hashed password: {hashed_password}")
    
    return username, hashed_password

if __name__ == "__main__":
    main()
