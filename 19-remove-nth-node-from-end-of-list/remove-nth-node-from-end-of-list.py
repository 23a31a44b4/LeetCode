# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head)
        diff=cur=dummy
        for i in range(n):
            diff=diff.next
        while diff.next:
            cur=cur.next
            diff=diff.next
        cur.next=cur.next.next
        return dummy.next