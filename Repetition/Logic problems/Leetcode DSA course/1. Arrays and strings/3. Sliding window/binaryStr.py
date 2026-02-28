def binaryStr(s: str) -> int:
    ans = 0
    left = 0
    numZeros = 0

    for right in range(len(s)):
        if s[right] == "0":
            numZeros += 1

        while numZeros > 1:
            if s[left] == "0":
                numZeros -= 1
            
            left += 1

        ans = max(ans, right - left + 1)

    return ans

print(binaryStr("1101100111"))