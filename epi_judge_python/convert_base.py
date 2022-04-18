from test_framework import generic_test
import string 

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    
    def constructNumFromInt(num_as_int:int, base:int):
        return ('' if num_as_int == 0 else constructNumFromInt(num_as_int // base, base) + string.hexdigits[num_as_int%base].upper())
    
    num_as_int = 0
    for num in num_as_string[num_as_string[0] == "-" or num_as_string == '+':]:
        num_as_int = num_as_int*b1 + string.hexdigits.index(num.lower())
    
    return ("-" if num_as_string[0] == "-" else "") + ("0" if num_as_int == 0 else constructNumFromInt(num_as_int,b2))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
