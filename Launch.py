#!/usr/bin/env python3
'''
Launch the space optimizer.
'''
### MODULES ---
import numpy as np
import matplotlib.pyplot as plt
from HexagonSolver import hexmesh, hexvertices
from shapely.geometry import Polygon, Point


### FUNCTIONS ---
def print_coordinates(start, top, diag, right):
    print('Coordinates')
    print('\tstart: {:f} {:f}'.format(*start))
    print('\ttop: {:f} {:f}'.format(*top))
    print('\tdiag: {:f} {:f}'.format(*diag))
    print('\tright: {:f} {:f}'.format(*right))



### TESTING ---
## Restaurant
x = 15
y = 10
room = np.array([[0, 0],
                 [0, y],
                 [7, y],
                 [9, 8],
                 [9, y],
                 [x, y],
                 [x, 0],
                 [12, 0],
                 [12, 5],
                 [10, 5],
                 [10, 0],
                 [6, 0],
                 [6, 5],
                 [4, 5],
                 [4, 0],
                 [0, 0]])

x0 = room[:,0].min()
y0 = room[:,1].min()
xend = room[:,0].max()
yend = room[:,1].max()


## Radius
tableSize = 1
personalSpace = 0
walkingSpace = 0

r = tableSize/2 + personalSpace + walkingSpace


## Define mesh
X, Y = hexmesh(x0, y0, xend, yend, r)
M, N = X.shape


## Plot
fig, ax = plt.subplots()

# Plot room
ax.fill(room[:,0], room[:,1], facecolor=[0.8]*3, edgecolor='k')

# Get circle centers
circleCenters = []

for i in range(M):
    for j in range(N):
        # Hexagon vertices
        pts = hexvertices(X[i,j], Y[i,j], r)

        # Append circle centers
        circleCenters.append(pts)

        # Plot hexagons
        ax.fill(pts[1:,0], pts[1:,1], facecolor=[0.5]*3, edgecolor='k')

        # Circles
        [ax.add_patch(plt.Circle(pt, r, color='c')) for pt in pts]

# Reformat circle centers as n x 2 array
circleCenters = np.vstack(circleCenters)
ax.plot(circleCenters[:,0], circleCenters[:,1], 'b.')

# Format plot
ax.set_aspect(1)
ax.set_xlabel('Room width')
ax.set_ylabel('Room length')
ax.set_title('ALL CIRCLES')
fig.savefig('/Users/rzinke/Desktop/Fig.png')


## Prune invalid circles
# Convert room coords to shapely polygon
room = Polygon(room)

# Determine threshold
maxArea = np.pi*r**2
threshold = 0.8*maxArea

# Loop through circles to check for area of overlap
validCircles = []
for circleCenter in circleCenters:
    circle = Point(*circleCenter).buffer(r)
    area = room.intersection(circle).area

    # Add to list of circles if area is greater than some threshold
    if area > threshold:
        validCircles.append(circleCenter)

# Plot valid circles
fig, ax = plt.subplots()

roomX, roomY = room.exterior.coords.xy
ax.fill(roomX, roomY, facecolor=[0.8]*3, edgecolor='k')
[ax.add_patch(plt.Circle(pt, r, color='b')) for pt in validCircles]

ax.set_aspect(1)
ax.set_xlabel('Room width')
ax.set_ylabel('Room length')
ax.set_title('VALID CIRCLES')
fig.savefig('/Users/rzinke/Desktop/Fig2.png')


## Report



plt.show()