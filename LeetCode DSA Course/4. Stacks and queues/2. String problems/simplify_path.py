def simplifyPath(path: str) -> str:
    # Initialize a stack.
    stack = []

    # Split input str. on "/" as the delim.
    # and process each portion one by one.
    for portion in path.split("/"):
        # If curr. component is a "..", then
        # we pop an entry from stack if it's non-empty.
        if portion == "..":
            if stack:
                stack.pop()
        elif portion == "." or not portion:
            # No-op. for a "." or empty str.
            continue
        else:
            # Legitimate dir. name, so add to
            # stack.
            stack.append(portion)

    # Stitch together all dir. names togeth:
    final_str = "/" + "/".join(stack)

    return final_str