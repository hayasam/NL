
import subprocess
import sys

def execute_command(cmd_string):
    try:
        result = subprocess.run(cmd_string, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Error: {result.stderr}", file=sys.stderr)
    except Exception as e:
        print(f"Failed to execute command: {e}", file=sys.stderr)

# Example usage
directory = "/home/user"
command_string = "ls -la {}".format(directory)
execute_command(command_string)
