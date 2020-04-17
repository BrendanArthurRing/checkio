# https://py.checkio.org/en/mission/restricted-sum/
# https://github.com/Bryukh-Checkio-Tasks/checkio-task-forbidden-sum.git { 11 }

def checkio(data):
    result = 0
    i = 0
    result += data[i]
    return result



if __name__ == '__main__':
    # These asserts are for testing
    assert checkio([1, 2, 3]) == 6



"""
The list of banned words are as follows:

    sum
    import
    for
    while
    reduce



"""