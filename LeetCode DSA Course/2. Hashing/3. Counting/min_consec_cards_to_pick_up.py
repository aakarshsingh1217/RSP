from collections import defaultdict

def min_consec_cards_pick_up(cards: list[int]):
    dic = defaultdict(list)
    ans = float("inf")

    for i in range(len(cards)):
        if cards[i] in dic:
            ans = min(ans, i - dic[cards[i]] + 1)

        dic[cards[i]] = i

    return ans if ans < float("inf") else -1

"""
first sol

from collections import defaultdict

def min_consec_cards_pick_up(cards: list[int]):
    dic = defaultdict(list)

    for i in range(len(cards)):
        dic[cards[i]].append(i)

    ans = float("inf")
    
    for key in dic:
        arr = dic[key]

        for i in range(len(arr) - 1):
            ans = min(ans, arr[i + 1] - arr[i] + 1)

    return ans if ans < float("inf") else -1
"""