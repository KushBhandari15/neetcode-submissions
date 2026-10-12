# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same(first, second):

            if not first and not second:
                return True
            if not first or not second:
                return False
            if first.val != second.val:
                return False
            
            left = is_same(first.left, second.left)
            if not left:
                return False
            right = is_same(first.right, second.right)
            if not right:
                return False
            
            return True
        
        def traverse(node):
            if not node:
                return False
            if is_same(node, subRoot):
                return True

            return traverse(node.left) or traverse(node.right)
        
        return traverse(root)
            
        