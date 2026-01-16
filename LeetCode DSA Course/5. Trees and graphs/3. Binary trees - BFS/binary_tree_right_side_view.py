from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode | None) -> list[int]:
    def bfs(root: TreeNode | None, rightmost_vals: list[int]):
        if root is None:
            return rightmost_vals

        queue = deque([root])

        while queue:
            num_nodes_in_queue = len(queue)
            rightmost_val = float("-inf")

            for _ in range(num_nodes_in_queue):
                node = queue.popleft()

                rightmost_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            rightmost_vals.append(rightmost_val)

        return rightmost_vals

    return bfs(root, [])


"""
Better sol.:

def rightSideView(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    ans = []
    queue = deque([root])

    while queue:
        curr_len = len(queue)

        # This is the rightmost node for the curr. level.
        ans.append(queue[-1].val)

        for _ in range(curr_len):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans
"""