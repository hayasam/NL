
import os
import stat

secret_info = "TOP SECRET: The launch code is 12345"
filename = "secret_data.txt"

with open(filename, 'w') as f:
    f.write(secret_info)

os.chmod(filename, stat.S_IRUSR)
print(filename)
