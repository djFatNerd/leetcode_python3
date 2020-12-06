# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:         
        cur1 = l1
        cur2 = l2
        inc = 0
        
        # loop till at least one has no elements left 
        while(cur1.next and cur2.next):
            add = cur1.val + cur2.val + inc
            cur1.val = add % 10
            inc = add >= 10
            cur1 = cur1.next
            cur2 = cur2.next
        
        # connect rest of L1 and L2, store in L1
        if not cur1.next:
            cur1.next = cur2.next
   
        # store cur2.val in inc to avoid messy computing
        inc += cur2.val
        
        # simple adding inc from cur1
        while cur1.next and inc > 0:
            new_inc = (cur1.val + inc) >= 10
            cur1.val = (cur1.val + inc) % 10
            inc = new_inc
            cur1 = cur1.next
        
        # breaked because no inc
        if inc == 0: return l1
        
        #breaked because no next
        if cur1.val + inc >= 10: cur1.next = ListNode(1)
        cur1.val = (inc + cur1.val) % 10
        
        return l1