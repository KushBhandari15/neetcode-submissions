# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head
        helper = []

        while curr:
            helper.append(curr.val)
            curr = curr.next
        
        curr = head
        i, j = 0, 1
        n = len(helper)
        while curr:
            if i%2 == 0:
                curr.val = helper[i//2]
            else:
                curr.val = helper[n-j]
                j += 1
            
            i += 1
            curr = curr.next

