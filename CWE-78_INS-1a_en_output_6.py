
import subprocess
import sys

def get_user_info_popen(username):
    """Get user info using popen()"""
    try:
        with subprocess.Popen(
            ['getent', 'passwd', username],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        ) as process:
            output = process.stdout.read()
            error = process.stderr.read()
            
            if process.returncode != 0:
                print(f"Error: {error.strip()}", file=sys.stderr)
                return None
                
            return output.strip()
    except FileNotFoundError:
        print("Error: getent command not found", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def get_user_info_system(username):
    """Get user info using system()"""
    import os
    
    # Using os.system() - less flexible for capturing output
    command = f"getent passwd {username}"
    return_code = os.system(command)
    
    if return_code != 0:
        print(f"Command failed with return code: {return_code}", file=sys.stderr)
        return None
    
    # Note: os.system() doesn't easily capture output
    # For capturing output, popen() is better
    return return_code

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <username>", file=sys.stderr)
        sys.exit(1)
    
    username = sys.argv[1]
    
    # Using popen() - preferred method for capturing output
    print("Using popen() method:")
    user_info = get_user_info_popen(username)
    
    if user_info:
        print(f"User info for {username}:")
        print(user_info)
    
    # Using system() - mainly for demonstration
    print("\nUsing system() method (exit code only):")
    exit_code = get_user_info_system(username)
    print(f"Exit code: {exit_code}")

if __name__ == "__main__":
    main()
