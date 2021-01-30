#!/usr/bin/env
'''
Class definitions for tables.
'''
### MODULES ---
from Shapely import Polygon



### CLASSES ---
class table:
    def __init__(self, tableType, position, size):
        '''
        Make Mathew happy.
        '''
        if tableType in ['circle', 'circular']:
            self.table = circular_table(position, size)

        elif tableType in ['rectangular']:
            self.table = rectangular_table(position, *size)


class circular_table:
    def __init__(self, (x,y), r):
        '''
        Define a circular table. Inherit from table class.
        '''
        pass


class rectangular_table:
    def __init__(self, (x, y), l, w):
        '''
        Define a rectangular table. Inherit from table class.
        '''
        pass