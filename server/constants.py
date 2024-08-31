import socket


SERVER_IP: str = socket.gethostbyname(socket.gethostname())
SERVER_PORT: int = 5555
HEADER: int = 16
ENCODING: str = 'utf-8'
