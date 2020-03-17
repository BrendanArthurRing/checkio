# https://py.checkio.org/en/mission/digits-multiplication/
# https://github.com/Bryukh-Checkio-Tasks/checkio-task-digits-multiplication { 37 }

import numpy

def checkio(number: int) -> int:
    numbers = [int(i) for i in str(number) if i != "0"]
    return numpy.product(numbers)


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


'''
 You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

Precondition: 0 < number < 106 

'''