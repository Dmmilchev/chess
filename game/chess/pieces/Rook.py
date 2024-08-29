from game.chess.pieces.Piece import Piece
import pygame
from abc import abstractmethod
from typing import Union
from game.chess.Move import Move
from game.Game import Game


class Rook(Piece):
    def __init__(self, colour: str, height: int, width: int, position: list[int]) -> None:
        super().__init__(colour, height, width, position)

        path: str = super().calculate_path_to_image('rook', colour)
        self.__image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(path),
            (self.height, self.width))

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.__image, super().calculate_surface_coordinates())

    @property
    def image(self) -> pygame.Surface:
        return self.__image

    def valid_moves(self, game: Game) -> set[Move]:
        moves: set = set()
        board = game.board.board

        # UP
        row = self.position[0] + 1
        while row < 8:
            if board[row][self.position[1]] is None:
                moves.add(Move(self, [row, self.position[1]], None))
            elif board[row][self.position[1]].colour == self.colour:
                break
            elif board[row][self.position[1]].colour != self.colour:
                moves.add(Move(self, [row, self.position[1]], board[row][self.position[1]]))
                break
            row += 1

        # DOWN
        row = self.position[0] - 1
        while row >= 0:
            if board[row][self.position[1]] is None:
                moves.add(Move(self, [row, self.position[1]], None))
            elif board[row][self.position[1]].colour == self.colour:
                break
            elif board[row][self.position[1]].colour != self.colour:
                moves.add(Move(self, [row, self.position[1]], board[row][self.position[1]]))
                break
            row -= 1

        # RIGHT
        col = self.position[1] + 1
        while col < 8:
            if board[self.position[0]][col] is None:
                moves.add(Move(self, [self.position[0], col], None))
            elif board[self.position[0]][col].colour == self.colour:
                break
            elif board[self.position[0]][col].colour != self.colour:
                moves.add(Move(self, [self.position[0], col], board[self.position[0]][col]))
                break
            col += 1

        # LEFT
        col = self.position[1] - 1
        while col >= 0:
            if board[self.position[0]][col] is None:
                moves.add(Move(self, [self.position[0], col], None))
            elif board[self.position[0]][col].colour == self.colour:
                break
            elif board[self.position[0]][col].colour != self.colour:
                moves.add(Move(self, [self.position[0], col], board[self.position[0]][col]))
                break
            col -= 1

        return moves

    def get_danger_moves(self, game: Game) -> set[Move]:
        return self.valid_moves(game)
