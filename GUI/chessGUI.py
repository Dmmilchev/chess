import pygame
from game.Game import Game
from client.Client import Client
import threading
from game.chess.Move import Move
import pickle


class ChessGUI:
    def __init__(self, width: int, height: int, client: Client) -> None:
        self.__width = width
        self.__height = height
        self.__client = client
        self.__game = Game(self.__height, self.__height)  # We want the board to be a square, that's why pass heightX2

    # GETTERS
    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    def receiving(self) -> None:
        while True:
            message = self.__client.receive()
            if message != b'':
                move: Move = pickle.loads(message)
                self.__game.execute_move(move)

    def while_loop(self) -> None:
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        running = True
        mouse_pressed = False

        # Thread for receiving messages from enemy
        receive_thread = threading.Thread(target=self.receiving)
        receive_thread.start()

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # SELECT A PIECE
                    if not mouse_pressed and 0 <= event.pos[0] <= 800 and 0 <= event.pos[1] <= 800:
                        # Handles turn based logic also.
                        played_move: Move = self.__game.handle_piece(event.pos)
                        if played_move is not None and played_move.piece.colour != self.__client.colour:
                            self.__game.undo_move()
                        if played_move is not None:
                            self.__client.send(pickle.dumps(played_move))
                        mouse_pressed = True

                if event.type == pygame.MOUSEBUTTONUP:
                    # Reset the flag when the mouse button is released
                    mouse_pressed = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:
                        self.__game.undo_move()
            # adding background:
            self.__game.draw(screen)

            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()
