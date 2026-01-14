from collections import deque

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    hashmap = {}

    for num in nums2:
        while stack and num > stack[-1]:
            hashmap[stack.pop()] = num

        stack.append(num)

    return[hashmap.get(i, -1) for i in nums1]