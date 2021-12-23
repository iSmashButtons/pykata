# **Closest pair problem** - The closest pair of points problem or closest pair
# problem is a problem of computational geometry: given *n* points in metric
# space, find a pair of points with the smallest distance between them.

from random import randint
from math import sqrt

def create_coordinates(xmax, ymax, n):
    '''
    Returns `n` number of random x-y tuples on a grid of xmax by ymax size.
    '''
    coords = []
    for i in range(n):
        xy = (randint(0, xmax), randint(0, ymax))
        coords.append(xy)

    return coords

#POINTS = [
    #(82, 65), (2, 64), (43, 39), (34, 17), (8, 39), (96, 28), (64, 78), (76, 2),
    #(99, 91), (14, 25), (94, 64), (58, 66), (17, 42), (93, 41), (22, 50), (7, 10),
    #(73, 27), (85, 79), (50, 23), (93, 79), (32, 92), (21, 85), (60, 22), (83, 0),
    #(94, 11), (41, 25), (4, 17), (54, 59), (29, 32), (57, 33), (17, 75), (30, 22),
    #(16, 70), (20, 100), (72, 43), (38, 69), (38, 53), (60, 88), (86, 97), (4, 78),
    #(50, 69), (89, 44), (1, 47), (77, 4), (60, 6), (18, 11), (30, 11), (72, 72),
    #(66, 64), (17, 65), (63, 85), (9, 37), (83, 87), (38, 23), (66, 23), (46, 57),
    #(97, 29), (96, 33), (28, 96), (45, 60), (92, 27), (74, 32), (6, 18), (22, 23),
    #(64, 71), (60, 32), (76, 80), (67, 28), (37, 17), (73, 70), (83, 16), (85, 21),
    #(13, 0), (40, 72), (48, 82), (54, 80), (76, 74), (22, 61), (31, 31), (73, 80),
    #(0, 8), (10, 1), (63, 67), (87, 67), (41, 71), (9, 30), (20, 48), (88, 57),
    #(55, 71), (71, 11), (40, 3), (40, 81), (66, 3), (62, 62), (62, 95), (47, 79),
    #(66, 18), (43, 78), (66, 5), (31, 41)
#]
POINTS = [ (82, 65), (2, 64), (43, 39), (34, 17), (8, 39)]

# Distance between two points:
# d = sqrt( (x1 - x2)^2 + (y1 - y2)^2 )

smallest_distance = sqrt( (0 - 100)**2 + (100 - 0)**2 )
print(smallest_distance)

for point1 in POINTS:
    temp_list = POINTS.copy()
    temp_list.remove(point1)
    print(temp_list)
    for point2 in temp_list:
        print(point1, point2)
        x1 = point1[0]
        x2 = point2[0]
        y1 = point1[1]
        y2 = point2[1]
        distance = sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
        if distance < smallest_distance:
            smallest_distance = distance
