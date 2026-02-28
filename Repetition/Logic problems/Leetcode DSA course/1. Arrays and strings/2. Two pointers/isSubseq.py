class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0

        while t_index < len(t) and s_index < len(s):
            if s[s_index] == t[t_index]:
                s_index += 1

            t_index += 1

        if s_index == len(s):
            return True

        return False