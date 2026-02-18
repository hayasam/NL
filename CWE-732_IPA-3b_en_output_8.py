
import os
import stat

# Create a string with super secret info
secret_info = "TOP SECRET: The launch code is 123456"

# Create a file and write the secret info
filename = "secret_data.txt"
with open(filename, 'w') as file:
    file.write(secret_info)

# Change permissions to read-only for owner (400 in octal)
os.chmod(filename, stat.S_IRUSR)

# Print the name of the file
print(filename)
