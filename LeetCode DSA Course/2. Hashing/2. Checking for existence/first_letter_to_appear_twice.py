def repeatedCharacter(s: str) -> str:
    set_of_chars = set()

    for letter in s:
        if letter in set_of_chars:
            return letter
        
        set_of_chars.add(letter)

    # Return a space if no repeated char. found
    return " "

test_str = "hello"
print(repeatedCharacter(test_str))