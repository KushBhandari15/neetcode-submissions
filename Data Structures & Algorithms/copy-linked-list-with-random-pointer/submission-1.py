"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
            
        root = Node(head.val)

        curr = root
        tracker = head.next

        helper = {head: curr}

        while tracker:
            nxt = Node(tracker.val)
            curr.next = nxt

            curr = curr.next
            helper[tracker] = curr
            tracker = tracker.next
        
        curr.next = None

        first = root
        second = head

        while second:
            if second.random == None:
                first.random = None
            else:
                first.random = helper[second.random]
            first = first.next
            second = second.next
        
        return root


