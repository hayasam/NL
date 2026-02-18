
import random

# Generate 3 random floats
floats = [random.uniform(0, 100) for _ in range(3)]

# Convert to strings
str_floats = [str(f) for f in floats]

# Concatenate into single string
result = ''.join(str_floats)

# Write to file
with open('output.txt', 'w') as f:
    f.write(result)
