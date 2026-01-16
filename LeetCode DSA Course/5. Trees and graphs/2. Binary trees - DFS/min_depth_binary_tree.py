# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode | None) -> int:
    def dfs(node: TreeNode | None, ans: int):
        if node is None:
            return float("inf")
        if node.left is None and node.right is None:
            return ans + 1

        left = dfs(node.left, ans + 1)
        right = dfs(node.right, ans + 1)

        return min(left, right)

    if root is None:
        return 0

    return dfs(root, 0)

"""
Cleaner solution.

def minDepth(root: TreeNode | None):
    # Define the depth-first search
    def dfs(root):
        if root is None:
            return 0
        
        # If only one of child is non-null, then go into
        # that recursion.
        if root.left is None:
            return 1 + dfs(root.right)
        elif root.right is None:
            return 1 + dfs(root.left)
        
        # Both children non-null, hence call for both children.
        return 1 + min(dfs(root.left), dfs(root.right))

    return dfs(root)
"""