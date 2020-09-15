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

# Edge case when s is of length 0 or 1
if len(s) in [0, 1]:
    return True

assert type(s) == str
# Preprocess the string
processed_string = s.replace(' ', '')
 processed_string = processed_string.replace('-', '')
processed_string = processed_string.lower()

# Proprocessing done
assert processed_string.find(' ') == -1
assert processed_string.find('-') == -1
assert processed_string.islower() == True

# Make letters distinct
str_set = ''.join(set(list(processed_string)))

# Check len(set(str)) == len(str)
# Isogram if True, not isogram if False
return len(str_set) == len(processed_string)