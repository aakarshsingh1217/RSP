def max_palin_subseq(string: str):
    def dp(curr_front: int, curr_back: int):
        if (curr_front, curr_back) in memo:
            return memo[(curr_front, curr_back)]
        if curr_front == curr_back:
            return 1
        if curr_front > curr_back:
            return 0
        
        # Add 2 to ans. as need to count 2 chars. just matched
        if (string[curr_front] == string[curr_back]):
            memo[(curr_front, curr_back)] = 2 + dp(string, curr_front + 1, curr_back - 1)
        else:
            memo[(curr_front, curr_back)] =  max(
                dp(string, curr_front + 1, curr_back),
                dp(string, curr_front, curr_back - 1)
            )

        return memo[(curr_front, curr_back)]
        
    memo = {}

    return dp(0, len(string) - 1)