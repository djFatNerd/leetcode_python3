# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p1 = head
        # base case
        if not p1 or not p1.next:
            return p1
        
        # recursive case
        p2 = p1.next
        p1.next = self.swapPairs(p2.next)
        p2.next = p1
        
        return p2