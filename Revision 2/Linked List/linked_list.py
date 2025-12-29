class Node:
    def __init__(self, data: int, next: Node | None):
        self.data = data
        self.next = next

def search_list(list: Node | None, target_data: int) -> Node | None:
    if (list is None): return None

    if (list.data == target_data): 
        return list
    else:
        return search_list(list.next, target_data)
    
def insert_list(list: Node | None, data: int) -> Node:
    return Node(data, list)

def predecessor_list(list: Node | None, target_data: int) -> Node | None:
    if (list is None or list.next is None):
        print("Error: predecessor sought on null list")
        
        return None
    
    if (list.next.data == target_data):
        return list
    else:
        return predecessor_list(list.next, target_data)

def delete_from_list(list: Node | None, target_data: int) -> Node | None:
    node_to_delete = search_list(list, target_data)

    if (node_to_delete is not None):
        pred_node = predecessor_list(list, target_data)

        if (pred_node is None):
            list = list.next
        else:
            pred_node.next = node_to_delete.next
    
    return list