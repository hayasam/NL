
import random

# Define RAND_MAX to match typical C implementation (2^31 - 1)
RAND_MAX = 2147483647

def rand():
    return random.randint(0, RAND_MAX)

# Generate three random floats between 0 and 1
float1 = rand() / RAND_MAX
float2 = rand() / RAND_MAX
float3 = rand() / RAND_MAX

# Convert to strings with formatting
string = f"{float1:.6f}"
string2 = f"{float2:.6f}"
string3 = f"{float3:.6f}"
