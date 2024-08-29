from game.chess.Board import Board
import pygame
from game.chess.Move import Move
from game.chess.pieces.King import King


class Game:
    def __init__(self, board_height: int, board_width: int) -> None:
        self.__history: list[Move] = []
        self.__board: Board = Board(board_height, board_width)
        self.__turn = 'white'

    # GETTERS
    @property
    def board(self) -> Board:
        return self.__board

    @property
    def history(self) -> list[Move]:
        return self.__history

    @property
    def turn(self) -> str:
        return self.__turn

    # FUNCTIONS
    def draw(self, surface: pygame.Surface) -> None:
        self.__board.draw(surface, self.history)

    def change_turn(self) -> None:
        if self.turn == 'white':
            self.__turn = 'black'
        elif self.turn == 'black':
            self.__turn = 'white'

    def handle_piece(self, position: tuple[int, int]) -> None:
        clicked_row = 7 - int(position[1] / 100)
        clicked_col = int(position[0] / 100)

        if self.board.selected_piece is None:
            self.board.selected_piece = self.board.board[clicked_row][clicked_col]

        else:
            moves = [x.to_position for x in self.board.selected_piece.valid_moves(self.board.board, history=self.history)]

            if [clicked_row, clicked_col] in moves and self.board.selected_piece.colour == self.turn:
                # EXECUTE MOVE
                move_to_be_played = [move for move in
                                     self.board.selected_piece.valid_moves(self.board.board, history=self.history)
                                     if move.to_position == [clicked_row, clicked_col]][0]
                if move_to_be_played.captured_piece is not None: # CAPTURED PIECE = NONE, BECAUSE OF EN PASSANT
                    self.board.board[move_to_be_played.captured_piece.position[0]][move_to_be_played.captured_piece.position[1]] = None
                self.board.board[clicked_row][clicked_col] = self.board.selected_piece
                self.board.board[self.board.selected_piece.position[0]][self.board.selected_piece.position[1]] = None
                self.board.selected_piece.position = [clicked_row, clicked_col]
                self.board.selected_piece.moved = True
                self.board.selected_piece = None
                self.__history.append(move_to_be_played)
                self.board.check_for_promotion(history=self.history)
                self.change_turn()

            elif (self.board.selected_piece.position == [clicked_row, clicked_col] or  # CLICKED ON ITSELF
                  self.board.board[clicked_row][clicked_col] is None):  # CLICKED ON EMPTY SQUARE
                self.board.selected_piece = None

            else:  # CLICKED ON ANOTHER PIECE
                self.board.selected_piece = self.board.board[clicked_row][clicked_col]

    def is_check(self, colour: str) -> bool:
        for i in range(8):
            for j in range(8):
                piece = self.board.board[i][j]
                if isinstance(piece, King) and piece.colour == colour and piece.is_check(self.board.board, self.history):
                    return True
        return False
