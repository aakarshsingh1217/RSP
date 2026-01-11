from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groupedStrs = defaultdict(list)

    for string in strs:
        sortedStr = "".join(sorted(string))
        groupedStrs[sortedStr].append(string)

    ans = []

    for key in groupedStrs:
        ans.append(groupedStrs[key])

    return ans

strs = ["eat","tea","tan","ate","nat","bat"]
ans = group_anagrams(strs)

print(ans)

"""
Better sol.:

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)

    return list(groups.values())
"""