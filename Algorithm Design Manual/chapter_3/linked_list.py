class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def search_list(node, val):
    if (node is None):
        return None
    
    if (node.val == val):
        return node
    else:
        return (search_list(node.next, val))
    
def insert_list(head, val):
    new_node = Node(val)
    new_node.next = head

    return new_node

def item_ahead(node_1, node_2):
    if (node_1 is None or node_1.next is None):
        return None
    
    if (node_1.next is node_2):
        return node_1
    else:
        return item_ahead(node_1.next, node_2)
    
def delete_node(head, node_to_delete):
    # Case 1: empty list
    if head is None:
        return None

    # Case 2: deleting the head
    if head is node_to_delete:
        return head.next

    # Case 3: find predecessor
    pred = item_ahead(head, node_to_delete)

    # If pred is None, node was not found
    if pred is None:
        return head

    # Case 4: splice out the node
    pred.next = node_to_delete.next

    return head  # updated list head

def main():
    head = insert_list(None, 2)
    head = insert_list(head, 7)
    head = insert_list(head, 5)

    head = delete_node(head, head.next)

    curr = head

    while (curr != None):
        print(curr.val, end=" -> ")
        curr = curr.next

    print("X")

if __name__ == '__main__':
    main()