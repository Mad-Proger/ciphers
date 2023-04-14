from ciphers import Cipher
from typing import Iterable
import itertools
import collections


class CaesarCipher(Cipher.Cipher):
    MOST_COMMON_LETTER = "e"

    def __init__(self, shift: int):
        self.__shift = shift

    def _get_shift_sequence(self) -> Iterable[int]:
        return itertools.repeat(self.__shift)

    @staticmethod
    def get_text_decoder(ciphertext: str):
        counter = collections.Counter(map(str.lower, filter(str.isalpha, ciphertext)))
        most_common_encrypted = counter.most_common(1)[0][0]
        return CaesarCipher(ord(most_common_encrypted) - ord(CaesarCipher.MOST_COMMON_LETTER))
