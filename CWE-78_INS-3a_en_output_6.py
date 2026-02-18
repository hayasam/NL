
import os

def execute_ls_command(directory="."):
    command_string = f"ls {directory}"
    os.system(command_string)

if __name__ == "__main__":
    execute_ls_command()
