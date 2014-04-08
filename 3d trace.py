__author__ = 'Matt'

import numpy as np
import scipy as sp

#Defining a wall
P = np.array([3,10,3])
Q = np.array([3,10,8])
R = np.array([3,3,3])

PQ = np.array(P-Q)
PR = np.array(P-R)

normalv = np.cross(PQ, PR)
print normalv
normalized = normalv/np.linalg.norm(normalv)
print normalized

#Finding orthogonal vector from source
source = np.array([5,5,5])

print normalv, np.dot(normalv,P)
A = np.array(normalv)
B = np.array([np.dot(normalv, P),0.])
solved = sp.linalg.solve(A, B)
print solved

print 'd = ' + str(plane_constant)
#Projection of unknown vector source -> plane onto normal vector.
dot_product = np.dot(normalized, source)
print dot_product
source_distance = dot_product/np.linalg.norm(normalized)
print source_distance


source_image = 2*source_distance+source
print source_image
