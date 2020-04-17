def checkio(data: str) -> bool:

    conditions = []

    # 10 or more characters
    if len(data) >= 10:
        conditions.append(True)
    else:
        conditions.append(False)

    # Contains digit
    if any(char.isdigit() for char in data):
        conditions.append(True)
    else:
        conditions.append(False)

    # Contains Upper
    if any(char.isupper() for char in data):
        conditions.append(True)
    else:
        conditions.append(False)

    # Contains Lower
    if any(char.islower() for char in data):
        conditions.append(True)
    else:
        conditions.append(False)

    if all(conditions):
        return True
    else:
        return False

# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('DHJK87DSKJHWW68D') == False, "7th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
