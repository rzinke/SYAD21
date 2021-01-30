#!/usr/bin python3
'''
Define restaraunt bounds.
'''
### MODULES ---
from shapely.geometry import LineString
from matplotlib.pyplot import plt



### CLASSES ---
class restaurant:
    def __init__(self, vertices):
        '''
        Define the bounds of a restaurant based on the corners of the room(s).
        '''
        # Define walls
        self.walls = LineString(corners)


    def plot(self):
        '''
        Plot the blueprint of the restaurant.
        '''
        # Spawn figure
        fig, ax = plt.subplots()