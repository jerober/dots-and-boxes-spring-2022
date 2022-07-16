import imp
import numpy as np

from game.casting.actor import Actor
from game.casting.int_grid import Int_Grid
from game.casting.bool_grid import Bool_Grid

class Game_Board(Actor):

    def __init__(self, row_length, column_length):
        """Initilizes grid representation.
        
        Attributes:
        _row_length (int): takes row_length arg
        _column_length (int): takes column_length arg
        _grid_size (int): _row_length multiplied by _column_length
        _grid_box_statuses (2-D matrix): built in the int_grid object
        _upper_walls_set_flags (2-D matrix): built in the bool_grid object
        _left_walls_set_flags (2-D matrix):built in the bool_grid object

        Args:
            row_length (int): sets _row_length for grid
            column_length (int): sets _column_length for grid
        """
        super().__init__()
        self._row_length = row_length
        self._column_length = column_length
        self._grid_size = self._row_length * self._column_length
        #initialize three matricies 
        self._grid_box_status = Int_Grid(self._column_length, self._row_length)
        self._upper_walls_flags = Bool_Grid(self._column_length, self._row_length)
        self._left_walls_flags = Bool_Grid(self._column_length, self._row_length)

        # initializes lines in the outside border on the grid
        for column in range(self._column_length):
            for row in range(self._row_length):
                if column == 0:
                    self._left_walls_flags.set_element(column, row, True)
                if row == 0:
                    self._upper_walls_flags.set_element(column, row, True)

    def get_upper_walls_flag(self, column, row):
        """Returns _upper_walls_flags matrix"""
        return self._upper_walls_flags.get_element(column, row)

    def get_left_walls_flag(self, column, row):
        """Returns _left_walls_flags matrix"""
        return self._left_walls_flags.get_element(column, row)

    def get_grid_box_status(self, column, row):
        """Returns _grid_box_statuses matrix"""
        return self._grid_box_status.get_element(column, row)

    @staticmethod
    def get_wall(pos_x, pos_y, box_size, wall_size):
        rest_x = pos_x % box_size
        rest_y = pos_y % box_size

        wall_slot_x = pos_x//box_size
        wall_slot_y = pos_y//box_size

        # in a corner
        if rest_x < wall_size and rest_y < wall_size:
            return -1, -1

        if rest_x < wall_size:
            # is left wall of the slot
            return wall_slot_x * box_size, wall_slot_y * box_size + wall_size

        if rest_y < wall_size:
            # is upper wall of the slot
            return wall_slot_x * box_size + wall_size, wall_slot_y * box_size

        # inside the box => not a wall
        return -1, -1

    def get_number_of_walls(self, column, row):
        """
        Get the number of set walls around the passed slot
        :param slot_column: x of the slot
        :param slot_row: y of the slot
        :return: number of set walls
        """
        number_of_walls = 0

        if column == self._column_length - 1:
            number_of_walls += 1
        elif self.get_left_walls_flag(column + 1, row):
            number_of_walls += 1

        if row == self._row_length - 1:
            number_of_walls += 1
        elif self.get_upper_walls_flag(column, row + 1):
            number_of_walls += 1

        if self.get_left_walls_flag(column, row):
            number_of_walls += 1

        if self.get_upper_walls_flag(column, row):
            number_of_walls += 1

        return number_of_walls

    def set_upper_walls_flag(self, column, row, value):
        """Sets _upper_walls_flags matrix"""
        self._upper_walls_flags.set_element(column, row, value)

    def set_left_walls_flag(self, column, row, value):
        """Sets _left_walls_flags matrix"""
        self._left_walls_flags.set_element(column, row, value)

    def set_grid_box_status(self, column, row, value):
        """Sets _grid_box_statuses matrix"""
        self._grid_box_status.set_element(column, row, value)


