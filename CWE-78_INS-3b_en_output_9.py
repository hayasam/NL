
import subprocess

def execute_command(cmd_string):
    result = subprocess.run(cmd_string, shell=True, capture_output=True, text=True)
    return result.stdout

format_string = "ls {}"
arguments = ["-la", "/tmp"]
command = format_string.format(*arguments)
output = execute_command(command)
print(output)
