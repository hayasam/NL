
import subprocess
import sys

def get_user_info_popen(username):
    """Get user info using popen()"""
    try:
        process = subprocess.Popen(
            ['getent', 'passwd', username],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate()
        
        if process.returncode == 0:
            return output.strip()
        else:
            return f"Error: {error.strip()}"
    except Exception as e:
        return f"Exception: {str(e)}"

def get_user_info_system(username):
    """Get user info using system() approach"""
    import os
    
    # Using system() - less flexible for capturing output
    return_code = os.system(f'getent passwd {username} > /tmp/user_info.txt 2>&1')
    
    if return_code == 0:
        with open('/tmp/user_info.txt', 'r') as f:
            return f.read().strip()
    else:
        with open('/tmp/user_info.txt', 'r') as f:
            return f"Error: {f.read().strip()}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    
    # Using popen() - preferred method
    print("Using popen():")
    result = get_user_info_popen(username)
    print(result)
    
    print("\n" + "="*50 + "\n")
    
    # Using system() approach
    print("Using system() approach:")
    result = get_user_info_system(username)
    print(result)

if __name__ == "__main__":
    main()
