# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode | None) -> bool:
    def dfs(node: TreeNode | None, small, large):
        if not node:
            return True

        if not (small < node.val < large):
            return False
        
        left = dfs(node.left, small, node.val)
        right = dfs(node.right, node.val, large)

        # Tree is a BST if left and right subtrees also BSTs.
        return left and right
    
    return dfs(root, float("-inf"), float("inf"))