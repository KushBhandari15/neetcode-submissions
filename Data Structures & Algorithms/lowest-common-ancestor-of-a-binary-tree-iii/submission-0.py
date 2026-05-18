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
        
        def find_node(node, match):
            if not node:
                return None
            
            if node == match:
                return node
            
            res = find_node(node.left, match)
            if res:
                return res

            return find_node(node.right, match)
        
        first = find_node(root, p)
        second = find_node(root, q)
        temp = []
        while first:
            temp.append(first)
            first = first.parent
        
        while second:
            if second in temp:
                return second
            second = second.parent
        return Node()
