import abc
from ciphers import Cipher


class StringKeyCipher(Cipher.Cipher, abc.ABC):
    @abc.abstractmethod
    def set_key(self, key: str):
        pass

    @abc.abstractmethod
    def get_key(self) -> str:
        return ""
