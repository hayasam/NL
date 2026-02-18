
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

# Generate and store the strings
string, string2, string3 = generate_random_strings()
