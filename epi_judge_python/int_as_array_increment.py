from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1

    for num in reversed(range(1,len(A))):
        if A[num] != 10:
            return A
        A[num - 1] += 1
        A[num] = 0
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
