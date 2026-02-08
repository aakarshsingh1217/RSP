def can_concat(s: str, words: list[str]):
    def dp(i: int):
        if i in memo:
            return memo[i]
        if i == len(s):
            return True
        
        for word in words:
            if s.startswith(word, i):
                if dp(i + len(word)):
                    memo[i] = True

                    return True
        
        memo[i] = False

        return memo[i]

    memo = {}

    return dp(0)