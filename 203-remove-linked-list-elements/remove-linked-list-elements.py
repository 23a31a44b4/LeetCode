# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res=prev=ListNode()
        temp=head
        while temp:
            if temp.val!=val:
                prev.next=temp
                prev=prev.next
            else:
                prev.next=temp.next
            temp=temp.next

        return res.next