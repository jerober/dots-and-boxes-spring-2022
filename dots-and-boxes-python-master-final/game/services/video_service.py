import pygame
import constants

from game.casting.player import Player

class VideoService():
    def __init__(self, grid, player_a, player_b):
        """Initializes screen components.
        
        Attributes:
        _screen (obj): display window
        _empty_img (image): empty box
        _a_img (image): player a filled box
        _b_img (image): player b filled box
        _grid_dot (image): grid dot
        _horizontal_line (image): horizontal filled line
        _empty_horizontal_line (image): empty horizontal line
        _vertical_line (image): vertical filled line
        _empty_vertical_line (image): empty vertical line
        _grid (obj): grid
        _player_a (obj): player object
        _player_b (obj): player object
        """
        #initializes screen attributes
        self._screen = pygame.display.set_mode([constants.BOX_SIZE * constants.ROW_LENGTH + constants.WALL_SIZE, constants.BOX_SIZE * constants.COLUMN_LENGTH + constants.WALL_SIZE])
        # initially loads all images
        self._empty_img = pygame.image.load("game/pics/empty_img.png")
        self._a_img = pygame.image.load("game/pics/a_img.png")
        self._b_img = pygame.image.load("game/pics/b_img.png")
        self._grid_dot = pygame.image.load("game/pics/grid_dot.png")
        self._horizontal_line = pygame.image.load("game/pics/horizontal_line.png")
        self._empty_horizontal_line = pygame.image.load("game/pics/empty_horizontal_line.png")
        self._vertical_line = pygame.image.load("game/pics/vertical_line.png")
        self._empty_vertical_line = pygame.image.load("game/pics/empty_vertical_line.png")
        self._grid = grid
        self._player_a = player_a
        self._player_b = player_b

    def load_screen(self):
        """
        Loads the screen
        Use the current grid and wall information to
        update the players screen
        """
        self._screen.fill(0)

        # loop over all boxes in grid to check vlaues for drawing images
        for column in range(constants.COLUMN_LENGTH):
            for row in range(constants.ROW_LENGTH):
                x, y = column * constants.BOX_SIZE, row * constants.BOX_SIZE
                self._screen.blit(self._grid_dot, (x, y))
                x += 4
                if not self._grid.get_upper_walls_flag(column, row):
                    self._screen.blit(self._empty_horizontal_line, (x, y))
                else:
                    self._screen.blit(self._horizontal_line, (x, y))
                x -= 4
                y += 4
                if not self._grid.get_left_walls_flag(column, row):
                    self._screen.blit(self._empty_vertical_line, (x, y))
                else:
                    self._screen.blit(self._vertical_line, (x, y))

                # calculate x and y in pixels based on constants
                x, y = column * constants.BOX_SIZE + constants.WALL_SIZE, row * constants.BOX_SIZE + constants.WALL_SIZE

                #draws the images in the proper locations
                if self._grid.get_grid_box_status(column, row) == 0:
                    self._screen.blit(self._empty_img, (x, y))
                elif self._grid.get_grid_box_status(column, row) == 1:
                    self._screen.blit(self._a_img, (x, y))
                elif self._grid.get_grid_box_status(column, row) == 2:
                    self._screen.blit(self._b_img, (x, y))

    def draw_wall(self, upper_wall, wall_x, wall_y):
        """Draws a wall when it is clicked on
        Args: 
        upper_wall: (bool)
        wall_x, wall_y (int): position in the matrix"""
        if upper_wall:
            self._screen.blit(self._horizontal_line, (wall_x, wall_y))
        else:
            self._screen.blit(self._vertical_line, (wall_x, wall_y))

    def set_all_slots(self, turn):
        """
        Find all newly closed boxes and close them for the current player
        :return: number of closed boxes
        """
        to_return = 0

        for column in range(constants.COLUMN_LENGTH):
            for row in range(constants.ROW_LENGTH):
                if self._grid.get_grid_box_status(column, row)!= 0 or self._grid.get_number_of_walls(column, row) < constants.WALL_SIZE:
                    continue

                if turn == constants.PLAYER_A:
                    self._grid.set_grid_box_status(column, row, 1)
                    self._screen.blit(self._a_img, (column * constants.BOX_SIZE + constants.WALL_SIZE, row * constants.BOX_SIZE + constants.WALL_SIZE))
                    self._player_a.add_points(1)
                elif turn == constants.PLAYER_B:
                    self._grid.set_grid_box_status(column, row, 2)
                    self._screen.blit(self._b_img, (column * constants.BOX_SIZE + constants.WALL_SIZE, row * constants.BOX_SIZE + constants.WALL_SIZE))
                    self._player_b.add_points(1)
                to_return += 1
        pygame.display.flip()
        return to_return

