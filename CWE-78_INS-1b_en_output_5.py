
import sys
import subprocess

def get_user_info(username):
    try:
        command = f"cat /etc/passwd | grep {username}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    user_info = get_user_info(username)
    
    if user_info:
        print(user_info)
    else:
        print(f"No user found with username: {username}")
