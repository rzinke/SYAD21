#!/usr/bin/env python3
'''
Solve for optimal circle packing within a restaurant using the hexagon arrangement.
See, e.g., https://en.wikipedia.org/wiki/Circle_packing
'''

### MODULES ---
import numpy as np



### CLASSES AND DEFINITIONS ---
def hexcell(x0, y0, r):
    '''
    Return the centers of three more hexagons given the center and radius of the first hexagon.
    top   diag
     |    /
     |  /
     o __ __ right

    First, compute the distance from one hexagon center to another.
    This is equal to 2*r*cos(30 deg) = 
    '''
    # Pre-solve parameters
    rad30 = np.deg2rad(30)
    cos30 = np.cos(rad30)
    sin30 = np.sin(rad30)

    # Define diameter
    d = 2*r

    # Solve for distance from the center of one hexagon to that of another
    dist = 2*cos30*d  # distance from one center to another

    # Format starting point as array
    start = np.array([x0, y0])

    # Define unit vectors
    nUpper = np.array([   0,       1])
    nDagnl = np.array([cos30,  sin30])
    nRight = np.array([cos30, -sin30])

    # Solve for centroids of other hexagons by scaling unit vectors
    upper = dist*nUpper + start  # coordinates of top hexagon
    dagnl = dist*nDagnl + start  # coordinates of diagonal hexagon
    right = dist*nRight + start  # coordinates of right hexagon

    return upper, dagnl, right


def hexmesh(x0, y0, xend, yend, r):
    '''
    Create a mesh of equilateral hexigons.
    '''
    # Pre-solve parameters
    rad30 = np.deg2rad(30)
    cos30 = np.cos(rad30)
    sin30 = np.sin(rad30)

    # Define diameter
    d = 2*r

    # Define distance from one centroid to another
    D = 2*d*cos30

    # x, y distances between hexagon centroids
    Dx = D*cos30
    Dy = D*sin30

    # Define mesh
    x = np.arange(x0, xend, Dx)
    y = np.arange(y0, yend, D)
    X, Y = np.meshgrid(x, y)

    # Offset /y
    Y[:,::2] += Dy

    return X, Y
    


def hexvertices(x0, y0, r):
    '''
    Find the vertices of a hexagon and return as x, y points, given the center of the hexagon and a radius parameter.
       2 -- 3
     /        \
    1           4
     \        /
       6 -- 5
    '''
    # Pre-solve parameters
    rad60 = np.deg2rad(60)
    cos60 = np.cos(rad60)
    sin60 = np.sin(rad60)

    # Format starting point as array
    start = np.array([x0, y0])

    # Convert radius to diameter
    d = 2*r

    # Unit vectors pointing to each vertex
    norms = []
    norms.append(np.array([     0,      0]))
    norms.append(np.array([    -1,      0]))
    norms.append(np.array([-cos60,  sin60]))
    norms.append(np.array([ cos60,  sin60]))
    norms.append(np.array([     1,      0]))
    norms.append(np.array([ cos60, -sin60]))
    norms.append(np.array([-cos60, -sin60]))

    # Solve for vertex coordinates
    P = np.array([d*n+start for n in norms])

    return P