from ciphers import Cipher
from typing import Iterable
import itertools


class VernamCipher(Cipher.Cipher):
    def __init__(self, key: str):
        self.__key_string = "".join(filter(str.isalpha, key))

    def _get_shift_sequence(self) -> Iterable[int]:
        return map(VernamCipher._get_symbol_index, self.__key_string)