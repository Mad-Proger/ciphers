from typing import Callable
from PyQt5 import QtWidgets, uic
from ciphers import CaesarCipher


class CaesarCipherDialog(QtWidgets.QWidget):
    def __init__(self, cipher: CaesarCipher.CaesarCipher, exit_callback: Callable[[], None]):
        super().__init__()
        uic.loadUi("gui/layouts/CaesarCipherDialog.ui", self)
        self.__cipher = cipher
        self.__setup_buttons()
        self.back_button.clicked.connect(exit_callback)

    def __setup_buttons(self):
        self.encrypt_button.clicked.connect(self.__encrypt)
        self.decrypt_button.clicked.connect(self.__decrypt)
        self.crack_button.clicked.connect(self.__crack)

    def __encrypt(self):
        plaintext = self.plaintext_field.toPlainText()
        self.__update_key()
        ciphertext = self.__cipher.encrypt(plaintext)
        self.ciphertext_field.setPlainText(ciphertext)

    def __decrypt(self):
        ciphertext = self.ciphertext_field.toPlainText()
        self.__update_key()
        plaintext = self.__cipher.decrypt(ciphertext)
        self.plaintext_field.setPlainText(plaintext)

    def __update_key(self):
        shift = self.shift_spin_box.value()
        self.__cipher.set_key(shift)

    def __crack(self):
        ciphertext = self.ciphertext_field.toPlainText()
        self.__cipher = CaesarCipher.CaesarCipher.get_text_decoder(ciphertext)
        self.shift_spin_box.setValue(self.__cipher.get_key())

