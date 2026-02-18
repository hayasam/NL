
import random

def generate_random_strings():
    # Generate three random floats between 0 and 1
    rand1 = random.random()
    rand2 = random.random()
    rand3 = random.random()
    
    # Convert to strings with 6 decimal places
    string = f"{rand1:.6f}"
    string2 = f"{rand2:.6f}"
    string3 = f"{rand3:.6f}"
    
    return string, string2, string3

# Alternative implementation using sprintf-like formatting
def generate_random_strings_sprintf_style():
    import sys
    
    # RAND_MAX equivalent in Python (system's max random integer)
    RAND_MAX = sys.maxsize
    
    # Generate three random floats between 0 and 1
    rand1 = random.randint(0, RAND_MAX) / RAND_MAX
    rand2 = random.randint(0, RAND_MAX) / RAND_MAX
    rand3 = random.randint(0, RAND_MAX) / RAND_MAX
    
    # Convert to strings using sprintf-like formatting
    string = "{:.6f}".format(rand1)
    string2 = "{:.6f}".format(rand2)
    string3 = "{:.6f}".format(rand3)
    
    return string, string2, string3

# Simple one-liner version
string, string2, string3 = [f"{random.random():.6f}" for _ in range(3)]
