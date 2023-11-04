# Beatrice Akinpelu
# 03/11/2023

# Problem #6 This program takes the user's input, calculates the factorial using a for loop

import math

# Get user input for the value for which to calculate the factorial
user_input = int(input("Enter a positive integer: "))

# Calculate the factorial using a for loop
factorial = 1
for i in range(1, user_input + 1):
    factorial *= i

# Calculate the factorial using the math module
factorial_with_math = math.factorial(user_input)

# Print the results
print(f"Factorial of {user_input} (calculated): {factorial}")
print(f"Factorial of {user_input} (math.factorial): {factorial_with_math}")


