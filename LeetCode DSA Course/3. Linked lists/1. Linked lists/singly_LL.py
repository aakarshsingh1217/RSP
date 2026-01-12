class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

# Let prev_node be node at pos. i - 1
def add_node(prev_node: Node, node_to_add: Node):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

def delete_node(prev_node: Node):
    prev_node.next = prev_node.next.next

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

node_1.next = node_2
node_2.next = node_3
head = node_1