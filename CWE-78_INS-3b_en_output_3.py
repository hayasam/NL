
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

# Using print to format the command string
directory = "/tmp"
command_string = print(f"ls -la {directory}", end='') or f"ls -la {directory}"
execute_command(command_string)
