import pygame
import os
import game
import game.chess
from game.Game import Game
from game.chess.pieces.King import King


class ChessGUI:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

        self.__game = Game(self.__height, self.__height) # We want the board to be a square, that's why pass heightX2

    # GETTERS
    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    def while_loop(self) -> None:
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        running = True
        mouse_pressed = False

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # SELECT A PIECE
                    if not mouse_pressed and 0 <= event.pos[0] <= 800 and 0 <= event.pos[1] <= 800:
                        self.__game.handle_piece(event.pos)
                        mouse_pressed = True

                if event.type == pygame.MOUSEBUTTONUP:
                    # Reset the flag when the mouse button is released
                    mouse_pressed = False

            # adding background:
            self.__game.draw(screen)

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()
