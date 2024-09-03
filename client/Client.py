import socket
import threading

from server.constants import SERVER_IP, SERVER_PORT, HEADER, ENCODING


class Client:
    def __init__(self) -> None:
        self.__server_ip: str = SERVER_IP
        self.__server_port: int = SERVER_PORT
        self.__header_length: int = HEADER
        self.__encoding: str = ENCODING

        self.__socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((self.__server_ip, self.__server_port))

        colour: bytes = self.receive()
        self.__colour: str = colour.decode(ENCODING)
        print(f'You are playing with {self.__colour} pieces.')

    @property
    def colour(self) -> str:
        return self.__colour

    def send(self, message: bytes) -> None:
        header: str = str(len(message))
        header += (' ' * (self.__header_length - int(len(header))))
        self.__socket.send(header.encode(self.__encoding))
        self.__socket.send(message)

    def receive(self) -> bytes:
        header: str = self.__socket.recv(self.__header_length).decode(self.__encoding)
        if header == '':
            return b''
        header_length: int = int(header)
        message: bytes = self.__socket.recv(header_length)
        return message
