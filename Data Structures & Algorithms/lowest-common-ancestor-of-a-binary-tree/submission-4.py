# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def path(node, target, curr_path):

            if node == target:
                return curr_path + [node]
            if not node:
                return []
            # Left
            left_path = path(node.left, target, curr_path + [node])
            if left_path:
                return left_path
            # Right 
            right_path = path(node.right, target, curr_path + [node])
            if right_path:
                return right_path
        
            return []
        
        p_path = path(root, p, [])
        q_path = path(root, q, [])
        i, j = 0, 0
        n, m = len(p_path), len(q_path)
        lowest = None
        while i < n and j < m:
            if p_path[i] != q_path[j]:
                return lowest
            lowest = p_path[i]
            i += 1
            j += 1
        
        return lowest