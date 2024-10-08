from game.chess.pieces.Piece import Piece
from game.chess.Move import Move
import pygame
import os
from typing import Union


class Pawn(Piece):
    def __init__(self, colour: str, height: int, width: int, position: list[int]) -> None:
        super().__init__(colour, height, width, position)

        path: str = super().calculate_path_to_image('pawn', colour)
        self.__image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(path),
            (self.height, self.width))

    def __getstate__(self) -> dict:
        state = self.__dict__.copy()
        del state['_Pawn__image']
        return state

    def __setstate__(self, state: dict) -> None:
        self.__dict__.update(state)
        path: str = super().calculate_path_to_image('pawn', self.colour)
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

        if self.colour == 'white':

            # FORWARD
            if not self.moved:

                if board[self.position[0] + 1][self.position[1]] is None:
                    moves.add(Move(self, [self.position[0] + 1, self.position[1]], None))

                    if board[self.position[0] + 2][self.position[1]] is None:
                        moves.add(Move(self, [self.position[0] + 2, self.position[1]], None))

            if self.moved:
                if board[self.position[0] + 1][self.position[1]] is None:
                    moves.add(Move(self, [self.position[0] + 1, self.position[1]], None))

            # DIAGONALS
            if self.position[1] > 0:
                enemy = board[self.position[0] + 1][self.position[1] - 1]
                if enemy is not None and enemy.colour == 'black':
                    moves.add(Move(self,
                                   [self.position[0] + 1, self.position[1] - 1],
                                   enemy))
            if self.position[1] < 7:
                enemy = board[self.position[0] + 1][self.position[1] + 1]
                if enemy is not None and enemy.colour == 'black':
                    moves.add(Move(self,
                                   [self.position[0] + 1, self.position[1] + 1],
                                   enemy))

        elif self.colour == 'black':

            # FORWARD
            if not self.moved:

                if board[self.position[0] - 1][self.position[1]] is None:
                    moves.add(Move(self, [self.position[0] - 1, self.position[1]], None))

                    if board[self.position[0] - 2][self.position[1]] is None:
                        moves.add(Move(self, [self.position[0] - 2, self.position[1]], None))

            if self.moved:
                if board[self.position[0] - 1][self.position[1]] is None:
                    moves.add(Move(self, [self.position[0] - 1, self.position[1]], None))

            # DIAGONALS
            if self.position[1] > 0:
                enemy = board[self.position[0] - 1][self.position[1] - 1]
                if enemy is not None and enemy.colour == 'white':
                    moves.add(Move(self,
                                   [self.position[0] - 1, self.position[1] - 1],
                                   enemy))
            if self.position[1] < 7:
                enemy = board[self.position[0] - 1][self.position[1] + 1]
                if enemy is not None and enemy.colour == 'white':
                    moves.add(Move(self,
                                   [self.position[0] - 1, self.position[1] + 1],
                                   enemy))

        return moves

    def get_danger_moves(self, board: 'list[list[Piece]]') -> set[Move]:
        valid_moves = self.immediate_valid_moves(board)
        danger_moves = set([move for move in valid_moves if self.position[1] != move.to_position[1]])

        if self.colour == 'white':
            if self.position[1] > 0:
                danger_moves.add(Move(self, [self.position[0] + 1, self.position[1] - 1], None))
            if self.position[1] < 7:
                danger_moves.add(Move(self, [self.position[0] + 1, self.position[1] + 1], None))

        if self.colour == 'black':
            if self.position[1] > 0:
                danger_moves.add(Move(self, [self.position[0] - 1, self.position[1] - 1], None))
            if self.position[1] < 7:
                danger_moves.add(Move(self, [self.position[0] - 1, self.position[1] + 1], None))

        return danger_moves
