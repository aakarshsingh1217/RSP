from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.parent = None
        self.val = x
        self.left = None
        self.right = None

def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    def dfs(node: TreeNode, parent: TreeNode):
        if not node:
            return
        
        node.parent = parent
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)

    queue = deque([target])
    seen = {target}
    distance = 0

    while queue and distance < k:
        current_length = len(queue)

        for _ in range(current_length):
            node = queue.popleft()

            for neighbour in [node.left, node.right, node.parent]:
                if neighbour and neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(neighbour)

        distance += 1

    return [node.val for node in queue]