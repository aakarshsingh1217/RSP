class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root: TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return TreeNode(val)

    def dfs(node: TreeNode | None, val: int):
        if node is None:
            return None

        left = None
        right = None
        
        if val < node.val:
            left = dfs(node.left, val)
        if val > node.val:
            right = dfs(node.right, val)

        if left is None or right is None:
            if left is None and val < node.val:
                node.left = TreeNode(val)
            if right is None and val > node.val:
                node.right = TreeNode(val)

        return node

    return dfs(root, val)