from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_all_nodes(root: TreeNode | None):
    queue = deque([root])

    while queue:
        nodes_in_curr_level = len(queue)
        # Do some logic for curr. level.

        for _ in range(nodes_in_curr_level):
            node = queue.popleft()
            # Do some logic here for curr. node.
            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


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

print_all_nodes(node_1)