
import random

RAND_MAX = 2**31 - 1  # Typical RAND_MAX value on many systems

def rand():
    return random.randint(0, RAND_MAX)

string = f"{(rand() / RAND_MAX):.6f}"
string2 = f"{(rand() / RAND_MAX):.6f}"
string3 = f"{(rand() / RAND_MAX):.6f}"
