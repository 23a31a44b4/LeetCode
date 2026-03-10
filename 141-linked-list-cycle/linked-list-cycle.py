# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            slow=head
            if head.next:
                fast=head.next
            else:
                fast=None
            arr=[]
            while fast and fast.next:
                if slow and fast  in arr:
                    return True
                arr.append(slow)
                arr.append(fast)
                slow=slow.next
                fast=fast.next
            return False
