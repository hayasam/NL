
import os
import hashlib
import base64

def hash_password(password):
    """Hash a password with a randomly generated salt."""
    # Generate a random salt
    salt = os.urandom(16)
    
    # Hash the password with the salt using SHA-256
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    
    # Combine salt and hashed password for storage
    salt_b64 = base64.b64encode(salt).decode('utf-8')
    hash_b64 = base64.b64encode(hashed).decode('utf-8')
    
    # Return format: salt$hashed_password
    return f"{salt_b64}${hash_b64}"

def verify_password(stored_password, provided_password):
    """Verify a password against the stored hash."""
    # Split the stored value into salt and hash
    salt_b64, hash_b64 = stored_password.split('$')
    
    # Decode from base64
    salt = base64.b64decode(salt_b64)
    stored_hash = base64.b64decode(hash_b64)
    
    # Hash the provided password with the same salt
    provided_hash = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt,
        100000
    )
    
    # Compare the hashes
    return stored_hash == provided_hash

def register_user(username, password, database):
    """Register a new user with hashed password."""
    if username in database:
        return False, "Username already exists"
    
    hashed_password = hash_password(password)
    database[username] = hashed_password
    return True, "Registration successful"

def login_user(username, password, database):
    """Login a user by verifying password."""
    if username not in database:
        return False, "User not found"
    
    stored_hash = database[username]
    if verify_password(stored_hash, password):
        return True, "Login successful"
    else:
        return False, "Invalid password"

# Example usage
if __name__ == "__main__":
    # Simulating a database (in practice, use a real database)
    user_database = {}
    
    # Register a new user
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    success, message = register_user(username, password, user_database)
    print(message)
    
    if success:
        # Try to login
        print("\n--- Login Test ---")
        test_user = input("Enter username: ")
        test_pass = input("Enter password: ")
        
        login_success, login_msg = login_user(test_user, test_pass, user_database)
        print(login_msg)
