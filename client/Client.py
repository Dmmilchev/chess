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


c = Client()


def sending():
    while True:
        c.send(input())


def receiving():
    while True:
        msg = c.receive()
        if msg != '':
            print(msg)


s_thread = threading.Thread(target=sending)
r_thread = threading.Thread(target=receiving)
s_thread.start()
r_thread.start()