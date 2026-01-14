def isValid(s: str) -> bool:
    stack = []
    matching = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        # if char is an opening bracket.
        if char in matching:
            stack.append(char)
        else:
            if not stack:
                return False
            
            previous_opening = stack.pop()

            if matching[previous_opening] != char:
                return False
            
    return not stack