def isValid(s: str):
    open_paren_stack = []

    for i in range(0, len(s) // 2):
        open_paren_stack.append(s[i])

    for i in range(len(s) // 2, len(s)):
        last_open_paren = open_paren_stack.pop()

        if s[i] == ")" and last_open_paren != "(":
            return False
        elif s[i] == "}" and last_open_paren != "{":
            return False
        elif s[i] == "]" and last_open_paren != "[":
            return False
        
    return True

print(isValid("([])"))
print(isValid("(]"))