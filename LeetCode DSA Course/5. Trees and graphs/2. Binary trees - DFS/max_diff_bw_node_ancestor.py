class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxAncestorDiff(root: TreeNode | None) -> int:
    if not root:
        return 0
    
    def helper(node, cur_max, cur_min):
        # If encounter leaves, ret. max-min along path.
        if not node:
            return cur_max - cur_min
        
        # Else, update max and min and return the max of left
        # and right subtrees.
        cur_max = max(cur_max, node.val)
        cur_min = min(cur_min, node.val)

        left = helper(node.left, cur_max, cur_min)
        right = helper(node.right, cur_max, cur_min)

        return max(left, right)
    
    return helper(root, root.val, root.val)

"""
Unnecessary vars. sol.

def max_diff(root: TreeNode | None) -> int:
    if not root:
        return 0
    
    # Record required max. diff.
    result = 0

    def helper(node: TreeNode | None, cur_max: int, cur_min: int):
        if not node:
            return
        
        # Update 'result'.
        nonlocal result
        result = max(result, 
            abs(cur_max - node.val),
            abs(cur_min - node.val)
        )

        # Update the max and min.
        cur_max = max(cur_max, node.val)
        cur_min = min(cur_min, node.val)

        helper(node.left, cur_max, cur_min)
        helper(node.right, cur_max, cur_min)

    helper(root, root.val, root.val)

    return result
"""