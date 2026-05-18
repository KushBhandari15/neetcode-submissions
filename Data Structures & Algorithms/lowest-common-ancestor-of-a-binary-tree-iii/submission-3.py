"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        first = p
        second = q
        helper = set()
        while first:
            helper.add(first)
            first = first.parent
        
        while second:
            if second in helper:
                return second
            second = second.parent
        return Node()
