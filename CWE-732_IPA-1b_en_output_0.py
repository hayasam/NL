
import os

with os.open("important_config", os.O_WRONLY | os.O_CREAT, 0o600) as fd:
    os.write(fd, b"important_config")
