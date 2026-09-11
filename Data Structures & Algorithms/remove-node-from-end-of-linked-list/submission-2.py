# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        n = size - n

        if n == 0:
            return head.next
        prev = None
        curr = head

        for _ in range(n ):
            prev = curr
            curr = curr.next
        
        print(prev.val)
        print(curr.val)
        prev.next = curr.next
        curr.next = None
        
        return head