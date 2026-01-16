class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def goodNodes(root: TreeNode | None) -> int:
    """
    Same format of DFS where we def. our func. to return ans.
    to original prob. and as we implement it we assume
    it's already working.
    """
    def dfs(node: TreeNode | None, maxSoFar: int):
        if not node:
            return 0

        """
        Since curr. node is on path from original root to children,
        if it's larger than maxSoFar we need to update it.
        """
        left = dfs(node.left, max(maxSoFar, node.val))
        right = dfs(node.right, max(maxSoFar, node.val))

        # Num. good nodes in left + right subtree + 1 if curr.
        # node is good.
        ans = left + right

        if node.val >= maxSoFar:
            ans += 1

        return ans
    
    return dfs(root, float("-inf"))