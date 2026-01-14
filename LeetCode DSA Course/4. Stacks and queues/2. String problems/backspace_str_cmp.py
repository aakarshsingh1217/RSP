def backspace_str_cmp(s: str, t: str) -> bool:
    def build(x):
        stack = []
        
        for c in x:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return stack

    return build(s) == build(t)