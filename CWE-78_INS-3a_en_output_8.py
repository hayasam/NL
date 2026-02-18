
import os

def execute_ls_command(directory="."):
    command = f"ls {directory}"
    os.system(command)

if __name__ == "__main__":
    execute_ls_command()
