from GUI.managerGUI import ManagerGUI
from GUI import constants
from client.Client import Client


def main() -> None:
    client = Client()
    gui = ManagerGUI(constants.WIDTH, constants.HEIGHT, client)
    gui.start()


if __name__ == '__main__':
    main()
