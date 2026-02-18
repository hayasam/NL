
import os

# Define the command to be executed
command = "ls"

# Create the string to pass to system function using print formatting
command_string = "{}".format(command)

# Execute the command using system function
os.system(command_string)
