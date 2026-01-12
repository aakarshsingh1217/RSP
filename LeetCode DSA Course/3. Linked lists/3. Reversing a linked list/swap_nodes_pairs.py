class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def swap_nodes_in_pairs(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None
    if head.next is None:
        return head
    
    prev = None
    curr = head

    while curr and curr.next:
        next_pair_start = curr.next.next

        if prev is not None:
            prev.next = curr.next
        else:
            head = curr.next

        curr.next.next = curr
        curr.next = next_pair_start
        prev = curr
        curr = next_pair_start

    return head

node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)
node_6 = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6

head = node_1
head = swap_nodes_in_pairs(head)

while head:
    print(f"{head.val} -> ", end="")
    head = head.next

print("X")