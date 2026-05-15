# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if self.helper(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def helper(self, first, second):

        if (first == None) != (second == None):
            return False
        if not first:
            return True
        if first.val != second.val:
            return False
        
        return self.helper(first.left, second.left) and self.helper(first.right, second.right)
