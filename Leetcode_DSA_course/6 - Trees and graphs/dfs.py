class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def dfs(node):
    if (node == None):
        return
    
    dfs(node.left)
    dfs(node.right)

    return

def preorder_dfs(node):
    if (not node):
        return
    
    print(node.val)
    preorder_dfs(node.left)
    preorder_dfs(node.right)

    return

def inorder_dfs(node):
    if (not node):
        return
    
    inorder_dfs(node.left)
    print(node.val)
    inorder_dfs(node.right)

    return

def postorder_dfs(node):
    if (not node):
        return
    
    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.val)
    
    return