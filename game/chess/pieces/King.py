from game.chess.pieces.Piece import Piece
import pygame
from abc import abstractmethod
from typing import Union
from game.chess.Move import Move


class King(Piece):
    def __init__(self, colour: str, height: int, width: int, position: list[int]) -> None:
        super().__init__(colour, height, width, position)

        path: str = super().calculate_path_to_image('king', colour)
        self.__image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(path),
            (self.height, self.width))

    def __getstate__(self) -> dict:
        state = self.__dict__.copy()
        del state['_King__image']
        return state

    def __setstate__(self, state: dict) -> None:
        self.__dict__.update(state)
        path: str = super().calculate_path_to_image('king', self.colour)
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

        # UP
        row = self.position[0] + 1
        if row < 8:
            if board[row][self.position[1]] is None:
                moves.add(Move(self, [row, self.position[1]], None))
            elif board[row][self.position[1]].colour != self.colour:
                moves.add(Move(self, [row, self.position[1]], board[row][self.position[1]]))

        # DOWN
        row = self.position[0] - 1
        if row >= 0:
            if board[row][self.position[1]] is None:
                moves.add(Move(self, [row, self.position[1]], None))
            elif board[row][self.position[1]].colour != self.colour:
                moves.add(Move(self, [row, self.position[1]], board[row][self.position[1]]))

        # RIGHT
        col = self.position[1] + 1
        if col < 8:
            if board[self.position[0]][col] is None:
                moves.add(Move(self, [self.position[0], col], None))
            elif board[self.position[0]][col].colour != self.colour:
                moves.add(Move(self, [self.position[0], col], board[self.position[0]][col]))
            col += 1

        # LEFT
        col = self.position[1] - 1
        if col >= 0:
            if board[self.position[0]][col] is None:
                moves.add(Move(self, [self.position[0], col], None))
            elif board[self.position[0]][col].colour != self.colour:
                moves.add(Move(self, [self.position[0], col], board[self.position[0]][col]))
            col -= 1

        # UP AND RIGHT
        row = self.position[0] + 1
        col = self.position[1] + 1
        if row < 8 and col < 8:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
            row += 1
            col += 1

        # UP AND LEFT
        row = self.position[0] + 1
        col = self.position[1] - 1
        if row < 8 and col >= 0:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
            row += 1
            col -= 1

        # DOWN AND RIGHT
        row = self.position[0] - 1
        col = self.position[1] + 1
        if row >= 0 and col < 8:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
            row -= 1
            col += 1

        # DOWN AND LEFT
        row = self.position[0] - 1
        col = self.position[1] - 1
        if row >= 0 and col >= 0:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
            row -= 1
            col -= 1

        # attacked_squares = self.attacked_squares(colour=self.colour, board=board, history=history)

        # REMOVING THE ATTACKED SQUARES
        # attacked_squares_positions = [x.to_position for x in attacked_squares]
        # moves = set([move for move in moves if move.to_position not in attacked_squares_positions])

        return moves

    def get_danger_moves(self, board: 'list[list[Piece]]') -> set[Move]:
        moves: set = set()

        # UP
        row = self.position[0] + 1
        if row < 8:
            if board[row][self.position[1]] is None:
                moves.add(Move(self, [row, self.position[1]], None))
            elif board[row][self.position[1]].colour != self.colour:
                moves.add(Move(self, [row, self.position[1]], board[row][self.position[1]]))

        # DOWN
        row = self.position[0] - 1
        if row >= 0:
            if board[row][self.position[1]] is None:
                moves.add(Move(self, [row, self.position[1]], None))
            elif board[row][self.position[1]].colour != self.colour:
                moves.add(Move(self, [row, self.position[1]], board[row][self.position[1]]))

        # RIGHT
        col = self.position[1] + 1
        if col < 8:
            if board[self.position[0]][col] is None:
                moves.add(Move(self, [self.position[0], col], None))
            elif board[self.position[0]][col].colour != self.colour:
                moves.add(Move(self, [self.position[0], col], board[self.position[0]][col]))
            col += 1

        # LEFT
        col = self.position[1] - 1
        if col >= 0:
            if board[self.position[0]][col] is None:
                moves.add(Move(self, [self.position[0], col], None))
            elif board[self.position[0]][col].colour != self.colour:
                moves.add(Move(self, [self.position[0], col], board[self.position[0]][col]))
            col -= 1

        # UP AND RIGHT
        row = self.position[0] + 1
        col = self.position[1] + 1
        if row < 8 and col < 8:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
            row += 1
            col += 1

        # UP AND LEFT
        row = self.position[0] + 1
        col = self.position[1] - 1
        if row < 8 and col >= 0:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
            row += 1
            col -= 1

        # DOWN AND RIGHT
        row = self.position[0] - 1
        col = self.position[1] + 1
        if row >= 0 and col < 8:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
            row -= 1
            col += 1

        # DOWN AND LEFT
        row = self.position[0] - 1
        col = self.position[1] - 1
        if row >= 0 and col >= 0:
            if board[row][col] is None:
                moves.add(Move(self, [row, col], None))
            elif board[row][col].colour != self.colour:
                moves.add(Move(self, [row, col], board[row][col]))
            row -= 1
            col -= 1

        return moves

    # def is_check(self, game: Game) -> bool:
    #     attacked_squares_positions = [x.to_position for x in self.attacked_squares(self.colour, game)]
    #     for position in attacked_squares_positions:
    #         if position == self.position:
    #             return True
    #     return False
    #
    # @staticmethod
    # def attacked_squares(colour: str, game: Game) -> set[Move]:
    #     attacked_squares: set[Move] = set()
    #     board = game.board.board
    #
    #     if colour == 'white':
    #         for i in range(8):
    #             for j in range(8):
    #                 if board[i][j] is not None and board[i][j].colour == 'black':
    #                     attacked_squares = attacked_squares.union(board[i][j].get_danger_moves(game))
    #
    #     if colour == 'black':
    #         for i in range(8):
    #             for j in range(8):
    #                 if board[i][j] is not None and board[i][j].colour == 'white':
    #                     attacked_squares = attacked_squares.union(board[i][j].get_danger_moves(game))
    #
    #     return attacked_squares
