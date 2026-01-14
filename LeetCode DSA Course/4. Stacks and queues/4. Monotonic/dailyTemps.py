def dailyTemps(temps: list[int]) -> list[int]:
    stack = []
    answer = [0] * len(temps)

    for i in range(len(temps)):
        while stack and temps[stack[-1]] < temps[i]:
            j = stack.pop()
            answer[j] = i - j

        stack.append(i)

    return answer