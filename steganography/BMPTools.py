import imageio.v3 as iio
import numpy as np
from steganography.ByteBuilder import ByteBuilder
from steganography.BitwiseIterator import BitwiseIterator


def write_text(text: str, filepath: str, cnt_bits: int):
    bitmap = iio.imread(filepath)
    shape = bitmap.shape
    bitmap = bitmap.reshape(-1)
    bit_sequence = np.array([*BitwiseIterator(bytes(text, "utf-8"), cnt_bits)], dtype="uint8")
    bit_sequence = np.pad(bit_sequence, ((0, bitmap.shape[0] - bit_sequence.shape[0]),))

    mask = (1 << cnt_bits) - 1
    bitmap = (bitmap & ~mask).astype("uint8") | bit_sequence

    iio.imwrite(filepath, bitmap.reshape(shape))


def read_text(filepath: str, cnt_bits: int) -> str:
    mask = (1 << cnt_bits) - 1
    bitmap = iio.imread(filepath) & mask

    builder = ByteBuilder()
    for x in bitmap.reshape(-1):
        builder.add_bits(x, cnt_bits)

    builder.flush_buffer()
    res = builder.get_bytes()
    res = res[:res.find(0)]
    return res.decode("utf-8")
