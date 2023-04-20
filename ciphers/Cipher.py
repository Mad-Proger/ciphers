import abc
from typing import Callable, Iterable
import itertools


class Cipher(metaclass=abc.ABCMeta):
    ALPHABET_SIZE = 26

    @staticmethod
    def _get_symbol_index(c: str) -> int:
        return ord(c) - (ord('a') if c.islower() else ord('A'))

    @staticmethod
    def _get_symbol_from_index(index: int, is_upper: bool) -> str:
        return chr(index + (ord('A') if is_upper else ord('a')))

    @staticmethod
    def _transform_symbol(c: str, func: Callable[[int], int]) -> str:
        if not c.isalpha():
            return c
        index = Cipher._get_symbol_index(c)
        index = func(index)
        return Cipher._get_symbol_from_index(index, c.isupper())

    @staticmethod
    def _transform_text(text: str, transform_sequence: Iterable[int],
                        transform_func: Callable[[int, int], int]) -> str:
        return "".join(Cipher._transform_symbol(sym, lambda x: transform_func(x, shift))
                       for sym, shift in zip(text, transform_sequence))

    @abc.abstractmethod
    def _get_shift_sequence(self) -> Iterable[int]:
        return itertools.repeat(0)

    def encrypt(self, plaintext: str) -> str:
        return Cipher._transform_text(plaintext, self._get_shift_sequence(),
                                      lambda index, shift: (index + shift) % Cipher.ALPHABET_SIZE)

    def decrypt(self, ciphertext: str) -> str:
        return Cipher._transform_text(ciphertext, self._get_shift_sequence(),
                                      lambda index, shift: (index - shift) % Cipher.ALPHABET_SIZE)
