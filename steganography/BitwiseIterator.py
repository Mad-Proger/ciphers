class BitwiseIterator:
    BITS_PER_BYTE = 8

    def __init__(self, s: bytes, bit_count: int = 1):
        self.__s = s + b"\0"
        self.__bit_cnt = bit_count
        self.__byte_index = 0
        self.__byte_offset = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.__byte_index == len(self.__s):
            raise StopIteration

        res = 0
        res_length = 0
        while res_length < self.__bit_cnt and self.__byte_index < len(self.__s):
            cur_length = min(self.__bit_cnt - res_length, BitwiseIterator.BITS_PER_BYTE - self.__byte_offset)
            cur_bits = self.__get_bits(cur_length)
            res = (res << cur_length) | cur_bits
            res_length += cur_length

        if res_length < self.__bit_cnt:
            res <<= self.__bit_cnt - res_length
        return res

    def __get_bits(self, cnt: int) -> int:
        mask = (1 << cnt) - 1
        shift = BitwiseIterator.BITS_PER_BYTE - (self.__byte_offset + cnt)
        ans = (self.__s[self.__byte_index] & (mask << shift)) >> shift

        self.__byte_offset += cnt
        if self.__byte_offset == BitwiseIterator.BITS_PER_BYTE:
            self.__byte_index += 1
            self.__byte_offset = 0
        return ans

