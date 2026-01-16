class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def path_sum(node: TreeNode | None, target_sum: int) -> bool:
    def dfs_sum(node: TreeNode, curr: int):
        if node is None:
            return False
        
        if node.left is None and node.right is None:
            return (node.val + curr) == target_sum
        
        curr += node.val
        left = dfs_sum(node.left, curr)
        right = dfs_sum(node.right, curr)

        return left or right
    
    return dfs_sum(node, 0) 

node_1 = TreeNode(0)
node_2 = TreeNode(1)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(6)
node_6 = TreeNode(2)
node_7 = TreeNode(5)

node_1.left = node_2
node_1.right = node_6
node_2.left = node_3
node_2.right = node_4
node_4.right = node_5
node_6.right = node_7

print(path_sum(node_1, 4))
print(path_sum(node_1, 55))
print(path_sum(node_1, 11))