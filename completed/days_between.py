# https://py.checkio.org/en/mission/days-diff/
# complete

import datetime as dt

def days_diff(a, b):
    # your code here
    date_a = dt.date(a[0], a[1], a[2])
    date_b = dt.date(b[0], b[1], b[2])
    return abs((date_a - date_b).days)


if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")

# Research
# https://www.geeksforgeeks.org/python-program-to-find-number-of-days-between-two-given-dates/