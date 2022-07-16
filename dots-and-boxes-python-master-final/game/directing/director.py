import constants
import pygame

class Director:

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.

        Attributes: 
        _is_game_over (bool): False
        _turn (str): constants.PLAYER_A
        """
        self._is_game_over = False
        self._turn = constants.PLAYER_A
        self._video_service = video_service

    def start_game(self, cast):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        #creates variables for manipulating players in the cast
        player_a = cast.get_actor("players", 0)
        player_b = cast.get_actor("players", 1)

        # sets initial caption
        pygame.display.set_caption(f'{self._turn} {constants.START_CAPTION} {constants.PLAYER_A} {player_a.get_points()} {constants.PLAYER_B} {player_b.get_points()}')
        
        screen = pygame.display.set_mode([constants.BOX_SIZE * constants.ROW_LENGTH + constants.WALL_SIZE, constants.BOX_SIZE * constants.COLUMN_LENGTH + constants.WALL_SIZE])
        self._video_service.load_screen()
        pygame.display.flip()

        """This is the game flow loop after game initilization."""
        while not self._is_game_over:
            # go through all events and check the types
            for event in pygame.event.get():
                # quit the game when the player closes it
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                # On mouse click
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    if self._is_game_over:
                        continue
                    # get the current position of the cursor
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                #     # check whether it was a not set wall that was clicked
                    grid = cast.get_actor("grids", 0)
                    wall_x, wall_y = grid.get_wall(x, y, constants.BOX_SIZE, constants.WALL_SIZE)

                    if not  (wall_x >= 0 and wall_y >= 0):
                        continue

                    #checks to see if the wall is an upper wall (sets upper_wall var to True if it is an upper wall. False means it is a left wall)
                    upper_wall = wall_y % constants.BOX_SIZE == 0

                    if upper_wall:
                        if not grid.get_upper_walls_flag(wall_x//constants.BOX_SIZE, wall_y//constants.BOX_SIZE):
                            grid.set_upper_walls_flag(wall_x//constants.BOX_SIZE, wall_y//constants.BOX_SIZE, True)
                            self._video_service.draw_wall(upper_wall, wall_x, wall_y)
                            self._video_service.load_screen()
                        else:
                            continue
                    else:
                        if not grid.get_left_walls_flag(wall_x//constants.BOX_SIZE, wall_y//constants.BOX_SIZE):
                            grid.set_left_walls_flag(wall_x//constants.BOX_SIZE, wall_y//constants.BOX_SIZE, True)
                            self._video_service.draw_wall(upper_wall, wall_x, wall_y)
                            self._video_service.load_screen()
                        else:
                            continue

                    #if the player does not close a box, switch whose turn it is
                    if not self._video_service.set_all_slots(self._turn) > 0:
                        if self._turn == constants.PLAYER_A:
                            self._turn = constants.PLAYER_B
                        elif self._turn == constants.PLAYER_B:
                            self._turn = constants.PLAYER_A

                    #gets the points of player for the caption
                    player_a_points = player_a.get_points()
                    player_b_points = player_b.get_points()

                    #evaluates if game is won, otherwise it redraws screen with updated caption
                    if player_a_points + player_b_points == constants.ROW_LENGTH * constants.COLUMN_LENGTH:
                        won_caption = f"Game Over {constants.PLAYER_A}: {player_a_points} {constants.PLAYER_B}: {player_b_points}"

                        # set the display caption
                        pygame.display.set_caption(won_caption)

                        # update the players screen
                        pygame.display.flip()
                    else:
                        # set the display caption
                        pygame.display.set_caption(f'{self._turn} {constants.START_CAPTION} {constants.PLAYER_A} {player_a.get_points()} {constants.PLAYER_B} {player_b.get_points()}')

                        # update the players screen
                        pygame.display.flip()

