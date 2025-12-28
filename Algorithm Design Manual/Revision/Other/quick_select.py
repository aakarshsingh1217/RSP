def quickselect(li, k):
    def partition(li, leftLimit, rightLimit):
        # Common  practice is picking random or
        # outermost pos. as pivot candidate.
        pivot = rightLimit

        # Partition scanners ('finder' and 'replacer').
        # They both start from same side, e.g. left.
        finder = replacer = leftLimit

        # Search for pivot continues recursively until
        # it's found and returned to calling func, quickselect().
        while finder < rightLimit:
            if li[finder] < li[pivot]:
                li[finder], li[replacer] = li[replacer], li[finder]
                replacer += 1

            finder += 1

        # 'finder' now equal to right limit
        li[finder], li[replacer] = li[replacer], li[finder]
        pivot = replacer

        # If pivot pos. matches 'k',
        # We've found our kth elem.
        if pivot == k:
            return pivot
        # Otherwise, if kth elem. somewhere in left partition,
        # recursive search turns left...
        elif pivot > k:
            return partition(li, leftLimit, pivot - 1)
        # ... or if kth elem. is somewhere in right partition,
        # recursive search turns right.
        else:
            return partition(li, pivot + 1, rightLimit)
        
    # If k' out of bounds, end alg.
    if k > len(li) or k < 0:
        return

    # Initialize partition limits.
    left = 0
    right = len(li) - 1

    # If list only has one elem., end alg.
    if left == right:
        return left
    
    # Start search over whole list as initial
    # partition.
    return partition(li, left, right)