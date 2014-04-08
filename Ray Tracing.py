__author__ = 'nathansibon'


import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

import matplotlib
# Define the 4 anchors of the room
# [x, y]
wall1 = [0, 0]
wall2 = [0, 10]
wall3 = [10, 10]
wall4 = [10, 0]
walls = np.array([wall1, wall2, wall3, wall4], ndmin=2)
print(walls)
# Define the source location
source = [2, 6]

# Define the receiver location
receiver = [8, 6]

images = []

# Create list of distances from the source to the walls

for wall in walls:
    #This block calculates the euclidean distance between the source and wall vectors. Probably not what we need.
    '''
    distarray = np.array([source, wall])
    print distarray
    print pdist(distarray, 'euclidean')
    '''
    print(str(math.fabs(wall[0] - source[0])) + ', ' + str(math.fabs(wall[1] - source[1])))


'''
#Possibility:
#Get the outline around the room anchors using the scipy Convex Hull method.
roomhull = ConvexHull(walls)

#Use the Hull to plot the room with MatPlotLib.
plt.plot(walls[:,0], walls[:,1], 'o')
for simplex in roomhull.simplices:
    plt.plot(walls[simplex,0], walls[simplex,1], 'k-')
plt.show()

#Issues: Convex Hull will only plot around the outside points. Any points placed 'inside' the current Hull will not be included.
'''