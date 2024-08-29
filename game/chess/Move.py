from game.chess.pieces.Piece import Piece
from typing import Union


class Move:
    def __init__(self, piece: Piece, to_position: list[int], captured_piece: Union[Piece, None]) -> None:
        self.__piece: Piece = piece
        self.__from_position: list[int] = piece.position
        if len(to_position) == 2 and 0 <= to_position[0] <= 7 and 0 <= to_position[1] <= 7:
            self.__to_position: list[int] = to_position
        else:
            raise ValueError('To position must have length 2 and it\'s values must be between 0 and 7')
        if captured_piece is not None:
            self.__captured_piece_position = captured_piece.position
        self.__captured_piece = captured_piece

    @property
    def piece(self) -> Piece:
        return self.__piece

    @property
    def to_position(self) -> list[int]:
        return self.__to_position

    @property
    def from_position(self) -> list[int]:
        return self.__from_position

    @property
    def captured_piece(self) -> Union[Piece, None]:
        return self.__captured_piece

    @property
    def captured_piece_position(self) -> list[int]:
        return self.__captured_piece_position

    def __eq__(self, other: 'Move') -> bool:
        if isinstance(other, Move):
            return (self.piece == other.piece and
                    self.from_position == other.from_position and
                    self.to_position == other.to_position and
                    self.captured_piece == other.captured_piece)
        return False

    def __hash__(self):
        return hash((self.piece, self.from_position[0], self.__from_position[1],
                     self.to_position[0], self.to_position[1], self.captured_piece))
