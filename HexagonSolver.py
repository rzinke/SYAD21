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
    # Solve for distance from the center of one hexagon to that of another
    adjScale = 1.7320508075688774  # scaling factor for centroid distance 2*cos(30 deg)
    dist = adjScale*r  # distance from one center to another

    # Format starting point as array
    start = np.array([x0, y0])

    # Define unit vectors
    nTop = np.array([0, 1])
    nDiag = np.array([np.sqrt(2), np.sqrt(2)])
    nRight = np.array([1, 0])

    # Solve for centroids of other hexagons by scaling unit vectors
    top = dist*nTop + start  # coordinates of top hexagon
    diag = dist*nDiag + start  # coordinates of diagonal hexagon
    right = dist*nRight + start  # coordinates of right hexagon

    return top, diag, right