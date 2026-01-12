class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be node at pos. i
def add_node(node: Node, node_to_add: Node):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add