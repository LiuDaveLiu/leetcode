def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    p1=p2=head
    counter=0
    while head:
        head=head.next
        counter+=1
    # reverse the second half
    half=counter//2
    for i in range(half):
        p1=p1.next
    
    prev=None
    curr=p1
    while curr:
        next_n=curr.next
        curr.next=prev
        prev=curr
        curr=next_n
    
    for i in range(half):
        if p2.val!=prev.val:
            return False
        else:
            p2=p2.next
            prev=prev.next
        
    return True