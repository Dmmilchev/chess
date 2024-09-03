import socket
import threading
import random
from Player import Player


class Game:
    def __init__(self, player1_socket: socket.socket, player2_socket: socket.socket, header_length: int, encoding: str):
        players = [player1_socket, player2_socket]
        random.shuffle(players)

        self.__players: dict[str, Player] = {
            'white': Player(players[0], header_length, encoding),
            'black': Player(players[1], header_length, encoding)
        }

        self.__turn = 'white'

        white_thread = threading.Thread(target=self.handle_player, args=('white', ))
        black_thread = threading.Thread(target=self.handle_player, args=('black', ))
        white_thread.start()
        black_thread.start()

        self.__players['white'].send('white'.encode(self.__players['white'].encoding))
        self.__players['black'].send('black'.encode(self.__players['black'].encoding))

    @staticmethod
    def get_enemy(colour: str) -> str:
        if colour == 'white':
            return 'black'
        else:
            return 'white'

    def handle_player(self, colour: str) -> None:
        enemy = self.get_enemy(colour)

        while True:
            message = self.__players[colour].receive()
            if message != b'':
                print(f'Received message from: {colour}. which is: {message}')
                self.__players[enemy].send(message)
