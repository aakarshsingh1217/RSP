class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def swapPairs(head: ListNode | None) -> ListNode | None:
    # Check edge case: LL has 0 or 1 nodes, just return.
    if not head or not head.next:
        return head
    
    dummy = head.next               # Step 5
    prev = None                     # Init. for step 3.

    while head and head.next:
        if prev:
            prev.next = head.next   # Step 4.
        
        prev = head                 # Step 3.

        next_node = head.next.next  # Step 2.
        head.next.next = head       # Step 1.

        head.next = next_node       # Step 6.
        head = next_node            # Move to next pair (step 3).

    return dummy