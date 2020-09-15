# Anagram
#An anagram is a rearrangement of letters to form a new word.
#Given a word and a list of candidates, select the sublist of anagrams of the given word and
# the program should return a list containing the anagrams

def sort_letters(word):
    """
    Convert word to list and order its charaters

    Arguments:
        word {string} -- Any word

    Returns:
        [list] -- A list of characters
    """
    sorted_letters = [c for c in word]
    sorted_letters.sort()
    return sorted_letters


def find_anagrams(word, candidates):
    """
    Given a word and a list of possible anagrams, select the correct sublist.

    Arguments:
        word {string} -- Any word
        candidates {list} -- List of words

    Returns:
        [list] -- List of anagrams
    """
    word_cap = word.upper()
    sorted_word = sort_letters(word_cap)

    candidates_cap = [candidate.upper() for candidate in candidates]
    anagrams = []
    for idx, candidate in enumerate(candidates_cap):
        if sorted_word == sort_letters(candidate) and word_cap != candidate:
            anagrams.append(candidates[idx])

    return anagrams

