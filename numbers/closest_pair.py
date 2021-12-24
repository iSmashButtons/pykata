# **Closest pair problem** - The closest pair of points problem or closest pair
#   problem is a problem of computational geometry: given *n* points in metric
#   space, find a pair of points with the smallest distance between them.

# My approach to this problem was to take each point in a list of points and
#   measure the distance from that point to every other point in the list.
#   each time a shorter distance is found, a variable keeping track of this
#   shortest distance is updated.

# Formula for the distance between two points:
# d = sqrt( (x1 - x2)**2 + (y1 - y2)**2 )

from random import randint
from math import sqrt

# config: set the maximum values for X and Y on the abstract plane
XMAX    = 1024
YMAX    = 768
NPOINTS = 50

def create_coordinates(xmax, ymax, n):
    '''
    Returns `n` number of random x-y tuples on a grid of xmax by ymax size.
    '''
    coords = []
    for i in range(n):
        xy = (randint(0, xmax), randint(0, ymax))
        if xy not in coords:
            coords.append(xy)
        else:
            continue

    return coords

POINTS = create_coordinates(XMAX, YMAX, NPOINTS)

# point1, point2, distance between the points
# start with the largest possible distance.
smallest_distance = ( (0, YMAX), (XMAX, 0), sqrt( (0 - YMAX)**2 + (XMAX - 0)**2 ) )

for point1 in POINTS:
    temp_list = POINTS.copy()
    temp_list.remove(point1)
    for point2 in temp_list:
        x1 = point1[0]
        x2 = point2[0]
        y1 = point1[1]
        y2 = point2[1]
        distance = sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
        if distance < smallest_distance[2]:
            smallest_distance = ( (x1, y1), (x2, y2), distance)
    del temp_list

print('Out of {0} points, on a {1} x {2} plane,'.format(NPOINTS, XMAX, YMAX))
print('The pair of points with the smallest distance between them is {0} and {1}.'.format(smallest_distance[0], smallest_distance[1]))
print('The distance is: {0}'.format(smallest_distance[2]))