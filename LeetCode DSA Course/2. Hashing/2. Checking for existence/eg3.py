def find_nums(nums: list[int]) -> list[int]:
    all_nums = set(nums)

    valid_nums = []

    for num in all_nums:
        if num + 1 not in all_nums and num - 1 not in all_nums:
            valid_nums.append(num)

    return valid_nums

nums = [1, -3, -4, 5, 6, 7, 9, 11]

valid_nums = find_nums(nums)

for num in valid_nums:
    print(num)