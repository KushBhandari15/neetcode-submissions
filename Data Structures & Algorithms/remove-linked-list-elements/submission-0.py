# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if not prev:
                    temp = curr.next
                    curr.next = None
                    curr = temp
                    head = curr
                else:
                    prev.next = curr.next
                    curr.next = None
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next
        
        return head

        
