from test_framework import generic_test


def reverse_bits(x: int) -> int:
    res = 0

    for i in range(64):
        bit = (x >> i) & 1
        res = res | (bit << (63-i))
    return res 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
