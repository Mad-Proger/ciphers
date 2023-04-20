from typing import Callable
from PyQt5 import QtWidgets, uic
from steganography import BMPTools


class BMPDialog(QtWidgets.QWidget):
    def __init__(self, exit_callback: Callable[[QtWidgets.QWidget], None]):
        super().__init__()
        uic.loadUi("gui/layouts/BMPDialog.ui", self)
        self.back_button.clicked.connect(lambda: exit_callback(self))
        self.__setup_buttons()

    def __setup_buttons(self):
        self.read_button.clicked.connect(self.__read)
        self.write_button.clicked.connect(self.__write)

    def __read(self):
        bits = self.__get_bits()
        filepath = self.__get_filepath()
        text = BMPTools.read_text(filepath, bits)
        self.text_field.setPlainText(text)

    def __write(self):
        bits = self.__get_bits()
        filepath = self.__get_filepath()
        text = self.text_field.toPlainText()
        BMPTools.write_text(text, filepath, bits)

    def __get_bits(self) -> int:
        return self.bits_spin_box.value()

    def __get_filepath(self) -> str:
        return self.filepath_field.toPlainText()
