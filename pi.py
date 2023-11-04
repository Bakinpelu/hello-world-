# Beatrice Akinpelu
# 03/11/2023

# Problem #4,

import random
import math

def approximate_pi(num_points):
    inside_circle = 0
    
    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_points) * 4

num_points = 1000000  # You can adjust this to increase or decrease the accuracy.
approximated_pi = approximate_pi(num_points)

print(f"Approximation of pi: {approximated_pi}")
print(f"Value of math.pi: {math.pi}")
