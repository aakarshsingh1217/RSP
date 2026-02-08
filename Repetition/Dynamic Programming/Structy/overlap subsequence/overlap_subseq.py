def overlap_subseq(str1: str, str2: str):
    def dp(front1: int, front2: int):
        if (front1, front2) in memo:
            return memo[(front1, front2)]
        if front1 == len(str1) or front2 == len(str2):
            return 0
        
        if str1[front1] == str2[front2]:
            memo[(front1, front2)] = 1 + dp(front1 + 1, front2 + 1)
        else:
            memo[(front1, front2)] = max(
                dp(front1 + 1, front2),
                dp(front1, front2 + 1)
            )

        return memo[(front1, front2)]

    memo = {}

    return dp(0, 0)