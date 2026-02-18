
import os
import stat

secret_info = "Super secret password: 7X!gH@q2"
filename = "secret_data.txt"

with open(filename, 'w') as f:
    f.write(secret_info)

os.chmod(filename, stat.S_IRUSR)
print(filename)
