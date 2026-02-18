
import os

def create_important_config():
    file_path = "important_config"
    flags = os.O_CREAT | os.O_TRUNC | os.O_WRONLY
    mode = os.S_IRUSR | os.S_IWUSR
    
    fd = os.open(file_path, flags, mode)
    
    with os.fdopen(fd, 'w') as f:
        # Write initial content if needed
        # f.write("initial configuration\n")
        pass
    
    print(f"File '{file_path}' created with owner read/write permissions")

if __name__ == "__main__":
    create_important_config()
