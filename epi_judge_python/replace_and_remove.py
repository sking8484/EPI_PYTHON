import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


'''Pass 1: If its a b then overwrite the last b with this letter. If its an a then update a count. Thats first pass. 
Pass 2: Since write index will be one greater than what it should be, set curr index to write index -1, set the write index to write index + a -1
    total cound is write index + 1 now. 

    first write index shows how many non bs we have. Second write index, gives us how many non bs as well as double as. 
    Curr index is going to be the last element in length, and write_idx is now where we write to with larger as. 
'''

def replace_and_remove(size: int, s: List[str]) -> int:
    write_idx, a_count = 0,0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
    
    curr_idx = write_idx - 1
    write_idx += a_count -1
    total_count = write_idx + 1

    while curr_idx >= 0:
        if s[curr_idx] == 'a':
            s[write_idx -1:write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        curr_idx -= 1
            

    return total_count


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
