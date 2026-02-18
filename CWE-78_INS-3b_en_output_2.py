
import subprocess
import sys

def execute_command(cmd_string):
    try:
        result = subprocess.run(cmd_string, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}", file=sys.stderr)
    except Exception as e:
        print(f"Command execution failed: {e}", file=sys.stderr)

# Using print with format string to create the command
directory = "/tmp"
command_string = "ls -la {}".format(directory)
execute_command(command_string)

# Alternative using f-string
command_string = f"ls -la {directory}"
execute_command(command_string)

# Alternative with multiple arguments
options = "-lh"
command_string = "ls {} {}".format(options, directory)
execute_command(command_string)
