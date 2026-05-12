# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []
        def helper(node):
            if not node:
                return None
            if not node.left and not node.right:
                self.res.append(node.val)
                return
            
            left = helper(node.left)
            # if left: self.res.append(left) 
            self.res.append(node.val)
            right = helper(node.right)
            # if right: self.res.append(right)
            
        
        helper(root)
        return self.res
            