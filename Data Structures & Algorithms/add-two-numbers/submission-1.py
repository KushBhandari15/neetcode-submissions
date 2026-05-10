# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        pointer1, pointer2 = l1, l2
        num1, num2 = 0, 0
        curr = 0
        while pointer1 and pointer2:
            val1 = pointer1.val; val2 = pointer2.val
            num1 = (num1 * 10) + val1
            num2 = (num2 * 10) + val2
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            curr += 1
        
        while pointer1:
            val1 = pointer1.val
            num1 = (num1 * 10) + val1
            pointer1 = pointer1.next
            curr += 1
        while pointer2:
            val2 = pointer2.val
            num2 = (num2 * 10) + val2
            pointer2 = pointer2.next
            curr += 1
        print(num1, num2)
        num1 = int(str(num1)[::-1])
        num2 = int(str(num2)[::-1])
        add = num1 + num2
        if add == 0:
            return ListNode(0)
        print(add)
        head = ListNode()
        res = head
        while add != 0:
            temp = add%10
            currNode = ListNode(temp)
            res.next = currNode
            res = res.next
            add = add // 10

        return head.next
        

