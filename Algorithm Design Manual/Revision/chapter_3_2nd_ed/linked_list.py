class ListNode:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


def search_list(head, target):
    if (head is None):
        return None
    
    if (head.item == target):
        return head
    
    return search_list(head.next, target)


def delete_list(head, target):
    # Case 1: empty list
    if (head is None):
        return None

    # Case 2: delete head
    if (head.item == target):
        return head.next

    # Case 3: delete non-head
    curr = head

    while curr.next:
        if (curr.next.item == target):
            curr.next = curr.next.next

            return head
        
        curr = curr.next

    return head  # target not found

node_1 = ListNode(3, None)
node_2 = ListNode(5, None)
node_3 = ListNode(7, None)

node_1.next = node_2
node_2.next = node_3

head = node_1

print(f"Found node 2: {search_list(head, 5).item}")

head = delete_list(head, 5)
print(search_list(head, 5))  # None

curr = head

while (curr is not None):
    print(f"{curr.item} -> ", end="")
    curr = curr.next

print("X")