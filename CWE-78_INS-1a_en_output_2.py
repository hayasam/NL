
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
    """Get user info using system() approach"""
    try:
        result = subprocess.run(['getent', 'passwd', username],
                              capture_output=True,
                              text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    
    # Using popen() approach
    print("Using popen() approach:")
    output_popen = get_user_info_popen(username)
    print(output_popen)
    
    # Using system() approach
    print("\nUsing system() approach:")
    output_system = get_user_info_system(username)
    print(output_system)
