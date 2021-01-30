#!/usr/bin/env
'''
Class definitions for tables.
'''
### MODULES ---
from shapely.geometry import Polygon;



### CLASSES ---
class table:
    CIRCULAR = 1;
    RECTANGULAR = 2;

    def __init__(self, position, size):
        '''
        Try to make Mathew happy. FAILED
        '''
        self.position = position;
        self.size = size;

        self.border_people = None;
        self.border_table = None;
        self.border_social_distance = None;


class circular_table(table):
    def __init__(self, (x,y), r):
        '''
        Define a circular table. Inherit from table class.
        '''
        table.__init__(self, (x,y), r);


class rectangular_table(table):
    def __init__(self, (x, y), l, w):
        '''
        Define a rectangular table. Inherit from table class.
        '''
        table.__init__(self, (x,y), r);
        