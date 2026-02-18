
import subprocess
import sys

def get_user_info_popen(username):
    """Get user info using popen()"""
    try:
        with subprocess.Popen(['getent', 'passwd', username], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            text=True) as process:
            output, error = process.communicate()
            if process.returncode == 0:
                return output
            else:
                print(f"Error: {error}", file=sys.stderr)
                return None
    except FileNotFoundError:
        print("Error: 'getent' command not found", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def get_user_info_system(username):
    """Get user info using system() approach"""
    import os
    command = f"getent passwd {username}"
    return_code = os.system(command)
    return return_code

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    
    # Using popen() method
    print("Using popen() method:")
    output = get_user_info_popen(username)
    if output:
        print(output)
    
    # Using system() method
    print("\nUsing system() method (return code only):")
    return_code = get_user_info_system(username)
    print(f"Command returned: {return_code}")

if __name__ == "__main__":
    main()
