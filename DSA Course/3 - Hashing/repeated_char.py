class Solution:
    def repeated_char(self, s: str) -> str:
        seen = set()

        for c in s:
            if c in seen:
                return c
            
            seen.add(c)

        return " "