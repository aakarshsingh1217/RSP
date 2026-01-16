class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: TreeNode | None, low: int, high: int):
    if not root:
        return 0

    ans = 0

    if low <= root.val <= high:
        ans += root.val

    if low < root.val:
        ans += rangeSumBST(root.left, low, high)
    if root.val < high:
        ans += rangeSumBST(root.right, low, high)

    return ans

node_10 = TreeNode(10)
node_5 = TreeNode(5)
node_15 = TreeNode(15)
node_3 = TreeNode(3)
node_18 = TreeNode(18)
node_7 = TreeNode(7)

node_10.left = node_5
node_10.right = node_15
node_5.left = node_3
node_5.right = node_7
node_15.right = node_18

print(rangeSumBST(node_10, 7, 15))