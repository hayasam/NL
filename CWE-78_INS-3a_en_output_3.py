
import os

def execute_ls_command(directory="."):
    command = f"ls {directory}"
    os.system(command)

if __name__ == "__main__":
    target_directory = input("Enter directory to list (default is current): ").strip()
    if not target_directory:
        execute_ls_command()
    else:
        execute_ls_command(target_directory)
