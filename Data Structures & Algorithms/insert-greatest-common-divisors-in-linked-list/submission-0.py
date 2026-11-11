import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        prev = head
        curr = head.next

        while curr:
            divisor = math.gcd(prev.val, curr.val)
            new = ListNode(divisor)
            prev.next = new
            new.next = curr
            prev = curr
            curr = curr.next
        
        return head