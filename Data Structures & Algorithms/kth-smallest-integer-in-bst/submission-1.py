# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        counter = k
        ans = None
        def helper(node):
            nonlocal counter, ans
            if not node or ans is not None:
                return -1
            
            helper(node.left)

            counter -= 1
            if counter == 0:
                ans = node.val

            helper(node.right)

        helper(root)
        return ans