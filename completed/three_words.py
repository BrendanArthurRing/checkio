# https://py.checkio.org/en/mission/three-words/

def checkio(words: str) -> bool:
    possible_words = words.split(" ")
    succession = 0


    for i in possible_words:
        if succession < 3:
            if i.isalpha():
                succession += 1
            else:
                succession = 0
    
    if succession >= 3:
        return True
    else:
        return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession. 
"""