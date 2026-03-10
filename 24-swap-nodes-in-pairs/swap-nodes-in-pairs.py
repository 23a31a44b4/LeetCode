# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        res=temp=ListNode()
        while head:
            temp.next=head
            head=head.next
            temp=temp.next
        prev=res
        slow=res.next
        if slow.next!=None:
            fast=slow.next
        while slow and slow.next:
            temp1=fast.next
            fast.next=slow
            slow.next=temp1
            prev.next=fast
            if prev.next.next:
                prev=prev.next.next
            if fast.next.next:
                slow=fast.next.next
            if slow.next:
                fast=slow.next
        return res.next
