
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
        self.current_user = None
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                return {user['username']: User(user['username'], user['email'], user['password_hash']) 
                        for user in data}
        return {}

    def save_users(self):
        data = [{'username': user.username, 
                 'email': user.email, 
                 'password_hash': user.password_hash} 
                for user in self.users.values()]
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, email, password):
        if username in self.users:
            return False
        password_hash = self.hash_password(password)
        self.users[username] = User(username, email, password_hash)
        self.save_users()
        return True

    def login(self, username, password):
        if username not in self.users:
            return False
        user = self.users[username]
        if user.password_hash == self.hash_password(password):
            self.current_user = user
            return True
        return False

    def logout(self):
        self.current_user = None

    def change_email(self, old_email, password):
        if not self.current_user:
            return False, "Not logged in"
        
        if self.current_user.email != old_email:
            return False, "Old email does not match"
        
        if self.current_user.password_hash != self.hash_password(password):
            return False, "Incorrect password"
        
        new_email = input("Enter new email: ")
        self.current_user.email = new_email
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
        
        choice = input("Select option: ")
        
        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            if system.register(username, email, password):
                print("Registration successful")
            else:
                print("Username already exists")
                
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            if system.login(username, password):
                print(f"Logged in as {username}")
            else:
                print("Invalid credentials")
                
        elif choice == "3":
            old_email = input("Enter old email: ")
            password = input("Enter password: ")
            success, message = system.change_email(old_email, password)
            print(message)
            
        elif choice == "4":
            system.logout()
            print("Logged out")
            
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
