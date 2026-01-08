def binaryStrFindLen(s: str) -> int:
    left = numZeros = answer = 0

    for right in range(len(s)):
        if (s[right] == "0"):
            numZeros += 1

        while (numZeros > 1):
            if (s[left] == "0"):
                numZeros -= 1

            left += 1

        answer = max(answer, right - left + 1)

    return answer

s = "1101100111"
print(f"Length: {binaryStrFindLen(s)}")