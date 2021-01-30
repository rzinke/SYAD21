#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "morganpothoff"

########################################################################################################################
#                                                                                                                      #
#   created by: morganpothoff                                                                                          #
#   on 2021.01.30                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION: Morgan is the worst.                                                                                  #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from shapely.geometry import LineString
import matplotlib.pyplot


### CLASSES ---
class Restaurant:
    def __init__(self, vertices):
        '''
        Define the bounds of a restaurant based on the vertices of the room(s).
        '''
        # Define walls
        self.walls = LineString(vertices)


    def plot(self):
        '''
        Plot the blueprint of the restaurant.
        '''
        # Spawn figure
        fig, ax = plt.subplots()


# Reads points from file.
# Takes filename.
# Uses space-separated-variables (ssv). Reads from file. Separate x-y coordinates.
#  Convert points to list of ints.
# Returns array of points (x, y).
def filePoints(filename):
	with open(filename, "r") as file:
		return [[int(coord) for coord in line.rstrip().split(" ")] for line in file.readlines()]


def main():
	vertices = filePoints("points.txt")
	restaurant = Restaurant(vertices)
	print(restaurant.walls)


if __name__ == '__main__':
	main()