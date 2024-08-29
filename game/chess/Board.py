from game.chess.pieces.Piece import Piece
import pygame
import os
from typing import Union
from game.chess.pieces.Pawn import Pawn
from game.chess.pieces.King import King
from game.chess.pieces.Bishop import Bishop
from game.chess.pieces.Rook import Rook
from game.chess.pieces.Queen import Queen
from game.chess.pieces.Knight import Knight
from game.chess.Move import Move


class Board:
    def __init__(self, height: int, width: int) -> None:
        self.__height: int = height
        self.__width: int = width
        self.__piece_height: int = int(height / 8)
        self.__piece_width: int = int(width / 8)
        self.__image = pygame.transform.scale(
            pygame.image.load(os.path.join('game', 'static', 'board.jpg')),
            (self.__height, self.__width))
        self.__board: list[list[Union[Piece, None]]] = self.setup_board(self)
        self.__selected_piece: Union[Piece, None] = None
        self.__history: list[Move] = []

    # GETTERS
    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def board(self) -> list[list[Piece]]:
        return self.__board

    @property
    def piece_height(self) -> int:
        return self.__piece_height

    @property
    def piece_width(self) -> int:
        return self.__piece_width

    @property
    def selected_piece(self) -> Union[Piece, None]:
        return self.__selected_piece

    @property
    def history(self) -> list[Move]:
        return self.__history

    # SETTERS
    @board.setter
    def board(self, board: list[list[Union[Piece, None]]]) -> None:
        self.__board = board

    @selected_piece.setter
    def selected_piece(self, selected_piece: Union[Piece, None]) -> None:
        self.__selected_piece = selected_piece

    @history.setter
    def history(self, history: list[Move]) -> None:
        self.__history = history

    # FUNCTIONS
    def draw(self, surface: pygame.Surface) -> None:
        def draw_rectangle(position: list[int]) -> None:
            light_green = (144, 238, 144)
            coord_row = 7 - position[0]
            coord_col = position[1]
            pygame.draw.rect(surface, light_green, (self.piece_width * coord_col + 3,
                                                    self.piece_height * coord_row + 3,
                                                    self.piece_height - 6, self.piece_width - 6))

        surface.blit(self.__image, (0, 0))

        if self.selected_piece is not None:
            draw_rectangle(self.selected_piece.position)
            for move in self.valid_moves(self.selected_piece):
                draw_rectangle(move.to_position)

        for row in range(8):
            for col in range(8):
                if self.board[row][col] is not None:
                    self.board[row][col].draw(surface)

    @staticmethod
    def setup_board(self) -> list[list[Union[Piece, None]]]:
        board: list[list[Union[Piece, None]]] = [[None for _ in range(8)] for _ in range(8)]
        for col in range(8):
            board[1][col] = Pawn('white', self.__piece_height, self.__piece_width, [1, col])
            board[6][col] = Pawn('black', self.__piece_height, self.__piece_width, [6, col])
        # WHITE PIECES
        board[0][0] = Rook('white', self.__piece_height, self.__piece_width,[0, 0])
        board[0][7] = Rook('white', self.__piece_height, self.__piece_width, [0, 7])
        board[0][1] = Knight('white', self.__piece_height, self.__piece_width, [0, 1])
        board[0][6] = Knight('white', self.__piece_height, self.__piece_width, [0, 6])
        board[0][2] = Bishop('white', self.__piece_height, self.__piece_width, [0, 2])
        board[0][5] = Bishop('white', self.__piece_height, self.__piece_width, [0, 5])
        board[0][3] = Queen('white', self.__piece_height, self.__piece_width, [0, 3])
        board[0][4] = King('white', self.__piece_height, self.__piece_width, [0, 4])

        # BLACK PIECES
        board[7][0] = Rook('black', self.__piece_height, self.__piece_width,[7, 0])
        board[7][7] = Rook('black', self.__piece_height, self.__piece_width, [7, 7])
        board[7][1] = Knight('black', self.__piece_height, self.__piece_width, [7, 1])
        board[7][6] = Knight('black', self.__piece_height, self.__piece_width, [7, 6])
        board[7][2] = Bishop('black', self.__piece_height, self.__piece_width, [7, 2])
        board[7][5] = Bishop('black', self.__piece_height, self.__piece_width, [7, 5])
        board[7][3] = Queen('black', self.__piece_height, self.__piece_width, [7, 3])
        board[7][4] = King('black', self.__piece_height, self.__piece_width, [7, 4])

        # TODO TESTING MOVEMENT SHOULD DELETE
        board[4][3] = Knight('black', self.__piece_height, self.__piece_width, [4, 3])
        board[4][4] = Knight('white', self.__piece_height, self.__piece_width, [4, 4])

        return board

    def check_for_promotion(self) -> None:
        for i in range(8):
            if isinstance(self.board[7][i], Pawn) and self.board[7][i].colour == 'white':
                self.board[7][i] = None
                self.board[7][i] = Queen('white', self.__piece_height, self.__piece_width, [7, i])
                self.history.append(Move(self.board[7][i], to_position=[7, i], captured_piece=None))
        for i in range(8):
            if isinstance(self.board[0][i], Pawn) and self.board[7][i].colour == 'black':
                self.board[0][i] = None
                self.board[0][i] = Queen('black', self.__piece_height, self.__piece_width, [0, i])
                self.history.append(Move(self.board[0][i], to_position=[0, i], captured_piece=None))

    def get_danger_moves(self, colour: str) -> set[Move]:
        danger_moves: set[Move] = set()
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece is not None and piece.colour == colour:
                    danger_moves = danger_moves.union(piece.get_danger_moves(self.board))
        return danger_moves

    def is_check(self, colour: str) -> bool:
        def get_king() -> Piece:
            for i in range(8):
                for j in range(8):
                    piece = self.board[i][j]
                    if isinstance(piece, King) and piece.colour == colour:
                        return piece

        danger_moves: set[Move] = set()
        if colour == 'white':
            danger_moves = self.get_danger_moves('black')
        if colour == 'black':
            danger_moves = self.get_danger_moves('white')

        attacked_squares = [x.to_position for x in danger_moves]
        return get_king().position in attacked_squares

    def execute_move(self, move: Move) -> None:
        if move.captured_piece is not None:
            self.board[move.captured_piece.position[0]][move.captured_piece.position[1]] = None
        self.board[move.to_position[0]][move.to_position[1]] = move.piece
        self.board[move.from_position[0]][move.from_position[1]] = None
        move.piece.move(move.to_position)
        self.history.append(move)
        self.check_for_promotion()

    def undo_move(self) -> None:
        if len(self.history) < 1:
            raise ValueError('You have to play a move before undoing it.')
        move = self.history[-1]
        self.board[move.from_position[0]][move.from_position[1]] = move.piece
        self.board[move.to_position[0]][move.to_position[1]] = None
        move.piece.position = move.from_position
        if move.captured_piece is not None:
            self.board[move.captured_piece_position[0]][move.captured_piece_position[1]] = move.captured_piece
        if move.piece not in [past_move.piece for past_move in self.history[:-1:1]]:
            move.piece.moved = False
        self.history.pop()

    def valid_moves(self, piece: Piece) -> set[Move]:
        moves: set[Move] = piece.immediate_valid_moves(self.board)

        # EN PASSANT WHITE
        if isinstance(piece, Pawn) and piece.colour == 'white' and len(self.history) > 0:
            # EN PASSANT LEFT
            if piece.position[0] == 4:
                last_move = self.history[-1]
                if piece.position[1] > 1:
                    if isinstance(last_move.piece, Pawn) and \
                            last_move.from_position[1] == piece.position[1] - 1 and \
                            last_move.from_position[0] == 6 and \
                            last_move.to_position[0] == 4:
                        moves.add(Move(piece, [piece.position[0] + 1, piece.position[1] - 1], last_move.piece))

            # EN PASSANT RIGHT
            if piece.position[0] == 4 and piece.colour == 'white' and len(self.history) > 0:
                last_move = self.history[-1]
                if piece.position[1] < 7:
                    if isinstance(last_move.piece, Pawn) and \
                            last_move.from_position[1] == piece.position[1] + 1 and \
                            last_move.from_position[0] == 6 and \
                            last_move.to_position[0] == 4:
                        moves.add(Move(piece, [piece.position[0] + 1, piece.position[1] + 1], last_move.piece))

        # EN PASSANT LEFT
        if piece.position[0] == 3 and piece.colour == 'black' and len(self.history) > 0:
            last_move = self.history[-1]
            if piece.position[1] > 1:
                if isinstance(last_move.piece, Pawn) and \
                        last_move.from_position[1] == piece.position[1] - 1 and \
                        last_move.from_position[0] == 1 and \
                        last_move.to_position[0] == 3:
                    moves.add(Move(piece, [piece.position[0] - 1, piece.position[1] - 1], last_move.piece))

        # EN PASSANT RIGHT
        if piece.position[0] == 3 and piece.colour == 'black' and len(self.history) > 0:
            last_move = self.history[-1]
            if piece.position[1] < 7:
                if isinstance(last_move.piece, Pawn) and \
                        last_move.from_position[1] == piece.position[1] + 1 and \
                        last_move.from_position[0] == 1 and \
                        last_move.to_position[0] == 3:
                    moves.add(Move(piece, [piece.position[0] - 1, piece.position[1] + 1], last_move.piece))

        moves_to_remove: set[Move] = set()

        # IF CHECK AFTER MOVE, DISCARD IT
        for move in moves:
            self.execute_move(move)
            if self.is_check(piece.colour):
                moves_to_remove.add(move)
            self.undo_move()

        moves = set([move for move in moves if move.to_position not in [m.to_position for m in moves_to_remove]])



        return moves
        # If check after move, discard it
            # get all moves
            # play the move
            # if check after move, undo

        # En passant if piece is Pawn
