import constants
import pygame

from game.casting.cast import Cast
from game.casting.game_board import Game_Board
from game.casting.player import Player
from game.casting.grid import Grid
from game.casting.caption import Caption
from game.directing.director import Director
from game.services.video_service import VideoService

def main():

    # initializes pygame
    pygame.init()

    # create the cast
    cast = Cast()
    cast.add_actor("players", Player(constants.PLAYER_A))
    cast.add_actor("players", Player(constants.PLAYER_B))
    cast.add_actor("grids", Game_Board(constants.ROW_LENGTH, constants.COLUMN_LENGTH))
    cast.add_actor("captions", Caption(constants.START_CAPTION))

    #start the game
    video_service = VideoService(cast.get_actor("grids", 0), cast.get_actor("players", 0), cast.get_actor("players", 1))
    director = Director(video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()