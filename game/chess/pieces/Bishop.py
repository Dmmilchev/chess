from game.chess.pieces.Piece import Piece
import pygame
from abc import abstractmethod
from typing import Union
from game.chess.Move import Move


class Bishop(Piece):
    def __init__(self, colour: str, height: int, width: int, position: list[int]) -> None:
        super().__init__(colour, height, width, position)

        path: str = super().calculate_path_to_image('bishop', colour)
        self.__image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(path),
            (self.height, self.width))

    def __getstate__(self) -> dict:
        state = self.__dict__.copy()
        del state['_Bishop__image']
        return state

    def __setstate__(self, state: dict) -> None:
        self.__dict__.update(state)
        path: str = super().calculate_path_to_image('bishop', self.colour)
        self.__image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(path),
            (self.height, self.width))

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.__image, super().calculate_surface_coordinates())

    @property
    def image(self) -> pygame.Surface:
        return self.__image

    def immediate_valid_moves(self, board: 'list[list[Piece]]') -> set[Move]:
        moves: set = set()

        # UP AND RIGHT
        row = self.position[0] + 1
        col = self.position[1] + 1
        while row < 8 and col < 8:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour == self.colour:
                break
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
                break
            row += 1
            col += 1

        # UP AND LEFT
        row = self.position[0] + 1
        col = self.position[1] - 1
        while row < 8 and col >= 0:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour == self.colour:
                break
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
                break
            row += 1
            col -= 1

        # DOWN AND RIGHT
        row = self.position[0] - 1
        col = self.position[1] + 1
        while row >= 0 and col < 8:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour == self.colour:
                break
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
                break
            row -= 1
            col += 1

        # DOWN AND LEFT
        row = self.position[0] - 1
        col = self.position[1] - 1
        while row >= 0 and col >= 0:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour == self.colour:
                break
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
                break
            row -= 1
            col -= 1

        return moves

    def get_danger_moves(self, board: 'list[list[Piece]]') -> set[Move]:
        return self.immediate_valid_moves(board)
