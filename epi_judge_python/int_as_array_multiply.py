from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:

    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    returnNums = [0]*(len(num1)+len(num2))
    num1[0], num2[0] = abs(num1[0]),abs(num2[0])
    for n1 in reversed(range(len(num1))):
        for n2 in reversed(range(len(num2))):
            returnNums[n1+n2 + 1] += num1[n1]*num2[n2]
            returnNums[n1+n2] += returnNums[n1+n2+1]//10
            returnNums[n1+n2+1] %= 10
    

    returnNums = returnNums[next((i for i,x in enumerate(returnNums) if x != 0),len(returnNums)):] or [0]
    returnNums = [sign*returnNums[0]] + returnNums[1:]

    return returnNums



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
                                       

