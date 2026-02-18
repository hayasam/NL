
import random

# Generate 3 random floats
float1 = random.random()
float2 = random.uniform(0, 100)
float3 = random.random() * 1000

# Convert to strings
str1 = str(float1)
str2 = str(float2)
str3 = str(float3)

# Concatenate into single string
result = str1 + "," + str2 + "," + str3

# Write to file
with open("random_floats.txt", "w") as file:
    file.write(result)
