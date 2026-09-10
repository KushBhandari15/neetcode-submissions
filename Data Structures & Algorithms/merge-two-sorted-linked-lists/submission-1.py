# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = ListNode()
        curr = new_head
        pointer1 = list1
        pointer2 = list2

        while pointer1 and pointer2:
            if pointer1.val < pointer2.val:
                temp = ListNode(pointer1.val)
                pointer1 = pointer1.next
            else:
                temp = ListNode(pointer2.val)
                pointer2 = pointer2.next
            curr.next = temp
            curr = curr.next
        
        while pointer1:
            temp = ListNode(pointer1.val)
            curr.next = temp
            pointer1 = pointer1.next
            curr = curr.next
        while pointer2:
            temp = ListNode(pointer2.val)
            curr.next = temp
            pointer2 = pointer2.next
            curr = curr.next
        
        return new_head.next
            