
import sys
import subprocess

def get_user_info(username):
    try:
        command = f"cat /etc/passwd | grep {username}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout.strip())
        elif result.returncode == 1:
            print(f"User '{username}' not found.")
        else:
            print(f"Error: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    get_user_info(username)
