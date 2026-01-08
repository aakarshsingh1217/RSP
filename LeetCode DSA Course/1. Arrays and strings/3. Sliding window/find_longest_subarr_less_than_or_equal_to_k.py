def find_length(nums: list[int], k: int) -> int:
    curr = 0
    left = 0
    answer = 0

    for right in range(len(nums)):
        curr += nums[right]

        while (curr > k):
            curr -= nums[left]
            left += 1

        answer = max(answer, right - left + 1)

    return answer

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

print(f"Length: {find_length(nums, k)}")