# https://py.checkio.org/en/mission/backward-each-word/

def backward_string_by_word(text: str) -> str:
    # your code here
    words = text.split(' ')
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
