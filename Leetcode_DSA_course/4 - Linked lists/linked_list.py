class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
one.next = two
head = one

curr = head

while (curr != None):
    print(f"{curr.val} -> ", end="")
    curr = curr.next

print("X")