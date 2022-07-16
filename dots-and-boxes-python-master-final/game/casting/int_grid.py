import numpy as np

from game.casting.grid import Grid

class Int_Grid(Grid):
    """Builds a matrix of ints. Default start = 0"""
    def __init__(self, column_length, row_length):
        super().__init__()
        self._matrix = np.zeros((column_length, row_length), np.int)

    def get_element(self, column, row):
        return self._matrix[column, row]

    def set_element(self, column, row, value):
        self._matrix[column, row] = value