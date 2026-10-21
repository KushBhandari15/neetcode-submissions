# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        k = len(lists)

        arr = []
        for head in lists:
            curr = head
            while curr:
                arr.append(curr.val)
                curr = curr.next
        
        idx = 0
        head = ListNode()
        curr = head

        for num in sorted(arr):
            curr.next = ListNode(num)
            curr = curr.next
        
        return head.next