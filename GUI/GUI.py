import pygame
import threading
from GUI.chessGUI import ChessGUI
from client.Client import Client


class GUI:
    def __init__(self, width: int, height: int, client: Client) -> None:
        self.__width = width
        self.__height = height
        self.__client = client
        self.__chessGUI = ChessGUI(width, height, client)

    def while_loop(self) -> bool:
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode((self.__width, self.__height))
        clock = pygame.time.Clock()
        running = True

        # Thread for receiving messages from enemy
        receive_thread = threading.Thread(target=self.__chessGUI.receiving)
        receive_thread.start()

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                self.__chessGUI.handle_event(event)

            # adding background:
            self.__chessGUI.draw(screen)

            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()
        return False
