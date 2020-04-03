# https://py.checkio.org/en/mission/split-list/

import math

def split_list(items: list) -> list:
    split_point = math.ceil(len(items) / 2)
    result = [items[:split_point], items[split_point:]]
    # your code here
    print(result)
    return result

# Split list
# if even len return split of equal lens
# if odd len return first list more len
# if empty return two empty lists
# the round() function uses bankers rounding
# it rounds .5 to the nearest even number
# Ceil always rounds up
# items[:math.ceil((len(items) / 2))] 

if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
