# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # Reverse list2
        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        pointer1, pointer2 = head, prev
        # Make new list
        while pointer2:
            temp1, temp2 = pointer1.next, pointer2.next
            pointer1.next = pointer2
            pointer2.next = temp1
            pointer1, pointer2 = temp1, temp2
