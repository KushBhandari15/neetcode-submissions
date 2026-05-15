# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        is_same = True

        def helper(first, second):
            nonlocal is_same
            if not is_same: 
                return
            
            # Structural check
            if (first is None) != (second is None):
                is_same = False
                return
            
            # Both are None (they match structurally here)
            if not first:
                return
            
            # Value check
            if first.val != second.val:
                is_same = False
                return

            helper(first.left, second.left)
            helper(first.right, second.right)
            
        helper(p, q)
        return is_same