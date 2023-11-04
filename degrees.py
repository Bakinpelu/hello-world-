# Beatrice Akinpelu
# 03/11/2023

# Problem #5 this program takes the user's input in radians, converts it to degrees using the formula

import math

# Get user input for radians
radians = float(input("Enter a value in radians: "))

# Convert radians to degrees
degrees = radians * (180 / math.pi)

# Calculate degrees using the math module
degrees_with_math = math.degrees(radians)

# Print the results
print(f"User input in radians: {radians} radians")
print(f"Converted to degrees: {degrees} degrees")
print(f"Calculated using math.degrees: {degrees_with_math} degrees")
