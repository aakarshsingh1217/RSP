def mostPoints(questions: list[list[int]]) -> int:
    def dp(i: int):
        if i >= len(questions):
            return 0
        if i in memo:
            return memo[i]
        
        """
        Next problem we consider is i + however much brain power
        this question costs + 1.
        If we're at second index and solving prob. costs 2
        brain power, then we have to skip problems 3 and 4 and
        next index we're at is 5.
        """
        j = i + questions[i][1] + 1

        memo[i] = max(questions[i][0] + dp(j), dp(i + 1))

        return memo[i]

    memo = {}

    return dp(0)