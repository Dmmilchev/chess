from __future__ import annotations
import pygame
from abc import ABC, abstractmethod
import os
from typing import Union


class Piece(ABC):
    def __init__(self, colour: str, height: int, width: int, position: list[int]) -> None:
        self.__colour = colour
        self.__height = height
        self.__width = width
        self.__moved = False
        if 0 <= position[0] <= 7 and 0 <= position[1] <= 7 and len(position) == 2:
            self.__position = position
        else:
            raise ValueError('Position must be an array with length 2 and values between 0 and 7')

    # GETTERS
    @property
    def colour(self) -> str:
        return self.__colour

    @property
    def position(self) -> list[int]:
        return self.__position

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def moved(self) -> bool:
        return self.__moved

    # SETTERS
    @position.setter
    def position(self, position: list[int]) -> None:
        if 0 <= position[0] <= 7 and 0 <= position[1] <= 7 and len(position) == 2:
            self.__position = position
        else:
            raise ValueError('Position must be an array with length 2 and values between 0 and 7')

    @moved.setter
    def moved(self, moved: bool) -> None:
        self.__moved = moved

    # FUNCTIONS
    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        pass

    def calculate_surface_coordinates(self) -> tuple[int, int]:
        return self.height * self.position[1], self.width * (7 - self.position[0])

    @staticmethod
    def calculate_path_to_image(piece: str, colour: str) -> str:
        image_name: str = ''
        if colour == 'white':
            image_name += 'w'
        elif colour == 'black':
            image_name += 'b'
        else:
            raise ValueError('Piece colour is either black or white!')

        if piece == 'pawn':
            image_name += 'P'
        elif piece == 'bishop':
            image_name += 'B'
        elif piece == 'knight':
            image_name += 'N'
        elif piece == 'queen':
            image_name += 'Q'
        elif piece == 'king':
            image_name += 'K'
        elif piece == 'rook':
            image_name += 'R'
        else:
            raise ValueError('Invalid name of piece!')

        image_name += '.svg'
        return os.path.join('game', 'static', 'pieces', image_name)

    def move(self, position: list[int]) -> None:
        self.position = position
        self.moved = True

    @abstractmethod
    def immediate_valid_moves(self, board: 'list[list[Piece]]'):
        pass

    @abstractmethod
    def get_danger_moves(self, board: 'list[list[Piece]]'):
        pass

    def __eq__(self, other: 'Piece'):
        if type(self) == type(self):
            return self.colour == other.colour and self.position == other.position
        return False

    def __hash__(self):
        return hash((self.colour, self.position[0], self.position[1], type(self)))
