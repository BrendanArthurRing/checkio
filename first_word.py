# https://py.checkio.org/en/mission/first-word/

import string

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    text = text.replace(".", " ")
    words = text.split(" ")
    punctuation = string.punctuation
    punctuation = punctuation.replace("'", "")
    mapping_table = str.maketrans("", "", punctuation)
    stripped_words = [word.translate(mapping_table) for word in words]
    print(stripped_words)
    for i in stripped_words:
        if i:
            return i

# Research
# https://machinelearningmastery.com/clean-text-machine-learning-python/


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
