
import os

def create_important_config():
    file_path = "important_config"
    
    # File permissions: readable and writable by owner (0600 in octal)
    permissions = os.O_CREAT | os.O_TRUNC | os.O_WRONLY
    mode = 0o600  # S_IRUSR|S_IWUSR
    
    try:
        fd = os.open(file_path, permissions, mode)
        with os.fdopen(fd, 'w') as file:
            # File is now open and truncated/created
            pass
        print(f"File '{file_path}' created successfully with appropriate permissions.")
    except Exception as e:
        print(f"Error creating file: {e}")

if __name__ == "__main__":
    create_important_config()
