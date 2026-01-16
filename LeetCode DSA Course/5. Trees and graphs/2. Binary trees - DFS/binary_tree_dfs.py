class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

def dfs(node: TreeNode):
    if node == None:
        return
    
    dfs(node.left)
    dfs(node.right)

    return

def preorder_dfs(node: TreeNode):
    if not node:
        return
    
    print(node.val)
    preorder_dfs(node.left)
    preorder_dfs(node.right)

    return

def inorder_dfs(node: TreeNode):
    if not node:
        return
    
    inorder_dfs(node.left)
    print(node.val)
    inorder_dfs(node.right)

    return

def postorder_dfs(node):
    if not node:
        return
    
    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.val)

    return

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

preorder_dfs(node_1)
print("===========")
inorder_dfs(node_1)
print("===========")
postorder_dfs(node_1)