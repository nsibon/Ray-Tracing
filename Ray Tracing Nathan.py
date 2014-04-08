__author__ = 'nathansibon'


import math

# Define functions that return the (http://stackoverflow.com/questions/11291242/python-dynamically-create-function-at-runtime)




# Define the source location
source = [2, 6]

# Define the receiver location
receiver = [8, 6]

images = []

# Create list of distances from the source to the walls
for wall in walls:
    print(math.fabs(wall[0] - source[0]))
    print(math.fabs(wall[1] - source[1]))
