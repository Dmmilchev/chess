import socket


SERVER_IP: str = socket.gethostbyname(socket.gethostname())
SERVER_PORT: int = 12344
HEADER: int = 16
ENCODING: str = 'utf-8'
