# https://py.checkio.org/en/mission/sort-array-by-element-frequency/

from collections import Counter

def frequency_sort(items):
    return [item for items, c in Counter(items).most_common() for item in [items] * c]
    # I dont understand how this works, but it works.
    # I know about list comprehensions, but not sure why there is a "'"
    # and no idea how [items] * c actually works.
    # I found this code here:
    # https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/
    # It would be nice if they actually explained how it works.
    # Bummed that I couldn't figure this out all on my own.
    # the "If two elements have the same frequency, they should end up in 
    # the same order as the first appearance in the iterable." part
    # really stumped me.

# (values) = [ (exression) for (value) in (collection) ] 


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

"""
 Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable

Output: Iterable 
"""