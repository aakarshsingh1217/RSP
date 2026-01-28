def max69Number(num: int) -> int:
    # Since we start with lowest digit, init. curr_digit = 0
    curr_digit = 0
    index_first_six = -1
    num_copy = num

    # Check every digit of num_copy from low to high
    while num_copy:
        # If curr. digit 6, record it as highest digit of 6.
        if num_copy % 10 == 6:
            index_first_six = curr_digit

        # Move onto next digit.
        num_copy //= 10
        curr_digit += 1

    return num if index_first_six == -1 else num + 3 * 10 ** index_first_six