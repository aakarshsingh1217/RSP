class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_middle(head: Node) -> int:
    if head is None:
        return float("inf")

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val

def append_node(head: Node, node_to_append: Node):
    if head is None:
        return node_to_append
    
    curr = head
    
    while curr.next:
        curr = curr.next

    curr.next = node_to_append

    return head
        

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

head = node_1
head = append_node(head, node_2)
head = append_node(head, node_3)
head = append_node(head, node_4)
head = append_node(head, node_5)

curr = head

while curr:
    print(f"{curr.val} -> ", end ="")
    curr = curr.next

print("X")
print(f"Middle val: {find_middle(head)}")
print(f"Middle val: {find_middle(Node(5))}")
print(f"Middle val: {find_middle(None)}")


"""
1 2 3 4 5 6 7 8 9 10 11
          X
                     y
"""