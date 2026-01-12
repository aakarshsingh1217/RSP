class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_to_end(node_to_add: Node):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add

def remove_from_end():
    if head.next == tail:
        return
    
    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

def add_to_start(node_to_add: Node):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add

def remove_from_start():
    if head.next == tail:
        return
    
    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

def get_sum_with_dummy(head: Node):
    ans = 0
    curr = head

    while curr:
        ans += curr.val
        curr = curr.next

    # same as before, but we still have pointer to head.
    return ans

head = Node(None)
tail = Node(None)

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_1.next = node_2
node_2.prev = node_1
node_2.next = node_3
node_3.prev = node_2

curr = node_1

while curr:
    print(f"{curr.val} <-> ", end="")
    curr = curr.next

print("X")

curr = node_3

while curr:
    print(f"{curr.val} <-> ", end="")
    curr = curr.prev

print("X")