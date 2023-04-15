from gui import AppWindow
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication([])
    window = AppWindow.AppWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
