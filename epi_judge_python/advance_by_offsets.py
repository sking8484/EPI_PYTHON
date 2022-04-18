from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    maxTraveledSoFar, maxIndex = 0, len(A) - 1
    
    for i in range(len(A)):
        
        if i <= maxTraveledSoFar and maxTraveledSoFar < len(A):
            maxTraveledSoFar = max(maxTraveledSoFar,A[i] + i)
    return maxTraveledSoFar>= maxIndex


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
