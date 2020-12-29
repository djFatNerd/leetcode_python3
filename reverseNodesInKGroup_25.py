# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# recursive method
'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # base case 0
        if k == 1: return head
        # base case 1: len(L) < k 
        # 1-2-3 k = 4
        i = 0
        p = head
        while i < k:
            if not p: return head
            i+=1
            p = p.next

        # recurse
        p = self.reverseKGroup(p, k)
        
        # reverse k elements
        # head -------- p
        while k > 0:
            cur1 = head.next
            head.next = p
            p = head
            head = cur1
            k-=1

        head = p

        return head
'''
    
# iterative method
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # count length
        l = 0
        cur = head
        while(cur):
            l+=1
            cur = cur.next
        
        # store head
        dummy = ListNode(0)
        dummy.next = head
        
        # loop through
        prev = dummy
        tail = head
        while l >= k:
            for i in range(k - 1):
                after = tail.next.next
                tail.next.next = prev.next
                prev.next = tail.next
                tail.next = after
            
            prev = tail
            tail = tail.next
            l-=k
        
        return dummy.next