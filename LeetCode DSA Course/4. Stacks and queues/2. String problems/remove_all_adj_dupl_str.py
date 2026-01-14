def remove_adj_dupl_str(s: str) -> str:
    stack = []
    last_char = None

    for i in range(len(s)):
        if stack:
            last_char = stack.pop()

        if last_char != s[i]:
            if last_char is not None:
                stack.append(last_char)
            
            stack.append(s[i])

        if not stack:
            last_char = None

    return "".join(stack)

print(remove_adj_dupl_str("abbaca"))

"""
Better sol.:

def remove_dupl(s: str) -> str:
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)
"""