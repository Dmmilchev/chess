from game.chess.pieces.Piece import Piece
import pygame
from abc import abstractmethod
from typing import Union
from game.chess.Move import Move

class Knight(Piece):
    def __init__(self, colour: str, height: int, width: int, position: list[int]) -> None:
        super().__init__(colour, height, width, position)

        path: str = super().calculate_path_to_image('knight', colour)
        self.__image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(path),
            (self.height, self.width))

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.__image, super().calculate_surface_coordinates())

    @property
    def image(self) -> pygame.Surface:
        return self.__image

    def immediate_valid_moves(self, board: 'list[list[Piece]]') -> set[Move]:
        def in_range(a: int, b: int):
            return 0 <= a <= 7 and 0 <= b <= 7
        moves: set = set()

        row = self.position[0] + 2
        col = self.position[1] + 1
        if in_range(row, col):
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))

        row = self.position[0] + 2
        col = self.position[1] - 1
        if in_range(row, col):
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))

        row = self.position[0] - 2
        col = self.position[1] + 1
        if in_range(row, col):
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))

        row = self.position[0] - 2
        col = self.position[1] - 1
        if in_range(row, col):
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))

        row = self.position[0] + 1
        col = self.position[1] + 2
        if in_range(row, col):
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))

        row = self.position[0] + 1
        col = self.position[1] - 2
        if in_range(row, col):
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))

        row = self.position[0] - 1
        col = self.position[1] + 2
        if in_range(row, col):
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))

        row = self.position[0] - 1
        col = self.position[1] - 2
        if in_range(row, col):
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))

        return moves

    def get_danger_moves(self, board: 'list[list[Piece]]') -> set[Move]:
        return self.immediate_valid_moves(board)
