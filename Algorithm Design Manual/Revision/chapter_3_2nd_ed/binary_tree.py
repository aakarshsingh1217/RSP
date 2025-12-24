class TreeNode:
    def __init__(self, left, right, parent, item):
        self.left = left
        self.right = right
        self.parent = parent
        self.item = item

def search_tree(tree, target):
    if (tree is None): return None
    if (tree.item == target): return tree

    if (target < tree.item):
        return search_tree(tree.left, target)
    else:
        return search_tree(tree.right, target)
    
def find_min(tree):
    if (tree is None): return None

    min = tree

    while (min.left is not None):
        min = min.left

    return min

def in_order_traversal(tree):
    """
    Visits left subtree, then node,
    then right subtree.
    Prints vals. in sorted order.
    """
    if (tree is not None):
        in_order_traversal(tree.left)
        print(tree.item)
        in_order_traversal(tree.right)

def pre_order_traversal(tree):
    """
    Visits node before its children.
    """
    if (tree is not None):
        print(tree.item)
        pre_order_traversal(tree.left)
        pre_order_traversal(tree.right)

def post_order_traversal(tree):
    """
    Visits children before node.
    """
    if (tree is not None):
        post_order_traversal(tree.left)
        post_order_traversal(tree.right)
        print(tree.item)