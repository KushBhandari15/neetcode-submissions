# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def get_path(node, target, path):
            if not node:
                return []

            path.append(node)

            if node == target:
                return path.copy()
            
            left = get_path(node.left, target, path)
            if left:
                return left
            right = get_path(node.right, target, path)
            if right:
                return right
            
            path.pop()
            return None
        
        first = get_path(root, p, [])
        second = get_path(root, q, [])
        lca = root

        for a, b in zip(first, second):
            if a != b:
                return lca
            lca = a
        
        return lca

        
