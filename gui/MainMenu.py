from typing import Callable
from PyQt5 import QtWidgets, uic
from gui import CaesarCipherDialog, StringCipherDialog, BMPDialog
from ciphers import CaesarCipher, VernamCipher, VigenereCipher


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self, sw: QtWidgets.QStackedWidget):
        super().__init__()
        uic.loadUi("gui/layouts/MainMenu.ui", self)
        self.__sw = sw
        self.__setup_buttons()

    def __setup_buttons(self):
        self.caesar_button.clicked.connect(self.__caesar)
        self.vigenere_button.clicked.connect(self.__vigenere)
        self.vernam_button.clicked.connect(self.__vernam)
        self.bmp_button.clicked.connect(self.__bmp)

    def __caesar(self):
        cipher = CaesarCipher.CaesarCipher()
        cipher_widget = CaesarCipherDialog.CaesarCipherDialog(cipher, self.__get_callback())
        self.__switch_widget(cipher_widget)

    def __vigenere(self):
        cipher = VigenereCipher.VigenereCipher("")
        cipher_widget = StringCipherDialog.StringCipherDialog(cipher, self.__get_callback(),
                                                              "Vigenere cipher")
        self.__switch_widget(cipher_widget)

    def __vernam(self):
        cipher = VernamCipher.VernamCipher("")
        cipher_widget = StringCipherDialog.StringCipherDialog(cipher, self.__get_callback(),
                                                              "Vernam cipher")
        self.__switch_widget(cipher_widget)

    def __bmp(self):
        bmp_widget = BMPDialog.BMPDialog(self.__get_callback())
        self.__switch_widget(bmp_widget)

    def __get_callback(self) -> Callable[[QtWidgets.QWidget], None]:
        def callback(widget: QtWidgets.QWidget):
            self.__sw.removeWidget(widget)
            self.__sw.setCurrentWidget(self)
        return callback

    def __switch_widget(self, widget: QtWidgets.QWidget):
        self.__sw.addWidget(widget)
        self.__sw.setCurrentWidget(widget)
