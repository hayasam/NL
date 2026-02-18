
import hashlib
import json
import os

class User:
    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash

class LoginSystem:
    def __init__(self, data_file="users.json"):
        self.data_file = data_file
        self.users = {}
        self.current_user = None
        self.load_users()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def load_users(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for username, user_data in data.items():
                        self.users[username] = User(
                            username=username,
                            email=user_data['email'],
                            password_hash=user_data['password_hash']
                        )
            except (json.JSONDecodeError, KeyError):
                self.users = {}
        else:
            self.users = {}

    def save_users(self):
        data = {}
        for username, user in self.users.items():
            data[username] = {
                'email': user.email,
                'password_hash': user.password_hash
            }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def register(self, username, email, password):
        if username in self.users:
            return False, "Username already exists"
        if any(user.email == email for user in self.users.values()):
            return False, "Email already registered"
        
        password_hash = self.hash_password(password)
        self.users[username] = User(username, email, password_hash)
        self.save_users()
        return True, "Registration successful"

    def login(self, username, password):
        if username not in self.users:
            return False, "Invalid username or password"
        
        user = self.users[username]
        if user.password_hash == self.hash_password(password):
            self.current_user = user
            return True, "Login successful"
        return False, "Invalid username or password"

    def logout(self):
        self.current_user = None
        return True, "Logged out"

    def change_email(self, old_email, password):
        if not self.current_user:
            return False, "You must be logged in to change your email"
        
        user = self.current_user
        
        if user.email != old_email:
            return False, "Old email does not match"
        
        if user.password_hash != self.hash_password(password):
            return False, "Incorrect password"
        
        new_email = input("Enter new email: ")
        
        if any(u.email == new_email for u in self.users.values() if u.username != user.username):
            return False, "Email already in use by another account"
        
        user.email = new_email
        self.save_users()
        return True, "Email changed successfully"

def main():
    system = LoginSystem()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Change Email")
        print("4. Logout")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            success, message = system.register(username, email, password)
            print(message)
            
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = system.login(username, password)
            print(message)
            
        elif choice == "3":
            old_email = input("Enter old email: ")
            password = input("Enter password: ")
            success, message = system.change_email(old_email, password)
            print(message)
            
        elif choice == "4":
            success, message = system.logout()
            print(message)
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
