def makeGood(s: str) -> str:
    stack = []

    for char in s:
        if stack:
            if char.islower() and stack[-1].isupper() and char == stack[-1].lower():
                stack.pop()
            elif char.isupper() and stack[-1].islower() and char == stack[-1].upper():
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    return "".join(stack)

print(makeGood("s"))