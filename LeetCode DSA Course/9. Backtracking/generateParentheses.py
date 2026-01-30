def genParentheses(n: int) -> list[str]:
    answer = []

    def backtracking(currStr: list[str], leftCount: int, rightCount: int):
        if len(currStr) == 2 * n:
            answer.append("".join(currStr))

            return

        if leftCount < n:
            currStr.append("(")
            backtracking(currStr, leftCount + 1, rightCount)
            currStr.pop()

        if rightCount < leftCount:
            currStr.append(")")
            backtracking(currStr, leftCount, rightCount + 1)
            currStr.pop()

    backtracking([], 0, 0)

    return answer