# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def helper(node, count):
            if not node:
                return count
            
            count += 1
            left = helper(node.left, count)
            right = helper(node.right, count)
            res = max(left, right)
        
            return res
        
        return helper(root, 0)