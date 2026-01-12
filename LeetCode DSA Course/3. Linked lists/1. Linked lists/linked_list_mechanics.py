def get_sum(head):
    ans = 0

    while head:
        ans += head.val
        head = head.next

    return ans

def get_sum(head):
    if not head:
        return 0
    
    return head.val + get_sum(head.next)