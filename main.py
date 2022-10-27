import sys

from PyQt6.QtWidgets import QApplication

from Model import Model
from Controller import Controller
from View import MainWindow_ver2


def main():
    app = QApplication(sys.argv)

    model = Model()
    controller = Controller(model)
    # view = MainWindow_ver1(model, controller)
    view = MainWindow_ver2(model, controller)
    view.show()

    app.exec()


if __name__ == '__main__':
    main()