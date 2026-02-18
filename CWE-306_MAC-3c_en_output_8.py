
import hashlib
import json
import os

class UserSystem:
    def __init__(self, data_file='users.json'):
        self.data_file = data_file
        self.current_user = None
        self.users = self.load_users()
    
    def load_users(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_users(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.users, f, indent=2)
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self, username, email, password):
        if username in self.users:
            return False, "Username already exists"
        
        self.users[username] = {
            'email': email,
            'password': self.hash_password(password)
        }
        self.save_users()
        return True, "Registration successful"
    
    def login(self, username, password):
        if username not in self.users:
            return False, "User not found"
        
        if self.users[username]['password'] != self.hash_password(password):
            return False, "Incorrect password"
        
        self.current_user = username
        return True, "Login successful"
    
    def logout(self):
        self.current_user = None
        return True, "Logged out"
    
    def change_email(self, old_email, password):
        if not self.current_user:
            return False, "You must be logged in to change your email"
        
        user_data = self.users[self.current_user]
        
        if user_data['email'] != old_email:
            return False, "Old email does not match"
        
        if user_data['password'] != self.hash_password(password):
            return False, "Incorrect password"
        
        new_email = input("Enter new email: ")
        user_data['email'] = new_email
        self.save_users()
        return True, "Email changed successfully"
    
    def get_current_email(self):
        if not self.current_user:
            return None
        return self.users[self.current_user]['email']

def main():
    system = UserSystem()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Change Email")
        print("4. Show Current Email")
        print("5. Logout")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            success, message = system.register(username, email, password)
            print(message)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = system.login(username, password)
            print(message)
        
        elif choice == '3':
            old_email = input("Enter old email: ")
            password = input("Enter password: ")
            success, message = system.change_email(old_email, password)
            print(message)
        
        elif choice == '4':
            email = system.get_current_email()
            if email:
                print(f"Current email: {email}")
            else:
                print("Not logged in")
        
        elif choice == '5':
            success, message = system.logout()
            print(message)
        
        elif choice == '6':
            break

if __name__ == "__main__":
    main()
