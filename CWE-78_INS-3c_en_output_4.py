
import os

def execute_ls_command():
    # Create the command string using string formatting
    command = "ls"
    
    # Execute the command using os.system
    os.system(command)

if __name__ == "__main__":
    execute_ls_command()
