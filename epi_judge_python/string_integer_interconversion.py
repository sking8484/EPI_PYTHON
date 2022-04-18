from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    isNeg = False
    if x < 0:
        x, isNeg = -x, True 

    s = []
    while True:
        s.append(chr(ord('0') + x%10))
        x //= 10
        if x == 0:
            break 
    return ('-' if isNeg else '') + ''.join(reversed(s))


def string_to_int(s: str) -> int:
    resultInt = 0
    print(s)
    for dig in s[s[0]=='-' or s[0]=='+':]:
        resultInt = resultInt*10 + int(dig)
    return resultInt*(-1 if s[0]=="-" else 1)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
