class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode | None, q: TreeNode | None):
    if p == None or q == None:
        return True
    
    if p == None or q == None:
        return False
    
    if p.val != q.val:
        return False
    
    left = isSameTree(p.left, q.left)
    right = isSameTree(p.right, q.right)

    return left and right