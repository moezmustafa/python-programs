# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 01:41:42 2015

@author: rafeh
"""

"""
Clone of 2048 game.
"""
from random import randint
import unittest
#import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    >>> merge([2, 0, 2, 4])
    [4, 4, 0, 0]
    >>> merge([0, 0, 2, 2])
    [4, 0, 0, 0]
    >>> merge([2, 2, 0, 0])
    [4, 0, 0, 0]
    >>> merge([2, 2, 2, 2, 2])
    [4, 4, 2, 0, 0]
    >>> merge([8, 16, 16, 8])
    [8, 32, 8, 0]
    """
    pairs = []
    prev = None
    for num in line:
        if not num:
            continue
        if prev is None:
            prev = num
        elif num == prev:
            pairs.append(num+prev)
            prev = None
        else:
            pairs.append(prev)
            prev = num
    if prev is not None:  # Append last value if non-zero
        pairs.append(prev)
    pairs.extend([0] * (len(line) - len(pairs)))
    return pairs

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initializing the board
        """
        self._rows = grid_height
        self._columns = grid_width
        self.board = self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self._columns)] \
                         for row in range(self._rows)]
        return self.grid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string_grid = ''
        for i in self.board:
            string_grid += "\n" + str(i)
        return "\n\n A %s x %s board %s \n" %(self._rows,self._columns,string_grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._rows

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._columns

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tile_row = randint(0, self._rows-1)
        tile_col = randint(0, self._columns-1)
        value = 2
        if randint(1,10) == 10:  # 10% chance of being 4.
            value = 4
        if self.board[tile_row][tile_col] == 0:
            self.board[tile_row][tile_col] = value
        return value  # self.board

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
class TestFullGame2048(unittest.TestCase):




    def testMerge(self):
        self.assertEqual(merge([0, 0, 2, 2]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 0, 2, 4]), [4, 4, 0, 0])
        self.assertEqual(merge([2, 2, 0, 0]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])
        self.assertEqual(merge([8, 16, 16, 8]), [8, 32, 8, 0])
        self.assertEqual(merge([8, 16, 16, 8, 2, 6]), [8, 32, 8, 2, 6, 0])

    def test__init__(self):
        self.assertIsInstance(TwentyFortyEight(5, 5), TwentyFortyEight)

    def test__str__(self):
        self.assertIsInstance(TwentyFortyEight(5, 5).__str__(), str)
        print(TwentyFortyEight(5, 5))

    def test_get_grid_height(self):
        self.assertEqual(TwentyFortyEight(3,5).get_grid_height(), 3)
        self.assertEqual(TwentyFortyEight(20,5).get_grid_height(), 20)
        self.assertNotEqual(TwentyFortyEight(5,20).get_grid_height(), 20)

    def test_get_grid_width(self):
        self.assertEqual(TwentyFortyEight(3,20).get_grid_width(), 20)
        self.assertEqual(TwentyFortyEight(20,5).get_grid_width(), 5)
        self.assertNotEqual(TwentyFortyEight(5,20).get_grid_width(), 5)

    def test_new_tile(self):
        probability = [TwentyFortyEight(5, 5).new_tile() for i in range(1000)]
        self.assertLess(probability.count(4), len(probability)*.15)
        print(TwentyFortyEight(5, 5).new_tile())
        #self.assertIsInstance(TwentyFortyEight(5, 5).new_tile(), int)



suite = unittest.TestLoader().loadTestsFromTestCase(TestFullGame2048)
unittest.TextTestRunner(verbosity=2).run(suite)
