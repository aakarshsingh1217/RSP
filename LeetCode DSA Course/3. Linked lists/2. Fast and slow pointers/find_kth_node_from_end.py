class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_kth_node_frm_end(head: Node | None, k: int) -> Node | None:
    fast = head
    slow = head

    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow