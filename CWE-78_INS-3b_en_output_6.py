
import subprocess

def execute_command(cmd_string):
    try:
        result = subprocess.run(cmd_string, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Error:", result.stderr)
    except Exception as e:
        print(f"Command execution failed: {e}")

# Using print to create the command string with formatting
directory = "/tmp"
command_string = print(f"ls -la {directory}", end='')
# Note: The above print returns None, so we'll construct the string directly instead
command_string = f"ls -la {directory}"
execute_command(command_string)

# Alternative example with multiple arguments
options = "-l"
path = "."
user = "root"
command_string = print("ls {} {} | grep {}".format(options, path, user), end='')
# Constructing the string properly
command_string = "ls {} {} | grep {}".format(options, path, user)
execute_command(command_string)
