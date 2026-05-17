# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        def helper(node, curr):

            curr += node.val
            
            if not node.left and not node.right:
                return curr == targetSum
            
            left = helper(node.left, curr) if node.left else False
            right = helper(node.right, curr) if node.right else False

            return left or right
        
        return helper(root, 0)

