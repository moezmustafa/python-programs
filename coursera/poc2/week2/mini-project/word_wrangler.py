__author__ = 'Rafeh'

"""
word_wrangler.py
Description: Given a word, identify every single possible English
word that could be made out of the word's letters.
"""

"""
Student code for Word Wrangler game
"""

# import urllib2
# import codeskulptor
# import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    return []

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """

    return []

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    list3 = [0 for _ in range(len(list1) + len(list2))]
    idx1, idx2, idx3 = 0, 0, 0
    len1, len2 = len(list1), len(list2)
    while idx1 < len1 and idx2 < len2:  # enough items in both lists?
        if list1[idx1] < list2[idx2]:  # if list1 is smaller
            list3[idx3] = list1[idx1]
            idx1 += 1  # since item from list1 was picked, inc idx1

        else:
            list3[idx3] = list2[idx2]
            idx2 += 1  # since item from list2 was picked, inc idx2
        idx3 += 1  # since we add 1 item into list3 regardless, inc idx3

    # either list1 or list2 is done.

    # copy remaining list1 items if any
    while idx1 < len1:
        list3[idx3] = list1[idx1]
        idx1 += 1
        idx3 += 1

    # copy remaining lst 2 items if any
    while idx2 < len2:
        list3[idx3] = list2[idx2]
        idx2 += 1
        idx3 += 1

    return list3

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    # base case
    if len(list1) <= 1:
        return list1

    # mid section
    mid = len(list1)//2

    # recursive case
    first_half = list1[:mid]
    second_half = list1[mid:]
    return merge(merge_sort(first_half), merge_sort(second_half))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return ['']

    perms = gen_all_strings(word[1:])
    result = []
    for perm in perms:
        for pos in range(len(perm)+1):
            result.append(perm[:pos] + word[0] + perm[pos:])
    return gen_all_strings(word[1:]) + result


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()
