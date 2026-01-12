class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def pairSum(head: ListNode | None) -> int:
    # Step 1: find middle.
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half.
    prev = None
    curr = slow

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Step 3: compute max twin sum.
    left = head
    right = prev # head of reversed second half.
    max_sum = 0

    while right:
        max_sum = max(max_sum, left.val + right.val)
        left = left.next
        right = right.next

    return max_sum

node_1: ListNode | None = ListNode(3)
node_2: ListNode | None = ListNode(5)
node_3: ListNode | None = ListNode(4)
node_4: ListNode | None = ListNode(2)
node_5: ListNode | None = ListNode(1)
node_6: ListNode | None = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6

head: ListNode | None = node_1

print(pairSum(head))