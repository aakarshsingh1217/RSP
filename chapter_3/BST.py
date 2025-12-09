class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.parent = None
        self.left = left
        self.right = right

        if (left is not None):
            left.parent = self
        if (right is not None):
            right.parent = self

def search_tree(node, val):
    if (node is None):
        return None
    
    if (node.val == val):
        return node
    
    if (val < node.val):
        return search_tree(node.left, val)
    else:
        return search_tree(node.right, val)
    
def find_minimum(node):
    curr_min = node

    if (node is None):
        return None
    
    while (curr_min.left is not None):
        curr_min = curr_min.left

    return curr_min

def find_maximum(node):
    curr_max = node

    if (node is None):
        return None
    
    while (curr_max.right is not None):
        curr_max = curr_max.right

    return curr_max

def insert_tree(node, val, parent = None):
    if node is None:
        new_node = TreeNode(val)
        new_node.parent = parent

        return new_node
    
    if (val < node.val):
        node.left = insert_tree(node.left, val, node)
    else:
        node.right = insert_tree(node.right, val, node)

    return node

def delete_tree(node, val):
    if (node is None):
        return None
    
    if (val < node.val):
        node.left = delete_tree(node.left, val)

        if (node.left is not None):
            node.left.parent = node
        
        return node
    elif (val > node.val):
        node.right = delete_tree(node.right, val)

        if (node.right is not None):
            node.right.parent = node

        return node
    
    if node.left is None and node.right is None:
        return None
    
    if node.left is None:
        node.right.parent = node.parent
        return node.right

    if node.right is None:
        node.left.parent = node.parent
        return node.left
    
    successor = find_minimum(node.right)
    node.val = successor.val
    node.right = delete_tree(node.right, successor.val)

    if node.right is not None:
        node.right.parent = node

    return node