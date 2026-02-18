
import subprocess
import sys

def get_user_info(username):
    try:
        result = subprocess.run(
            ['grep', f'^{username}:', '/etc/passwd'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return f"User '{username}' not found."
    except FileNotFoundError:
        return "Error: /etc/passwd file not found or grep command unavailable."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    user_info = get_user_info(username)
    print(user_info)
