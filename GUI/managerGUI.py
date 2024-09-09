from GUI.GUI import GUI
from client.Client import Client
from GUI.chessGUI import ChessGUI
from GUI.startGUI import StartGUI
import pygame


class ManagerGUI:
    def __init__(self, width: int, height: int, client: Client):
        self.__mode = 'start'
        self.__GUI = GUI(width, height, client)
        self.__startGUI = StartGUI(width, height)

    def start(self) -> None:
        running = True

        while running:
            if self.__mode == 'start' and self.__startGUI.while_loop():
                self.__mode = 'chess'
            if self.__mode == 'chess' and not self.__GUI.while_loop():
                running = False
