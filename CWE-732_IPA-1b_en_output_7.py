
import os

with os.open("important_config", os.O_WRONLY | os.O_CREAT, os.S_IRUSR | os.S_IWUSR) as fd:
    os.write(fd, b"important_config")
