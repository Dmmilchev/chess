from game.chess.Board import Board
import pygame


class Game:
    def __init__(self, board_height: int, board_width: int) -> None:
        self.__board: Board = Board(board_height, board_width)
        self.__turn = 'white'

    # GETTERS
    @property
    def board(self) -> Board:
        return self.__board

    @property
    def turn(self) -> str:
        return self.__turn

    # FUNCTIONS
    def draw(self, surface: pygame.Surface) -> None:
        self.__board.draw(surface)

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
            moves = [x.to_position for x in self.board.valid_moves(self.board.selected_piece)]

            if [clicked_row, clicked_col] in moves and self.board.selected_piece.colour == self.turn:
                # EXECUTE MOVE
                move_to_be_played = [move for move in
                                     self.board.valid_moves(self.board.selected_piece)
                                     if move.to_position == [clicked_row, clicked_col]][0]
                self.board.execute_move(move_to_be_played)
                self.board.selected_piece = None
                self.change_turn()

            elif (self.board.selected_piece.position == [clicked_row, clicked_col] or  # CLICKED ON ITSELF
                  self.board.board[clicked_row][clicked_col] is None):  # CLICKED ON EMPTY SQUARE
                self.board.selected_piece = None

            else:  # CLICKED ON ANOTHER PIECE
                self.board.selected_piece = self.board.board[clicked_row][clicked_col]

    def undo_move(self) -> None:
        self.board.undo_move()
        self.change_turn()

    def is_game_over(self) -> bool:
        return (self.board.is_checkmate('white') or
                self.board.is_stalemate('white') or
                self.board.is_checkmate('black') or
                self.board.is_stalemate('black'))

    def get_winner(self) -> str:
        if self.board.is_stalemate('white') or self.board.is_stalemate('black'):
            return 'draw'
        elif self.board.is_checkmate('white'):
            return 'black'
        elif self.board.is_checkmate('black'):
            return 'white'
