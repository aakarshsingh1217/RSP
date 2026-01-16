# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode | None) -> int:
    if root is None:
        return 0

    def dfs(node: TreeNode | None, curr_len: int):
        if node is None:
            return curr_len

        left = dfs(node.left, curr_len + 1)
        right = dfs(node.right, curr_len + 1)

        return max(left, right)
    
    left_max = dfs(root.left, 0)
    right_max = dfs(root.right, 0)

    return left_max + right_max

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_3 = TreeNode(3)
node_6 = TreeNode(6)
node_7 = TreeNode(7)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5
node_5.right = node_6
node_6.right = node_7

print(diameterOfBinaryTree(node_1))