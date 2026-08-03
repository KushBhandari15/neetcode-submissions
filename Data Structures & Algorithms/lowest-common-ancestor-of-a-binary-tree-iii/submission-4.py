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
        
        
        p_set = set()
        q_set = set()

        while p or q:

            if p:
                if p in q_set:
                    return p
                p_set.add(p)
                p = p.parent
            if q:
                if q in p_set:
                    return q
                q_set.add(q)
                q = q.parent
            
        return None