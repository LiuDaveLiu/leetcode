def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    while head and head.val==val:
        head=head.next
        if not head or head.val!=val: break
    ans=head
    while head and head.next:
        if head.next.val==val:
            head.next=head.next.next
        else:
            head=head.next
    return ans