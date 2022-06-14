class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        prev=None
        curr=head
        while curr:
            next_n=curr.next
            curr.next=prev
            prev=curr
            curr=next_n
        while head:
            if head.val!=prev.val:
                return False
            else:
                head=head.next
                prev=prev.next
        return True