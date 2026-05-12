# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        self.val = val
        def helper(curr):

            if not curr:
                return None
            

            curr.next = helper(curr.next)

            if curr.val == self.val:
                return curr.next
            
            return curr
        
        return helper(head)


        
