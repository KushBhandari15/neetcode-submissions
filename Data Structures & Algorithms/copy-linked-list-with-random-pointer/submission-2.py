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
        
        helper = {None: None}
        curr = head

        while curr:
            copy = Node(curr.val)
            helper[curr] = copy
            curr = curr.next
        
        curr = head
        
        while curr:
            copy = helper[curr]
            copy.next = helper[curr.next]
            copy.random = helper[curr.random]
            curr = curr.next
        
        return helper[head]