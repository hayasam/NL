
import subprocess
import sys

def get_user_info_popen(username):
    """Get user info using popen()"""
    try:
        with subprocess.Popen(['getent', 'passwd', username], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            text=True) as proc:
            output = proc.stdout.read()
            return output
    except Exception as e:
        return f"Error: {e}"

def get_user_info_system(username):
    """Get user info using system()"""
    try:
        # Note: system() doesn't capture output directly
        # This is a workaround using subprocess.call
        import os
        return_code = os.system(f'getent passwd {username}')
        return f"Command executed with return code: {return_code}"
    except Exception as e:
        return f"Error: {e}"

def get_user_info_subprocess(username):
    """Get user info using subprocess.run (modern alternative)"""
    try:
        result = subprocess.run(['getent', 'passwd', username], 
                              capture_output=True, 
                              text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        
        # Using popen() as requested
        output = get_user_info_popen(username)
        print(output)
    else:
        print("Usage: python script.py <username>")
