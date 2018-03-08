"""Problem from "Cracking the Coding Interview" (recursion section):

Suppose you have a robot that can only move left or down, and the robot
needs to move from the upper left corner of a grid to the lower right
corner, but some of the squares may be blocked.

Given a grid with r rows and c columns, find a path for the robot.
"""

import numpy as np

class Grid():
    """Class to encode a grid with some squares blocked.
    """
    def __init__(self, arr):
        """
        Parameters
        ----------
        arr : numpy array of ints
                A 2D numpy array representing a rectangular grid of squares
                that are open (0) or blocked (1).
        """
        self.grid = arr
        self.n_rows, self.n_cols = arr.shape

    def rc_to_index(self, r,c):
        """
        Converts a row, col pair to an index.
        """
        return self.n_rows-r, self.n_cols-c

    def down_is_open(self, r,c):
        """
        Checks whether the square below the 'current position'
        is open or blocked.
        """
        #Get current index
        (i,j) = self.rc_to_index(r,c)
        if i == self.n_rows-1:
            return False

        return self.grid[i+1,j] == 0

    def right_is_open(self, r,c):
        """
        Checks whether the square to the right of the 'current position'
        is open or blocked.
        """
        #Get current index
        (i,j) = self.rc_to_index(r,c)
        if j == self.n_cols-1:
            return False

        return self.grid[i,j+1] == 0



class PathFinder():
    """
    Class to compute the path of the robot.
    """
    def __init__(self, grid):
        self.grid = grid

    def find_path(self, r=None, c=None):
        """Recursively finds an unblocked down-right path from the upper
        left to the lower right corner of the lower right (r x c)-subgrid of
        this object's grid. Thus,

        Parameters
        ----------
        r : int
            The number of rows of the subgrid, i.e. the number of rows
            (inclusive) from the current position to the right edge of
            the full grid. If `None` (default), the total number of rows
            in the full grid is assumed.
        c : int
            The number of columns of the subgrid, i.e. the number of columns
            (inclusive) from the current position to the bottom edge of
            the full grid. If `None` (default), the total number of columns
            in the full grid is assumed.

        Returns
        -------
        path : str or None
            A string representing the path of the robot, such as "RRDDDR",
            with 'R' representing a rightward move, and 'D' representing
            a downward move. If the robot is already in the lower right
            corner, the empty string "" is returned. If no down-right
            path exists, None is returned. The algorithm uses a greedy
            strategy, searching to the right first, then going down if no
            rightward path is found.
        """
        #Set the default values of r and c if None passed.
        if r is None:
            r = self.grid.n_rows
        if c is None:
            c = self.grid.n_cols

        #If we're already at lower right corner, return the identity move.
        if r == 1 and c == 1:
            return ""

        #Try moving right
        if self.grid.right_is_open(r,c):
            #If the rightward square is open, we know we can move there,
            #so try finding a path from that position.
            path = self.find_path(r, c-1)
            #If we found a path, append our rightward move to the beginning.
            if path is not None:
                return "R" + path

        #Try moving down if moving right wasn't successful.
        #This occurs if rightward square was blocked or if we found no path
        # by moving right.
        if self.grid.down_is_open(r,c):
            path = self.find_path(r-1, c)
            if path is not None:
                return "D" + path

        #If we found no valid path by moving either right or down, then there
        #is no valid path from the current position, so return None.
        return None
