class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head: Node | None) -> Node | None:
    prev = None
    curr = head

    while curr:
        next_node = curr.next # first make sure we don't lose next node
        curr.next = prev # reverse direction of pointer
        prev = curr # set curr node to prev for the next node
        curr = next_node # move on

    return prev