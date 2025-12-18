from collections import deque

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def print_all_nodes(root):
    queue = deque([root])

    while (queue):
        nodes_in_curr_level = len(queue)

        for _ in range (nodes_in_curr_level):
            node = queue.popleft()

            print(node.val)

            if (node.left):
                queue.append(node.left)
            if (node.right):
                queue.append(node.right)