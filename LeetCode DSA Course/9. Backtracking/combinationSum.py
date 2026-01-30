def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    def backtrack(path: list[int], start: int, currSum: int):
        if currSum == target:
            ans.append(path)

            return
        
        for i in range(start, len(candidates)):
            num = candidates[i]

            if currSum + num <= target:
                path.append(num)
                backtrack(path, i, currSum + num)
                path.pop()

    ans = []
    backtrack([], 0, 0)

    return ans  