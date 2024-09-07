from GUI import GUI
from GUI import constants
from client.Client import Client


def main() -> None:
    client = Client()
    gui = GUI.GUI(constants.WIDTH, constants.HEIGHT, client)
    gui.while_loop()


if __name__ == '__main__':
    main()
