
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
    
    def save_users(self):
        data = {}
        for username, user in self.users.items():
            data[username] = {
                'email': user.email,
                'password_hash': user.password_hash
            }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self, username, email, password):
        if username in self.users:
            return False, "Username already exists"
        
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
        return True, "Logged out successfully"
    
    def change_email(self, old_email, password):
        if not self.current_user:
            return False, "You must be logged in to change your email"
        
        if self.current_user.email != old_email:
            return False, "Old email is incorrect"
        
        if self.current_user.password_hash != self.hash_password(password):
            return False, "Password is incorrect"
        
        new_email = input("Enter your new email: ")
        self.current_user.email = new_email
        self.save_users()
        return True, "Email changed successfully"
    
    def get_current_user_info(self):
        if self.current_user:
            return f"Username: {self.current_user.username}, Email: {self.current_user.email}"
        return "No user logged in"

def main():
    system = LoginSystem()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Change Email")
        print("4. View Current User")
        print("5. Logout")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
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
            old_email = input("Enter your old email: ")
            password = input("Enter your password: ")
            success, message = system.change_email(old_email, password)
            print(message)
        
        elif choice == "4":
            print(system.get_current_user_info())
        
        elif choice == "5":
            success, message = system.logout()
            print(message)
        
        elif choice == "6":
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
