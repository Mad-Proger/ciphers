from ciphers import VernamCipher
from typing import Iterable
import itertools


class VigenereCipher(VernamCipher.VernamCipher):
    def __init__(self, key: str):
        super().__init__(key)

    def _get_shift_sequence(self) -> Iterable[int]:
        return itertools.cycle(super()._get_shift_sequence())
