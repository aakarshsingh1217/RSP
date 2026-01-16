class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(root: TreeNode | None, p: TreeNode | None, q: TreeNode | None) -> TreeNode | None:
    if not root:
        return None
    
    if root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    
    if left:
        return left
    
    return right