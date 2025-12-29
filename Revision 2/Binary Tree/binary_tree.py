from collections import deque

class TreeNode:
    def __init__(self, val: int, left: TreeNode | None, right: TreeNode | None):
        self.val = val
        self.left = left
        self.right = right

def bfs_and_print_all_nodes(root: TreeNode | None):
    queue = deque([root])

    while queue:
        nodes_in_current_level = len(queue)
        # Do some logic here for curr. level.

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def bfs_contains(root: TreeNode | None, target: int) -> bool:
    if root is None:
        return False
    
    queue = deque([root])

    while queue:
        nodes_in_current_level = len(queue)

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            if node.val == target:
                return True
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return False

def dfs(node: TreeNode | None):
    if node == None:
        return
    
    dfs(node.left)
    dfs(node.right)

    return

def dfs_contains(node: TreeNode | None, target: int) -> bool:
    if node is None:
        return False

    if node.val == target:
        return True

    found_left = dfs_contains(node.left, target)

    if found_left:
        return True

    found_right = dfs_contains(node.right, target)

    return found_right

def preorder_dfs(node: TreeNode | None):
    if not node:
        return
    
    print(node.val)
    preorder_dfs(node.left)
    preorder_dfs(node.right)

    return

def inorder_dfs(node: TreeNode | None):
    if not node:
        return
    
    inorder_dfs(node.left)
    print(node.val)
    inorder_dfs(node.right)

    return

def postorder_dfs(node: TreeNode | None):
    if not node:
        return
    
    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.val)

    return

def bst_insert(node: TreeNode | None, val: int) -> TreeNode:
    # Empty spot: create node
    if node is None:
        return TreeNode(val, None, None)
    
    # Go left
    if val < node.val:
        node.left = bst_insert(node.left, val)

    # Go right
    elif val > node.val:
        node.right = bst_insert(node.right, val)

    # if val == node.val, do nothing (no dupl.)
    return node

def bst_search(node: TreeNode | None, target: int) -> bool:
    if node is None:
        return False
    
    if node.val == target:
        return True
    elif target < node.val:
        return bst_search(node.left, target)
    else:
        return bst_search(node.right, target)
    
"""
Key cases:

1. Leaf node -> remove directly.
2. One child -> replace node with child.
3. Two children -> Replace with inorder successor (min
of right subtree).
"""
def find_min(node: TreeNode) -> TreeNode:
    while node.left:
        node = node.left
    
    return node

def bst_remove(node: TreeNode | None, target: int) -> TreeNode | None:
    if node is None:
        return None
    
    if target < node.val:
        node.left = bst_remove(node.left, target)
    elif target > node.val:
        node.right = bst_remove(node.right, target)
    else:
        # Case 1: no children
        if node.left is None and node.right is None:
            return None
        
        # Case 2: one child
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        
        # Case 3: two children
        successor = find_min(node.right)
        node.val = successor.val
        """
        Delete successor.val from right subtree and give
        me back the (possibly changed) right subtree
        root.
        ↓↓↓
        """
        node.right = bst_remove(node.right, successor.val)

    return node