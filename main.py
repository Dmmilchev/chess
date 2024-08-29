from GUI import chessGUI
from GUI import constants


def main() -> None:
    gui = chessGUI.ChessGUI(constants.WIDTH, constants.HEIGHT)
    gui.while_loop()


if __name__ == '__main__':
    main()
