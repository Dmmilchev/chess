import socket
from constants import SERVER_PORT, SERVER_IP, HEADER, ENCODING
from Game import Game


class Server:
    def __init__(self) -> None:
        self.__ip: str = SERVER_IP
        self.__port: int = SERVER_PORT
        self.__header_length: int = HEADER
        self.__encoding: str = ENCODING

        self.__socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.ip, self.port))
        self.__socket.listen()

        self.__games: list[Game] = []

    @property
    def ip(self) -> str:
        return self.__ip

    @property
    def port(self) -> int:
        return self.__port

    @property
    def header_length(self) -> int:
        return self.__header_length

    @property
    def encoding(self) -> str:
        return self.__encoding

    def wait_for_game(self) -> None:
        """Wait's for two players to connect and then starts a game"""

        player1_socket, player1_address = self.__socket.accept()
        print(f'A player with address: {player1_address} has connected!')
        player2_socket, player2_address = self.__socket.accept()
        print(f'A player with address: {player2_address} has connected!')

        game = Game(player1_socket, player2_socket, self.header_length, self.encoding)
        self.__games.append(game)


s = Server()
while True:
    s.wait_for_game()
