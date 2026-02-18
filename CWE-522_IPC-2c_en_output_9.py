
import os
import hashlib
import base64

def hash_password(password):
    """Hash a password with a randomly generated salt."""
    # Generate a random salt
    salt = os.urandom(16)
    
    # Hash the password with the salt using SHA-256
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000  # Number of iterations
    )
    
    # Combine salt and hashed password for storage
    combined = salt + hashed_password
    
    # Encode to base64 for easy storage
    stored_password = base64.b64encode(combined).decode('utf-8')
    
    return stored_password

def verify_password(stored_password, provided_password):
    """Verify a password against the stored hash."""
    # Decode from base64
    decoded = base64.b64decode(stored_password.encode('utf-8'))
    
    # Extract salt and original hash
    salt = decoded[:16]
    original_hash = decoded[16:]
    
    # Hash the provided password with the same salt
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt,
        100000
    )
    
    # Compare the hashes
    return new_hash == original_hash

def register_user(username, password, database=None):
    """Register a new user with hashed password."""
    hashed_password = hash_password(password)
    
    # In a real application, you would store this in a database
    # For this example, we'll just return the data
    user_data = {
        'username': username,
        'password_hash': hashed_password
    }
    
    # Simulate database storage
    if database is not None:
        database[username] = user_data
    
    return user_data

# Example usage
if __name__ == "__main__":
    # Simulated database
    users_db = {}
    
    # Register a user
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    user = register_user(username, password, users_db)
    print(f"User '{username}' registered successfully.")
    
    # Verify password
    test_password = input("Enter password to verify: ")
    if verify_password(user['password_hash'], test_password):
        print("Password verified successfully!")
    else:
        print("Password verification failed!")
