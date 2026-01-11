from collections import defaultdict

def lenOflongestSubstr(s: str) -> int:
    n = len(s)
    ans = 0

    # charToNextIndex stores index after curr. char.
    charToNextIndex = {}
    i = 0

    # try to extend range [i, j]
    for j in range(n):
        if s[j] in charToNextIndex:
            i = max(charToNextIndex[s[j]], i)
        
        ans = max(ans, j - i + 1)
        charToNextIndex[s[j]] = j + 1
    
    return ans

"""
First sol.

from collections import defaultdict

def lenOflongestSubstr(s: str) -> int:
    chars = defaultdict(int)
    left = right = res = 0

    while right < len(s):
        curr_right = s[right]
        chars[curr_right] += 1

        while chars[curr_right] > 1:
            curr_left = s[left]
            chars[curr_left] -= 1
            left += 1

        res = max(res, right - left + 1)
        right += 1

    return res
"""