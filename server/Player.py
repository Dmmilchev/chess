import socket


class Player:
    def __init__(self, player_socket: socket.socket, header_length: int, encoding: str):
        self.__socket = player_socket
        self.__header_length = header_length
        self.__encoding = encoding

    def send(self, message: str) -> None:
        header: str = str(len(message))
        header += (' ' * (self.__header_length - int(len(header))))
        self.__socket.send(header.encode(self.__encoding))
        self.__socket.send(message.encode(self.__encoding))

    def receive(self) -> str:
        header: str = self.__socket.recv(self.__header_length).decode(self.__encoding)
        if header == '':
            return ''
        header_length: int = int(header)
        message: str = self.__socket.recv(header_length).decode(self.__encoding)
        return message
