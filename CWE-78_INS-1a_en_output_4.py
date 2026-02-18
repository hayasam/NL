
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
    """Get user info using system() - redirects output to a file"""
    import os
    
    # Create a temporary file
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Execute command and redirect output to file
    command = f'getent passwd {username} > {temp_path}'
    return_code = os.system(command)
    
    # Read the output from the file
    try:
        with open(temp_path, 'r') as f:
            output = f.read()
        os.unlink(temp_path)  # Clean up temp file
        return output
    except Exception as e:
        return f"Error: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    
    # Using popen
    print("Using popen():")
    result = get_user_info_popen(username)
    print(result)
    
    print("\n" + "="*50 + "\n")
    
    # Using system
    print("Using system():")
    result = get_user_info_system(username)
    print(result)

if __name__ == "__main__":
    main()
