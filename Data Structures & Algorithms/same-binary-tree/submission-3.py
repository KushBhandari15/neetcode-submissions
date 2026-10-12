# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(first, second):
            if not first and not second:
                return True

            # Only one node is None
            if not first or not second:
                return False

            # Values don't match
            if first.val != second.val:
                return False
            
            left = dfs(first.left, second.left)
            if not left:
                return False
            right = dfs(first.right,second.right)
            if not right:
                return False
            
            return True


        return dfs(p, q)
                