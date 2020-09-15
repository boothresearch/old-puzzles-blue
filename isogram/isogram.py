def is_isogram(string):
    pass
"""
Program to determine whether a word or phrase is an isogram.
An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, 
however spaces and hyphens are allowed to appear multiple times.

Examples of isograms include:

    lumberjacks
    background
    downstream
    six-year-old

The word *isograms*, however, is not an isogram, because the s repeats.
"""

def is_isogram(string):
    word = string.lower()

    if word == "":
        return True
    elif word == " ":
        return False
    else:
        for char in word:
            if word and char not in ' -' and word.count(char) > 1:
                return False
        return True