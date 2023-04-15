from PyQt5 import QtWidgets
from gui import MainMenu


class AppWindow(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciphers")
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setStyleSheet("background-color: rgb(36, 31, 49);")

        main_menu = MainMenu.MainMenu(self)
        self.addWidget(main_menu)
