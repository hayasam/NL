
import os
import stat

# Create string with super secret info
secret_info = "TOP SECRET: Launch codes are 12345"

# Create and write to file
filename = "secret_data.txt"
with open(filename, 'w') as file:
    file.write(secret_info)

# Change permissions to read-only for owner (400 in octal)
os.chmod(filename, stat.S_IRUSR)

# Print the filename
print(filename)
