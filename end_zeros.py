# https://py.checkio.org/en/mission/end-zeros/

def end_zeros(num: int) -> int:
    # your code here
    x = []
    for i in str(num)[::-1]:
        if i == "0":
            x.append(i)
        else:
            break
    return x.count('0')


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
