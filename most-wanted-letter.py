#  https://github.com/Bryukh-Checkio-Tasks/checkio-task-most-wanted-letter.git { 36 }

import collections
import operator


def checkio(text: str) -> str:
    letter_count =  dict(collections.Counter(text.lower()))
    sorted_letter_count = sorted(letter_count.items())
    most_frequent_letter = max(sorted_letter_count, key=operator.itemgetter(1))[0]
    return most_frequent_letter

checkio("Hello World")
checkio("One")

test = True
if __name__ == '__main__' and test == True:
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
# https://stackoverflow.com/questions/4131123/finding-the-most-frequent-character-in-a-string
# Ok this most common thing is built into Counter

# https://docs.python.org/3/library/collections.html#counter-objects
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary