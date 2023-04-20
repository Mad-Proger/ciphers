class ByteBuilder:
    BITS_PER_BYTE = 8

    def __init__(self):
        self.__seq = []
        self.__last_byte = 0
        self.__last_length = 0

    def add_bits(self, bits: int, cnt: int):
        self.__last_byte = (self.__last_byte << cnt) | bits
        self.__last_length += cnt
        self.__push_to_sequence()

    def __push_to_sequence(self):
        mask = (1 << ByteBuilder.BITS_PER_BYTE) - 1
        while self.__last_length >= ByteBuilder.BITS_PER_BYTE:
            shift = self.__last_length - ByteBuilder.BITS_PER_BYTE
            bits = (self.__last_byte & (mask << shift)) >> shift
            self.__last_length -= ByteBuilder.BITS_PER_BYTE
            self.__seq.append(bits)

        self.__last_byte &= mask

    def get_bytes(self) -> bytes:
        return bytes(self.__seq)

    def flush_buffer(self):
        self.__last_byte <<= ByteBuilder.BITS_PER_BYTE - self.__last_length
        self.__last_length = 0
        self.__seq.append(self.__last_byte)
        self.__last_byte = 0
