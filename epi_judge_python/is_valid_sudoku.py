from cmath import sqrt
import math
from typing import List



from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    
    def containDuplicates(data) -> bool:
        
        
        return len(data)!=len(set(data))

    n = len(partial_assignment)
    if any(
        containDuplicates([partial_assignment[i][j] for j in range(n)]) or containDuplicates([partial_assignment[j][i] for j in range(n)]) for i in range(n)):
        return False 
    
    region_size = int(math.sqrt(n))
    return all(not containDuplicates([partial_assignment[a][b] for a in range(I * region_size, region_size *(I + 1)) for b in range(J * region_size, region_size*(J+1))]) for I in range(region_size) for J in range(region_size))

    
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))

