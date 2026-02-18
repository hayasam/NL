
import os

# Create a format string with a placeholder
format_string = "ls {}"

# Arguments to substitute into the format string
arguments = ("-la",)

# Use print to format the string
command = print(format_string.format(*arguments), end='')

# Actually we need to capture the string, not print it
# Let me correct that approach
command = format_string.format(*arguments)

# Execute the command using os.system
os.system(command)
