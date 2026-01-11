from collections import defaultdict

def check_equal_num_occurences(s: str) -> bool:
    char_count = defaultdict(int)
    last_char_count = 0

    for char in s:
        char_count[char] += 1
        last_char_count = char_count[char]

    for key in char_count:
        if char_count[key] != last_char_count:
            return False
        
    return True

print(check_equal_num_occurences("abacbc"))
print(check_equal_num_occurences("aaabb"))

"""
Better sol:

from collections import defaultdict

def areOccurencesEqual(s: str) -> bool:
    counts = defaultdict(int)

    for char in s:
        counts[char] += 1

    # .values() returns dict_values view object
    # that provides dynamic, iterable view of
    # of all vals. in dict., updating automatically
    # when dict. modified.
    # E.g. for s = "abacbc", 
    # counts = {
    #   'a': 2,
    #   'b': 2,
    #   'c': 2
    # }
    # frequencies = dict_values([2, 2, 2])
    # .values() is O(1) as it doesn't copy
    # vals., returns view obj. of internal
    # storage which requires no iteration
    # and no alloc. proportional to dict.
    # size, therefore O(1) time and space.
    frequencies = counts.values()

    return len(set(frequencies)) == 1
"""