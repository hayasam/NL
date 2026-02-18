
import os

def execute_ls_command(directory="."):
    command_string = "ls {}".format(directory)
    os.system(command_string)

if __name__ == "__main__":
    target_directory = input("Enter directory to list (or press Enter for current): ")
    if not target_directory:
        execute_ls_command()
    else:
        execute_ls_command(target_directory)
