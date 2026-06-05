# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        helper = []

        curr = head
        while curr:
            helper.append(curr)
            curr = curr.next
        
        size = len(helper)
        delete_node = helper[-n]

        prev = None
        curr = head
        while True:
            if curr == delete_node:
                if prev == None:
                    head = curr.next
                    curr.next = None
                else:
                    prev.next = curr.next
                    curr.next = None
                break
            else:
                prev = curr
                curr = curr.next
        
        return head
            
