
import os
import stat

secret_info = "This is super secret information that should be protected."
filename = "secret_data.txt"

with open(filename, 'w') as f:
    f.write(secret_info)

os.chmod(filename, stat.S_IRUSR)

print(filename)
