#  https://github.com/Bryukh-Checkio-Tasks/checkio-task-most-wanted-letter.git { 36 }

from collections import Counter

def checkio(text: str) -> str:
    wc = Counter(text.lower())
    s = max(wc.values())
    print(wc, s)

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

# Research
# https://www.geeksforgeeks.org/python-program-to-find-the-most-occurring-character-and-its-count/