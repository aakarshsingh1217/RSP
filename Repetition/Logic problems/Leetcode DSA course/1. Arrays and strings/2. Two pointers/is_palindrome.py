"""
Given a string s, return true if it's a palindrome
and false if otherwise. A string is a palindrome if
it reads the same forward as backward, that means
after reversing it, it's still the same string.

Input: "racecar" , Output: True (reads the same way
backwards and forwards).

Input values: can be uppercase or lowercase ASCII
chars.

Input size: 1 <= s.length <= 2 * 10^5.
"""

def is_palindrome(s: str) -> bool:
    """
    ptr_1 = start
    ptr_2 = end

    while ptr_1 < ptr_2:
        if s[ptr_1] != s[ptr_2]:
            return False

    return True

    Complexity analysis: O(N) time complexity,
    iterate through each value in the string
    exactly once.

    O(1) space, as we only use primitive vars.
    """

    ptr_1 = 0
    ptr_2 = len(s) - 1

    while ptr_1 < ptr_2:
        if s[ptr_1] != s[ptr_2]:
            return False
        
        ptr_1 += 1
        ptr_2 -= 1
        
    return True

"""
Input: "racecar" , Output: True (reads the same way
backwards and forwards).

ptr_1 = 0
ptr_2 = 6

while ptr_1 < ptr_2:
    if s[ptr_1] != s[ptr_2] never returns True:
        skip

    ptr_1 increments to 3 and ptr_2 decrements to 3, while
    condition breaks

return True
"""

def main():
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))

main()