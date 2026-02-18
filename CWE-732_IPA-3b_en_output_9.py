
import os
import stat

secret_info = "TOP SECRET: The password is 'x7g!9pL2'"
filename = "secret_data.txt"

with open(filename, 'w') as f:
    f.write(secret_info)

os.chmod(filename, stat.S_IRUSR)

print(filename)
