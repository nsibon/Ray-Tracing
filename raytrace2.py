__author__ = 'Matthew'
import math
import numpy as np

face_y = 40
face_x = 10
source = np.array([6,2])

def FaceMaker(x, y):
    vertex1 = np.array([0,0])
    vertex2 = np.array([x,0])
    vertex3 = np.array([x,y])
    vertex4 = np.array([0,y])
    vertex_list = [vertex1, vertex2, vertex3, vertex4]
    wall1 = np.array([math.fabs(vertex2[0]-vertex1[0]),
                      math.fabs(vertex2[1]-vertex1[1])])

    wall2 = np.array([math.fabs(vertex3[0]-vertex2[0]),
                      math.fabs(vertex3[1]-vertex2[1])])

    wall3 = np.array([math.fabs(vertex4[0]-vertex3[0]),
                      math.fabs(vertex4[1]-vertex3[1])])

    wall4 = np.array([math.fabs(vertex1[0]-vertex4[0]),
                      math.fabs(vertex1[1]-vertex4[1])])

    wall_matrix = [wall1, wall2, wall3, wall4]
    print wall_matrix
    return wall_matrix

wall_matrix = FaceMaker(face_x,face_y)

def getOrtho(wall):
    print wall
    if wall[1] == 0:
        wall += [0,1]
    ortho = [1, -wall[0]/wall[1]]
    return ortho

ortholist = []
for wall in wall_matrix:
    ortholist.append(getOrtho(wall))
print ortholist



