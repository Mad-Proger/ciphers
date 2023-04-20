from ciphers import StringKeyCipher
from typing import Iterable
import itertools


class VernamCipher(StringKeyCipher.StringKeyCipher):
    def __init__(self, key: str):
        self.__key_string = ""
        self.set_key(key)

    def get_key(self) -> str:
        return self.__key_string

    def set_key(self, key: str):
        self.__key_string = "".join(filter(str.isalpha, key))

    def _get_shift_sequence(self) -> Iterable[int]:
        return map(VernamCipher._get_symbol_index, self.__key_string)