from typing import Callable
from PyQt5 import QtWidgets, uic
from ciphers import StringKeyCipher


class StringCipherDialog(QtWidgets.QWidget):
    def __init__(self, cipher: StringKeyCipher.StringKeyCipher,
                 exit_callback: Callable[[QtWidgets.QWidget], None], cipher_name: str):
        super().__init__()
        uic.loadUi("gui/layouts/StringCipherDialog.ui", self)
        self.__cipher = cipher
        self.__setup_buttons()
        self.back_button.clicked.connect(lambda: exit_callback(self))
        self.cipher_label.setText(cipher_name)

    def __setup_buttons(self):
        self.encrypt_button.clicked.connect(self.__encrypt)
        self.decrypt_button.clicked.connect(self.__decrypt)

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
        key = self.key_field.toPlainText()
        self.__cipher.set_key(key)
