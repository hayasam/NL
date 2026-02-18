
import random

RAND_MAX = getattr(random, 'RAND_MAX', 32767)  # Default to common value if not defined

# Generate three random floats between 0 and 1
float1 = random.random()
float2 = random.random()
float3 = random.random()

# Convert to strings with desired formatting
string = f"{float1:.6f}"
string2 = f"{float2:.6f}"
string3 = f"{float3:.6f}"
