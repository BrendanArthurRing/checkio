# https://py.checkio.org/en/mission/acceptable-password-ii/

# Taken from mission Acceptable Password I

# https://py.checkio.org/en/mission/acceptable-password-i/

def is_acceptable_password(password: str) -> bool:
    return True if len(password) > 6 else False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""
 You are the beginning of a password series. Every mission will be based on the previous one. Going forward the missions will become slightly more complex.

In this mission you need to create a password verification function.

Those are the verification conditions:
the length should be bigger than 6.

Input: A string.

Output: A bool. 
"""

def is_acceptable_password(password: str) -> bool:
    more_than_six_characters = len(password) > 6
    contains_number = any(i.isdigit() for i in password)
    return all([more_than_six_characters, contains_number])


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""
 In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit.

Input: A string.

Output: A bool. 
"""